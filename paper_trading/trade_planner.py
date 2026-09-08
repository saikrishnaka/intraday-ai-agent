class TradePlanner:

    def create_plan(self, stock, strategy):

        price = stock.get("price", 0)

        if price <= 0:
            return {
                "status": "REJECTED",
                "reason": "Invalid price"
            }

        direction = "LONG"

        if strategy == "trend_following":
            stop_loss = price * 0.98
            target = price * 1.04

        elif strategy == "breakout":
            stop_loss = price * 0.97
            target = price * 1.06

        elif strategy == "momentum":
            stop_loss = price * 0.98
            target = price * 1.05

        elif strategy == "mean_reversion":
            stop_loss = price * 0.99
            target = price * 1.02

        elif strategy == "vwap":
            stop_loss = price * 0.98
            target = price * 1.04

        else:
            stop_loss = price * 0.98
            target = price * 1.04

        risk = abs(price - stop_loss)
        reward = abs(target - price)

        risk_reward = reward / risk

        return {
            "status": "PAPER_ONLY",
            "symbol": stock.get("symbol"),
            "direction": direction,
            "strategy": strategy,
            "entry": round(price, 2),
            "stop_loss": round(stop_loss, 2),
            "target": round(target, 2),
            "risk_reward": round(risk_reward, 2)
        }


if __name__ == "__main__":
    planner = TradePlanner()

    sample_stock = {
        "symbol": "DEMO1",
        "price": 100
    }

    print(
        planner.create_plan(
            sample_stock,
            "trend_following"
        )
    )
