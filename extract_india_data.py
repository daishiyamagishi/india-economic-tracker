from datetime import datetime
import pandas as pd
import wbgapi as wb

print(
    "Fetching comprehensive historical economic & structural data for India"
    " from the World Bank..."
)

# Define parameters
country_code = "IND"  # ISO code for India
indicators = {
    "GDP_Growth": "NY.GDP.MKTP.KD.ZG",  # GDP growth (annual %)
    "Inflation": "FP.CPI.TOTL.ZG",  # Inflation, consumer prices (annual %)
    "Unemployment": "SL.UEM.TOTL.ZS",  # Unemployment (% of total labor force)
    "Mobile_Subscriptions": "IT.CEL.SETS.P2",  # Mobile cellular subscriptions (per 100 people)
    "FDI_Inflows_Pct_GDP": "BX.KLT.DINV.WD.GD.ZS",  # Foreign direct investment, net inflows (% of GDP)
    "Gross_Capital_Formation": "NE.GDI.TOTL.ZS",  # Gross capital formation (% of GDP - investment/infrastructure)
}

# Automatically set start year to World Bank's earliest records (1960)
# and end year to the current year dynamically
start_year = 1960
end_year = datetime.now().year

# Fetch data using wbgapi and convert to a Pandas DataFrame
df = wb.data.DataFrame(
    list(indicators.values()),
    country_code,
    range(start_year, end_year + 1),
    numericTimeKeys=True,
    columns="series",
).reset_index()

# Clean up column headers to match user-friendly names
df.rename(
    columns={
        "time": "Year",
        "NY.GDP.MKTP.KD.ZG": "GDP_Growth_Pct",
        "FP.CPI.TOTL.ZG": "Inflation_Pct",
        "SL.UEM.TOTL.ZS": "Unemployment_Pct",
        "IT.CEL.SETS.P2": "Mobile_Subscriptions_Per_100",
        "BX.KLT.DINV.WD.GD.ZS": "FDI_Inflows_Pct_GDP",
        "NE.GDI.TOTL.ZS": "Gross_Capital_Formation_Pct_GDP",
    },
    inplace=True,
)

# Sort by year in ascending order
df = df.sort_values(by="Year", ascending=True)

# Display a preview of recent data in the console logs
print("\nExtracted Data Preview (Recent Years):")
print(df.tail(10))

# Export comprehensive clean data to CSV file
output_filename = "india_economic_data.csv"
df.to_csv(output_filename, index=False)
print(
    f"\nSuccess! Comprehensive historical dataset saved locally to"
    f" '{output_filename}'"
)
