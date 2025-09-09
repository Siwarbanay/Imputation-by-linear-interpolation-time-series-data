# Imputation-by-linear-interpolation-time-series-data

This Python script is designed to interpolate interest rates for financial instruments based on a given yield curve. It uses the Alteryx Python SDK, pandas for data manipulation, and scipy for interpolation. Here's a detailed breakdown:

Imports:

Alteryx: For reading and writing data in the Alteryx workflow
pandas: For data manipulation and analysis
interp1d from scipy.interpolate: For performing linear interpolation
Data Input:

isins_df: Reads input data containing ISIN (International Securities Identification Number) information from Alteryx input #1
courbe_df: Reads yield curve data from Alteryx input #2 (EUR 3M curve)
Data Preparation:

Converts date columns to pandas datetime format for proper date handling
Maturity in isins_df
date_valorisation (valuation date) and maturite_point_courbe (curve point maturity) in courbe_df
Main Processing:

Initializes an empty list results to store the final output
Gets unique valuation dates from the yield curve data
For each valuation date: a. Filters the yield curve data for that specific date b. Calculates the time to maturity (in days) for each curve point c. Creates a linear interpolation function using the curve's maturity and rate data d. For each ISIN in the input data:
Calculates the time to maturity (delta) for that ISIN
Interpolates the rate based on the yield curve
Stores the results with ISIN information, valuation date, maturity, and interpolated rate e. Handles cases where interpolation might fail by setting the interpolated rate to None
Output:

Converts the results list to a pandas DataFrame
Writes the final DataFrame to Alteryx output #1
Key Features:

The script performs linear interpolation of interest rates based on a yield curve
It handles multiple valuation dates in the input data
The interpolation includes extrapolation for maturities outside the defined curve points
Error handling is implemented to ensure the script continues even if interpolation fails for some dates
Note: This script appears to be part of an Alteryx workflow, which is a data analytics platform. The #1 and #2 in the read functions refer to specific input connections in the Alteryx workflow, and the 1 in the write function refers to an output connection.
