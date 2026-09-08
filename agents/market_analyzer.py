class MarketAnalyzer:

    def analyze(self, market_data):
        results = []

        for stock in market_data.get("stocks", []):
            score = 0

            if stock.get("rsi", 50) > 55:
                score += 1

            if stock.get("vwap_position") == "above":
                score += 1

            if stock.get("momentum") == "positive":
                score += 1

            results.append({
                "symbol": stock.get("symbol"),
                "score": score,
                "market_regime": market_data.get("market_regime"),
                "trend": market_data.get("trend")
            })

        results.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return results


if __name__ == "__main__":
    analyzer = MarketAnalyzer()

    sample_data = {
        "market_regime": "TRENDING",
        "trend": "BULLISH",
        "stocks": [
            {
                "symbol": "DEMO1",
                "rsi": 62,
                "vwap_position": "above",
                "momentum": "positive"
            }
        ]
    }

    print(analyzer.analyze(sample_data))
