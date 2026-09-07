class StrategySelector:

    def select(self, market_analysis):
        selected = []

        for stock in market_analysis:
            regime = stock.get("market_regime")
            trend = stock.get("trend")
            score = stock.get("score", 0)

            if regime == "TRENDING" and trend == "BULLISH":
                strategy = "trend_following"

            elif regime == "TRENDING":
                strategy = "breakout"

            elif regime == "RANGING":
                strategy = "mean_reversion"

            else:
                strategy = "momentum"

            selected.append({
                "symbol": stock.get("symbol"),
                "score": score,
                "selected_strategy": strategy
            })

        return selected


if __name__ == "__main__":
    selector = StrategySelector()

    sample_analysis = [
        {
            "symbol": "DEMO1",
            "score": 3,
            "market_regime": "TRENDING",
            "trend": "BULLISH"
        }
    ]

    print(selector.select(sample_analysis))
