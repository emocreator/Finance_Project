# Stock Analysis with Python

This project provides a detailed analysis of stock prices for a selected list of securities using Python's powerful data analysis libraries.

## Libraries Used:
- yfinance: To fetch stock data.
- pandas: For data manipulation and analysis.
- numpy: For numerical calculations.
- matplotlib: For plotting.

## Overview:

1. **Data Fetching**:
    - A list of stock symbols is provided, which includes major companies and indices.
    - Stock data is fetched from Yahoo Finance for each stock symbol from January 1, 2010, to the present day.

2. **Data Analysis**:
    - All fetched data is merged on the 'Date' column to create a unified dataframe.
    - Basic statistics are derived from the merged data, including mean, standard deviation, and percent change.
    - The data is visualized using line plots and bar plots for a clearer understanding of stock price movements.
    - Log returns for the stocks are calculated and analyzed.
    - Cumulative returns are plotted.
    - Data is resampled to weekly and monthly intervals for a different perspective.
    - Rolling statistics, including min, max, mean, and standard deviation, are calculated.
    - Moving averages are used to derive trading positions based on crossovers.
    - Specific stocks and indices are visualized together, with one being used as a secondary axis for better comparison.

3. **Visualization**:
    - Scatter matrices are created for the returns to analyze the relationships between different stocks/indices.
    - Different visualizations are used to present stock data, returns, moving averages, and trading positions.

## Key Insights:
- The project provides a holistic view of the stock prices and their movements over time.
- Moving averages and their crossovers provide potential trading signals.
- Scatter matrices give insights into the relationships and correlations between different stocks/indices.

## Getting Started:
1. Ensure all required libraries are installed.
2. Clone the repository and navigate to the project directory.
3. Run the Python script to fetch the data and perform the analysis.
4. Visualizations will be plotted in your default browser or Jupyter environment.

