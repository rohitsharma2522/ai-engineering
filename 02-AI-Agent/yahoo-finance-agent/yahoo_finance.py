import yfinance as yf
from pydantic import BaseModel, Field

class StockPriceResult(BaseModel):
    """Model to represent the stock price result"""
    ticker: str = Field(..., description="The stock symbol")
    price: float = Field(..., description="The current stock price")
    currency: str = Field(..., description="The currency of the stock price")

class StockPriceError(BaseModel):
    """Model to represent an error in retrieving stock price"""
    ticker: str = Field(..., description="The stock symbol")
    error: str = Field(..., description="Error message if the stock price could not be retrieved")


def get_stock_price(ticker_symbol: str) -> str:
    """
    Fetches the current stock price for the given ticker symbol using Yahoo Finance API.

    Args:
        ticker_symbol (str): The stock symbol to fetch the price for.

    Returns:
        str: JSON string containing either the stock price result or an error message.
    """
    try:
        # Fetch stock data from Yahoo Finance
        stock_data = yf.Ticker(ticker_symbol).fast_info
        
        # Create a StockPriceResult object
        result = StockPriceResult(
            ticker=ticker_symbol,
            price=stock_data["last_price"],
            currency=stock_data["currency"]
        )
        
        # Return the result as a JSON string
        return result.model_dump_json()
    except Exception as e:
        # Create a StockPriceError object in case of an error
        error_result = StockPriceError(
            ticker=ticker_symbol,
            error=str(e)
        )
        return error_result.model_dump_json()

if __name__ == "__main__":
        # Example usage
        ticker = "AAPL"
        print(get_stock_price(ticker))