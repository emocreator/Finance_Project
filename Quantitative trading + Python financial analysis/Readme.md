# Stock Data Analysis

This script provides an in-depth analysis of stock data for various symbols. It fetches historical stock data, performs various data transformations, and visualizes the results.

## Libraries Used:
- `yfinance`: For fetching stock data.
- `warnings`: To suppress any warnings for cleaner output.
- `pandas`: For data manipulation and analysis.
- `matplotlib`: For data visualization.
- `numpy`: For numerical operations.

## Features:

1. **Data Retrieval and Merging**: 
   - Fetches closing price data from 2010-01-01 till now for a predefined list of stock symbols.
   - Merges individual stock dataframes into a unified dataframe based on the 'Date' column.
   
2. **Data Visualization**:
   - Plots the closing prices for all stocks in separate subplots.
   - Displays summary statistics, mean, and data information.
   - Plots mean percentage change for stocks.
   
3. **Data Analysis**:
   - Calculates differences between consecutive rows to get day-over-day change.
   - Calculates percentage changes between consecutive rows.
   - Calculates log returns for stock data.
   - Determines positions based on moving averages' cross.
   - Fits a linear regression between `^SPX` and `^VIX` returns.
   - Calculates rolling correlation between `^SPX` and `^VIX` returns.

4. **Data Resampling**:
   - Resamples data to weekly and monthly frequency.
   
5. **Rolling Statistics**:
   - Calculates rolling statistics for the `AAPL` stock.
   
6. **Scatter Matrices**:
   - Creates scatter matrices for returns with histogram and kernel density estimates.

## Visualization:

The script uses `matplotlib` to visualize data in various formats such as line plots, bar plots, and scatter plots. It also uses the scatter matrix functionality of `pandas` to visualize relationships between different stock returns.
