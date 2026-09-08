class DecisionEngine:

    def decide(self, stock):
        scores = {}

        rsi = stock.get("rsi", 50)
        vwap = stock.get("vwap_position")
        momentum = stock.get("momentum")

        scores["trend_following"] = 0
        scores["breakout"] = 0
        scores["momentum"] = 0
        scores["mean_reversion"] = 0
        scores["vwap"] = 0

        if rsi > 55:
            scores["trend_following"] += 1
            scores["momentum"] += 1

        if momentum == "positive":
            scores["momentum"] += 2
            scores["trend_following"] += 1

        if vwap == "above":
            scores["vwap"] += 2
            scores["trend_following"] += 1

        if rsi < 35:
            scores["mean_reversion"] += 2

        best_strategy = max(scores, key=scores.get)
        best_score = scores[best_strategy]

        return {
            "symbol": stock.get("symbol"),
            "best_strategy": best_strategy,
            "score": best_score,
            "all_scores": scores
        }


if __name__ == "__main__":
    engine = DecisionEngine()

    sample_stock = {
        "symbol": "DEMO1",
        "rsi": 62,
        "vwap_position": "above",
        "momentum": "positive"
    }

    print(engine.decide(sample_stock))
