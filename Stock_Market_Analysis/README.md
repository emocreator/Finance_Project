# S&P 500 Data Analysis

This project retrieves S&P 500 historical data and performs analysis using Python and Pandas.

## Data

- Uses yfinance to download S&P 500 (^GSPC) price data
- Covers period from 2019-01-01 to 2023-01-01
- Stores data in a Pandas DataFrame (df_history)

## Analysis

The project includes the following analysis on the S&P 500 data:

- Summary statistics
- Distribution of closing prices
- Calculating daily log returns
- Annualized volatility
- Histogram and stats on returns
- Checking for normality using scipy
- Regression on returns
- Rolling volatility
- Risk analysis (VaR, ES) 
- Correlation matrix and scatter plot
- Monte Carlo simulation
- Linear regression prediction
- Hypothesis testing

## Requirements

The main libraries used are:

- pandas 
- numpy
- yfinance
- statsmodels
- scipy
- sklearn

## Usage

The Jupyter notebook can be run to retrieve the data and replicate the analysis.

This covers a broad range of techniques for analyzing and modeling financial time series data using Python. The methods can be extended or modified for other data sets and use cases.