# Simple Black-Scholes European Option Pricing

This Python function implements the Black-Scholes formula to calculate the theoretical value of European call and put options.

## Parameters

- S0 - Current price of the underlying asset
- K - Strike price of the option
- r - Annualized risk-free interest rate  
- T - Time to maturity in years
- sigma - Volatility of the underlying asset 
- option_type - 'call' or 'put'

## Calculation

1. Calculate d1 and d2 using the Black-Scholes formulas:

```py
d1 = (log(S0/K) + (r + sigma^2/2)T) / (sigma*sqrt(T))
d2 = d1 - sigma*sqrt(T)
```

2. Calculate N(d1), N(d2), N(-d1) and N(-d2) using the normal cumulative distribution function

3. For a call option:  

```py
c = S0*N(d1) - Ke^(-rT)*N(d2)
```


4. For a put option:

```py
p = Ke^(-rT)*N(-d2) - S0*N(-d1)
```


5. Return the value c or p depending on the option_type parameter

6. To make the profit, the asset price at the option expiry should correspond the following rule:
```9 – 1.0298 – Price > 0, i.e., Price < 7.97```

## Usage

The function can price European call and put options. Pass the appropriate parameters and 'call' or 'put' for option_type.

The Black-Scholes formula provides a fast way to calculate the fair value of European options based on the underlying asset price, strike, volatility and time to maturity.
