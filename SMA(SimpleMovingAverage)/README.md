# Trading Strategy Using Moving Averages

This Python script implements a simple trading strategy using moving averages. It includes two different examples of trading strategies: one using Yahoo Finance data for a specific stock (e.g., AAPL), and another using synthetic data with various technical indicators.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Description](#description)

## Requirements

Before running the code, make sure you have the following Python packages installed:

- `datetime`
- `matplotlib`
- `yfinance`
- `enum`
- `pandas`
- `numpy`
- `talib`

You can install these packages using `pip`:

```bash
pip install datetime matplotlib yfinance pandas numpy TA-Lib
```

## Usage

### Moving Average Crossover Strategy (Yahoo Finance Data)

1. Import the necessary libraries:

   ```python
   import datetime as dt
   import matplotlib.pyplot as plt 
   import yfinance as yf
   from enum import Enum
   ```

2. Define the moving average periods (`ma_1` and `ma_2`), start and end dates, and stock ticker symbol.

3. Download historical stock data using Yahoo Finance:

   ```python
   data = yf.download(stock_ticker, start, end)
   ```

4. Calculate and plot the moving averages and buy/sell signals:

   ```python
   # Calculate moving averages and generate buy/sell signals
   # Plot the results
   plt.plot(data['Adj Close'], label="Share Price", alpha=0.5)
   # ...
   plt.show()
   ```

### Synthetic Trading Strategy (Synthetic Data)

1. Import the necessary libraries:

   ```python
   import pandas as pd
   import numpy as np
   import talib
   ```

2. Define the synthetic data (e.g., Close prices) and strategy parameters (short window, long window, stop loss).

3. Calculate technical indicators such as SMA (Simple Moving Average) and RSI (Relative Strength Index).

4. Generate buy/sell signals with stop-loss logic and plot the results:

   ```python
   # Generate signals and apply stop-loss logic
   # Plot the results
   plt.plot(data['Close'], label='Close')
   # ...
   plt.legend()
   plt.show()
   ```

## Description

- The code provides examples of two different trading strategies: one based on real stock data from Yahoo Finance and another using synthetic data with technical indicators.

- The Yahoo Finance strategy uses moving average crossovers to generate buy and sell signals for a specific stock.

- The synthetic data strategy calculates Simple Moving Averages (SMA) and the Relative Strength Index (RSI) to generate buy and sell signals with a stop-loss mechanism.

- The code includes comments and explanations for each part of the code to help you understand how the strategies work.
