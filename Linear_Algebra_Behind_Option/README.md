# Binomial Tree Call Option Pricing 

This Python code implements a binomial tree model to price a European call option.

## Parameters

- S0 - Current stock price
- K - Strike price  
- T - Time to maturity
- r - Risk-free interest rate
- sigma - Volatility of stock returns
- q - Dividend yield
- N - Number of steps in the tree

## Steps 

1. Calculate the up and down factors u and d, and risk-neutral probability p

```
u = exp(sigma * √Δt)
d = 1/u  
p = (exp((r-q)*Δt) - d)/(u-d) 
```

2. Create a matrix to store the option values at each node
3. Populate the final nodes with the payoff values 
4. Work backwards through the tree to calculate the option value at each node using risk-neutral pricing
5. Return the option value at the initial node (0,0)

## Explanation

The binomial tree model discretizes the evolution of the stock price over the option lifetime into N time steps. At each step, the price can move up by a factor of u or down by a factor of d. Risk-neutral valuation is used to determine the option value at each node.

The risk-neutral probabilities p and 1-p are calculated using the risk-free rate and the up/down factors. The option value matrix C is populated backwards starting from the final payoffs. At each node, the risk-neutral expectation is taken over the up and down nodes of the next step.

The initial call option value is returned from the matrix C at the initial node (0,0). 

The binomial tree provides a computationally simple yet robust way to price options, especially when closed-form solutions like Black-Scholes are not applicable.

## Visualisation

```
        C[0,3]      
    /           \
   /             \
C[0,2]           C[1,2]   
  /  \            /   \
 /    \          /     \  
C[0,1] C[1,1]  C[1,1] C[2,1]
 |      |        |      | 
C[0,0] C[1,0] C[1,0] C[2,0]

```

Where:

- C[i,j] represents the option value at node (i,j) 
- i indexes the time step
- j indexes the stock price (j-i = number of up moves)

This shows a 3-step binomial tree with 4 possible stock prices at each step. 

The option values are calculated starting from the final nodes C[ ,3] using the payoffs. Then working backwards to calculate C[ ,2], C[ ,1] and finally the initial option value C[0,0].

The stock price at each node is calculated as:

```
S[i,j] = S0 * u^(j-i) * d^i
```

Where S0 is the initial stock price.

This visualization shows how the binomial tree branches out from the initial node and allows pricing the option across all possible stock price paths.