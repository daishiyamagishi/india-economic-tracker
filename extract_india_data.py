import pandas as pd
import wbgapi as wb

print("Fetching economic data for India from the World Bank...")

# Define parameters
country_code = "IND"  # ISO code for India
indicators = {
    "GDP_Growth": "NY.GDP.MKTP.KD.ZG",  # GDP growth (annual %)
    "Inflation": "FP.CPI.TOTL.ZG",  # Inflation, consumer prices (annual %)
}
start_year = 2010
end_year = 2025

# Fetch data using wbgapi and convert to a Pandas DataFrame
# 'mrv' or custom time range can be specified. Here we use a range from start_year to end_year
df = wb.data.DataFrame(
    list(indicators.values()),
    country_code,
    range(start_year, end_year + 1),
    numericTimeKeys=True,
    columns="series",
).reset_index()

# Clean up column headers to make them user-friendly
df.rename(
    columns={
        "time": "Year",
        "NY.GDP.MKTP.KD.ZG": "GDP_Growth_Pct",
        "FP.CPI.TOTL.ZG": "Inflation_Pct",
    },
    inplace=True,
)

# Sort by year
df = df.sort_values(by="Year", ascending=True)

# Display the extracted data in the console
print("\nExtracted Data Preview:")
print(df.head(10))

# Export clean data to a CSV file (ready to load into SQL or Power BI)
output_filename = "india_economic_data.csv"
df.to_csv(output_filename, index=False)
print(f"\nSuccess! Data saved locally to '{output_filename}'")
