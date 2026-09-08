class MarketData:
    def get_sample_market_data(self):
        return {
            "market": "NSE",
            "index": "NIFTY",
            "market_regime": "TRENDING",
            "trend": "BULLISH",
            "volatility": "MEDIUM",
            "stocks": [
                {
                    "symbol": "DEMO1",
                    "price": 100.0,
                    "volume": 150000,
                    "rsi": 62,
                    "vwap_position": "above",
                    "momentum": "positive"
                },
                {
                    "symbol": "DEMO2",
                    "price": 200.0,
                    "volume": 90000,
                    "rsi": 48,
                    "vwap_position": "below",
                    "momentum": "weak"
                }
            ]
        }

if __name__ == "__main__":
    data = MarketData()
    print(data.get_sample_market_data())
