# README

## Introduction

This code is a trading bot specifically built to analyze candlestick data for the USDT_BTC trading pair and make decisions to buy or sell based on certain trading strategies.

### Dependencies

The bot uses the following libraries:

- `sys`
- `datetime`
- `numpy`

### Structure

The program is divided into three main classes:

1. **Bot**: This is the main trading bot class. It processes inputs, updates its internal state, and decides on trading actions. The primary trading strategies are based on Bollinger Bands, Relative Strength Index (RSI), and the Bearish Engulfing pattern.
2. **Candle**: Represents a single candlestick data. It captures details like the date, open, close, high, low, and volume for a particular time period.
3. **Chart**: Keeps track of a series of candlestick data.
4. **BotState**: Maintains the state of the bot. It includes settings, current stack values, and candlestick charts.

### How to Use

When you run the bot, it waits for inputs. The inputs should be formatted strings representing the current state of the market or the bot settings. Based on this input, the bot will decide on an action (buy, sell, or no move) and print the action to the stdout.

The input can be in the format of:

- **settings**: Updates settings of the bot. For example: "settings timebank 10000".
- **update**: Updates the bot's state with new game data or candle data.
- **action**: A prompt for the bot to decide on an action.

### Trading Strategies

The bot uses a combination of the following trading strategies:

1. **Bollinger Bands**: It sells if the current closing price is above the upper Bollinger Band and buys if it is below the lower Bollinger Band.
2. **Bearish Engulfing Pattern**: If the bot identifies a bearish engulfing pattern and the market is overbought (based on RSI), it sells.
3. **Risk Strategy**: The bot uses a risk factor to determine the amount to buy or sell.
4. **Relative Strength Index (RSI)**: The bot uses RSI to determine if the market is overbought or oversold.

### Notes

- The bot also has a wait mechanism (`wait_buy`) to prevent buying too frequently.
- There are debug print statements that print to stderr for easier debugging. These can be removed in a production environment.
- The bot currently focuses on the USDT_BTC trading pair, but can be easily extended to other pairs.

### Future Enhancements

- Implement additional trading strategies for better accuracy.
- Add more error handling and input validation.
- Optimize the bot for better performance.
- Extend the bot to handle multiple trading pairs.

---

**Disclaimer**: The bot is designed for educational purposes and should not be used in real-world trading without extensive testing and modifications. Trading cryptocurrencies is risky, and you should consult with a financial advisor before making any trading decisions.