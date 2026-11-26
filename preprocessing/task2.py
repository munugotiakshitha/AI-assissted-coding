import pandas as pd

data = pd.read_csv("sales_data.csv")
data.columns = data.columns.str.strip()

# Change these names to match your CSV headings.
DATE_COLUMN = "Date"
SALES_COLUMN = "Sales"

if DATE_COLUMN not in data.columns:
    raise ValueError(f"Date column '{DATE_COLUMN}' was not found. Check the CSV headings.")

if SALES_COLUMN not in data.columns:
    raise ValueError(f"Sales column '{SALES_COLUMN}' was not found. Check the CSV headings.")

# Convert dates and remove rows where the date could not be read.
data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN], errors="coerce")
data = data.dropna(subset=[DATE_COLUMN]).copy()

# Add time-based features.
data["Month"] = data[DATE_COLUMN].dt.month
data["Year"] = data[DATE_COLUMN].dt.year
data["DayOfWeek"] = data[DATE_COLUMN].dt.day_name()

# Convert sales to numbers and fill missing sales with the median.
data[SALES_COLUMN] = pd.to_numeric(data[SALES_COLUMN], errors="coerce")
data[SALES_COLUMN] = data[SALES_COLUMN].fillna(data[SALES_COLUMN].median())

# Cap extreme sales values using the IQR method.
q1 = data[SALES_COLUMN].quantile(0.25)
q3 = data[SALES_COLUMN].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

data[SALES_COLUMN] = data[SALES_COLUMN].clip(lower_limit, upper_limit)

# Min-max normalize sales to a range from 0 to 1.
minimum = data[SALES_COLUMN].min()
maximum = data[SALES_COLUMN].max()

if maximum != minimum:
    data["Sales_Normalized"] = (data[SALES_COLUMN] - minimum) / (maximum - minimum)
else:
    data["Sales_Normalized"] = 0.0

print(data.head())
data.to_csv("sales_data_preprocessed.csv", index=False)
print("Saved as sales_data_preprocessed.csv")