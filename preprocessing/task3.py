import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline

data = pd.read_csv("healthcare.csv")
data.columns = data.columns.str.strip()

# Change this to the target/outcome column in your dataset.
TARGET_COLUMN = "target"

if TARGET_COLUMN not in data.columns:
    raise ValueError(
        f"Target column '{TARGET_COLUMN}' was not found. "
        f"Available columns: {list(data.columns)}"
    )

# Convert requested medical measurements to numeric if present.
for column in ("blood_pressure", "BloodPressure", "cholesterol", "Cholesterol"):
    if column in data.columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

# Separate features from the value to predict.
X = data.drop(columns=[TARGET_COLUMN])
y = data[TARGET_COLUMN]

# Identify numeric and categorical columns.
numeric_columns = X.select_dtypes(include="number").columns.tolist()
categorical_columns = X.select_dtypes(exclude="number").columns.tolist()

# Fill numeric missing values with medians and scale numeric features.
numeric_pipeline = Pipeline([
    ("fill_missing", SimpleImputer(strategy="median")),
    ("scale", MinMaxScaler()),
])

# Fill categorical missing values and convert categories into indicator columns.
categorical_pipeline = Pipeline([
    ("fill_missing", SimpleImputer(strategy="most_frequent")),
    ("encode", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_columns),
    ("categorical", categorical_pipeline, categorical_columns),
])

# Split first so preprocessing is learned from the training data only.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train_ready = preprocessor.fit_transform(X_train)
X_test_ready = preprocessor.transform(X_test)

print("Training rows:", X_train_ready.shape[0])
print("Testing rows:", X_test_ready.shape[0])
print("Processed feature count:", X_train_ready.shape[1])

# Save the processed feature sets.
# These files are suitable for passing into a machine-learning model.
pd.DataFrame(X_train_ready.toarray() if hasattr(X_train_ready, "toarray")
             else X_train_ready).to_csv("healthcare_X_train.csv", index=False)
pd.DataFrame(X_test_ready.toarray() if hasattr(X_test_ready, "toarray")
             else X_test_ready).to_csv("healthcare_X_test.csv", index=False)
y_train.to_csv("healthcare_y_train.csv", index=False)
y_test.to_csv("healthcare_y_test.csv", index=False)

print("Saved the processed training and testing data.")