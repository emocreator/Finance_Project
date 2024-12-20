# Finance Project/Pricing Models

This project contains:

a) implementations and analysis of pricing models using Python.

b) implementations/analysis of the stock market using Python for data analysis.

## Folder Structure

There are 4 main folders:

**Black-Scholes**

Contains a Jupyter notebook [B_s.ipynb](https://github.com/emocreator/Finance_Project/blob/main/Black%20Scholes/B_S.ipynb) implementing the Black-Scholes formula for European option valuation.

**Linear_Algebra_Behind_Option** 

Contains a notebook [labo.ipynb](https://github.com/emocreator/Finance_Project/blob/main/Linear_Algebra_Behind_Option/labo.ipynb) explaining the linear algebra concepts behind options pricing.

**Stock_Market_Analysis**

Contains a notebook [SMA.ipynb](https://github.com/emocreator/Finance_Project/blob/main/Stock_Market_Analysis/SMA.ipynb) retrieving  historical data and performs analysis using Python and Pandas.

**Simple Moving average**

Contains a notebook [SMA.ipynb](https://github.com/emocreator/Finance_Project/blob/main/SMA(SimpleMovingAverage)/SMA.ipynb) retrieving  historical data and performs analysis using Python and Pandas.

## Models

The project covers two key option pricing models:

**Black-Scholes Formula**

- Closed-form solution for European options
- Implemented in B_s.ipynb
- Requires underlying price, volatility, interest rates, time to maturity
- Provides quick and efficient pricing

**Binomial Tree** 

- Discretized numerical model 
- Allows early exercise valuation
- Implemented in labo.ipynb
- Intuitively represents different price paths
- Computationally more intensive than Black-Scholes

## Usage

The models can be used to price European and American options. The notebooks contain examples of calculating prices under different market conditions.

The linear algebra notebook also explains how matrix operations can derive the risk-neutral pricing used in these models.

These notebooks provide an introduction to implementing and understanding key option pricing techniques in Python.

## Author

- [Gudfit](https://github.com/emocreator)
