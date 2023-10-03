import sys
import datetime
import numpy as np

class Bot:
    def __init__(self):
        self.botState = BotState()
        self.max_sell_amount = 0
        self.bought_at = 0
        self.wait_buy = 0
        self.bollinger_period = 20  # Number of periods to consider for Bollinger Bands
        self.bollinger_std_dev = 2  # Number of standard deviations for Bollinger Bands

    def run(self):
        while True:
            reading = input()
            if len(reading) == 0:
                continue
            self.parse(reading)

    def parse(self, info: str):
        tmp = info.split(" ")
        if tmp[0] == "settings":
            self.botState.update_settings(tmp[1], tmp[2])
        if tmp[0] == "update":
            if tmp[1] == "game":
                self.botState.update_game(tmp[2], tmp[3])
        if tmp[0] == "action":
            if self.wait_buy > 0:       # Wait before two buy action
                self.wait_buy = self.wait_buy - 1
            timestamp = self.botState.date      # Get date
            date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            dollars = self.botState.stacks["USDT"]      # Current money
            current_closing_price = self.botState.charts["USDT_BTC"].closes[-1]     # Current closing price
            affordable = dollars / current_closing_price        # Current affordable stock
            risk = 0.3      # Risk strategy. It buys affordable * risk
            upper_band, lower_band = self.calculate_bollinger_bands()
            if upper_band is None or lower_band is None:
                print("no_moves", flush=True)
                return # Bollinger bands calcul
            print(f'Date: {date} | Dollars: {dollars} | Affordable: {affordable}', file=sys.stderr)

            if self.is_bearish_engulfing_pattern() and self.is_overbought(70):
                self.sell(1, date)
            elif current_closing_price > upper_band:
                self.sell(1, date)
            elif dollars < 50:
                print("no_moves", flush=True)
            elif current_closing_price < lower_band:
                self.buy(affordable * risk, date, 0)
            # elif self.is_oversold(40):
            #     self.buy(affordable * risk, date, 0)
            else:
                print("no_moves", flush=True)
    
    def buy(self, affordable, date, wb):
        if self.wait_buy == 0:
            if affordable > 0:
                print(f'buy USDT_BTC {affordable}', flush=True)
                print(f'Buy! For : {affordable} | Date: {date}', file=sys.stderr)
                self.max_sell_amount = self.max_sell_amount + (affordable) * (1 - (self.botState.transactionFee / 100))
                self.wait_buy = wb
            else:
                print("no_moves", flush=True)
        else:
            print("no_moves", flush=True)
    
    def sell(self, risk, date):
        if self.max_sell_amount > 0:
            print(f'sell USDT_BTC {self.max_sell_amount * risk}', flush=True)
            print(f'Sell! For : {self.max_sell_amount * risk} | Date: {date}', file=sys.stderr)
            self.max_sell_amount = self.max_sell_amount - (self.max_sell_amount * risk)

        else:
            print("no_moves", flush=True)

    def is_bearish_engulfing_pattern(self):
        # Check if current candle is red
        if len(self.botState.charts["USDT_BTC"].closes) < 2:
            return False
       # Check if current candle is red
        if self.botState.charts["USDT_BTC"].closes[-1] < self.botState.charts["USDT_BTC"].opens[-1]:
            # Check if previous candle was green
            if self.botState.charts["USDT_BTC"].closes[-2] > self.botState.charts["USDT_BTC"].opens[-2]:
                # Check if current candle engulfs previous
                if (self.botState.charts["USDT_BTC"].opens[-2] > self.botState.charts["USDT_BTC"].closes[-1] and 
                    self.botState.charts["USDT_BTC"].closes[-2] < self.botState.charts["USDT_BTC"].opens[-1]):
                    return True    
        return False
    
    def is_bullish_engulfing_pattern(self):
        # Check if current candle is green
        if self.botState.charts["USDT_BTC"].closes[-1] > self.botState.charts["USDT_BTC"].opens[-1]:
            # Check if previous candle was red
            if self.botState.charts["USDT_BTC"].closes[-2] < self.botState.charts["USDT_BTC"].opens[-2]:
                # Check if current candle engulf previous
                if self.botState.charts["USDT_BTC"].opens[-2] < self.botState.charts["USDT_BTC"].closes[-1] and self.botState.charts["USDT_BTC"].closes[-2] > self.botState.charts["USDT_BTC"].opens[-1]:
                    return True
        
        return False
    
    def is_oversold(self, rsi_check):
        closing_prices = self.botState.charts["USDT_BTC"].closes
        if len(closing_prices) >= 14:
            prices = closing_prices[-14:]
            gains = []
            losses = []
            for i in range(1, len(prices)):
                diff = prices[i] - prices[i - 1]
                if diff >= 0:
                    gains.append(diff)
                    losses.append(0)
                else:
                    gains.append(0)
                    losses.append(abs(diff))
            avg_gain = sum(gains) / 14
            avg_loss = sum(losses) / 14
            if avg_loss > 0:
                rs = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + rs))
                if rsi <= rsi_check:
                    return True
        
        return False
    
    def is_overbought(self, rsi_check):
        closing_prices = self.botState.charts["USDT_BTC"].closes
        if len(closing_prices) >= 14:
            prices = closing_prices[-14:]
            gains = []
            losses = []
            for i in range(1, len(prices)):
                diff = prices[i] - prices[i - 1]
                if diff >= 0:
                    gains.append(diff)
                    losses.append(0)
                else:
                    gains.append(0)
                    losses.append(abs(diff))
            avg_gain = sum(gains) / 14
            avg_loss = sum(losses) / 14
            if avg_loss > 0:
                rs = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + rs))
                if rsi >= rsi_check:
                    return True
        
        return False

    def calculate_bollinger_bands(self):
        closing_prices = self.botState.charts["USDT_BTC"].closes
        if len(closing_prices) >= self.bollinger_period:
            prices = closing_prices[-self.bollinger_period:]
            sma = np.mean(prices)  # Calculate the Simple Moving Average (SMA)
            std_dev = np.std(prices)  # Calculate the standard deviation
            upper_band = sma + (self.bollinger_std_dev * std_dev)  # Calculate the upper Bollinger Band
            lower_band = sma - (self.bollinger_std_dev * std_dev)  # Calculate the lower Bollinger Band
            return upper_band, lower_band
        else:
            return None, None

class Candle:
    def __init__(self, format, intel):
        tmp = intel.split(",")
        for (i, key) in enumerate(format):
            value = tmp[i]
            if key == "pair":
                self.pair = value
            if key == "date":
                self.date = int(value)
            if key == "high":
                self.high = float(value)
            if key == "low":
                self.low = float(value)
            if key == "open":
                self.open = float(value)
            if key == "close":
                self.close = float(value)
            if key == "volume":
                self.volume = float(value)

    def __repr__(self):
        return str(self.pair) + str(self.date) + str(self.close) + str(self.volume)


class Chart:
    def __init__(self):
        self.dates = []
        self.opens = []
        self.highs = []
        self.lows = []
        self.closes = []
        self.volumes = []
        self.indicators = {}

    def add_candle(self, candle: Candle):
        self.dates.append(candle.date)
        self.opens.append(candle.open)
        self.highs.append(candle.high)
        self.lows.append(candle.low)
        self.closes.append(candle.close)
        self.volumes.append(candle.volume)


class BotState:
    def __init__(self):
        self.timeBank = 0
        self.maxTimeBank = 0
        self.timePerMove = 1
        self.candleInterval = 1
        self.candleFormat = []
        self.candlesTotal = 0
        self.candlesGiven = 0
        self.initialStack = 0
        self.transactionFee = 0.1
        self.date = 0
        self.stacks = dict()
        self.charts = dict()

    def update_chart(self, pair: str, new_candle_str: str):
        if not (pair in self.charts):
            self.charts[pair] = Chart()
        new_candle_obj = Candle(self.candleFormat, new_candle_str)
        self.charts[pair].add_candle(new_candle_obj)

    def update_stack(self, key: str, value: float):
        self.stacks[key] = value

    def update_settings(self, key: str, value: str):
        if key == "timebank":
            self.maxTimeBank = int(value)
            self.timeBank = int(value)
        if key == "time_per_move":
            self.timePerMove = int(value)
        if key == "candle_interval":
            self.candleInterval = int(value)
        if key == "candle_format":
            self.candleFormat = value.split(",")
        if key == "candles_total":
            self.candlesTotal = int(value)
        if key == "candles_given":
            self.candlesGiven = int(value)
        if key == "initial_stack":
            self.initialStack = int(value)
        if key == "transaction_fee_percent":
            self.transactionFee = float(value)

    def update_game(self, key: str, value: str):
        if key == "next_candles":
            new_candles = value.split(";")
            self.date = int(new_candles[0].split(",")[1])
            for candle_str in new_candles:
                candle_infos = candle_str.strip().split(",")
                self.update_chart(candle_infos[0], candle_str)
        if key == "stacks":
            new_stacks = value.split(",")
            for stack_str in new_stacks:
                stack_infos = stack_str.strip().split(":")
                self.update_stack(stack_infos[0], float(stack_infos[1]))


if __name__ == "__main__":
    mybot = Bot()
    mybot.run()
