import yfinance as yf
import ta
from datetime import date

def get_bollinger_bands(symbol, end_date=None):
    """
    Calculate Bollinger Bands for a given symbol.

    Args:
        symbol (str): Ticker symbol of the stock.
        end_date (str, optional): End date for the historical price data. Defaults to None.

    Returns:
        str: Formatted string containing the current price and Bollinger Bands.
    """
    stock_data = yf.download(symbol, end=end_date, progress=False)
    indicator_bb = ta.volatility.BollingerBands(stock_data['Close'])
    current_price = stock_data['Close'].iloc[-1]
    bb_high = indicator_bb.bollinger_hband().iloc[-1]
    bb_mid = indicator_bb.bollinger_mavg().iloc[-1]
    bb_low = indicator_bb.bollinger_lband().iloc[-1]

    current_price = round(current_price, 2)
    bb_high = round(bb_high, 2)
    bb_low = round(bb_low, 2)
    bb_mid = round(bb_mid, 2)
    output = f"(Price: {current_price}), BB: ({bb_high}), ({bb_mid}), ({bb_low})"
    return output
