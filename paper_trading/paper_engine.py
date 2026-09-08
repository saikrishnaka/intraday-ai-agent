class PaperTradingEngine:

    def create_trade(self, symbol, direction, entry, stop_loss, target):
        return {
            "symbol": symbol,
            "direction": direction,
            "entry": entry,
            "stop_loss": stop_loss,
            "target": target,
            "status": "OPEN",
            "mode": "PAPER"
        }

    def update_trade(self, trade, current_price):
        if trade["direction"] == "LONG":
            if current_price <= trade["stop_loss"]:
                trade["status"] = "STOP_LOSS"
            elif current_price >= trade["target"]:
                trade["status"] = "TARGET"

        elif trade["direction"] == "SHORT":
            if current_price >= trade["stop_loss"]:
                trade["status"] = "STOP_LOSS"
            elif current_price <= trade["target"]:
                trade["status"] = "TARGET"

        return trade


if __name__ == "__main__":
    engine = PaperTradingEngine()

    trade = engine.create_trade(
        "DEMO1",
        "LONG",
        100,
        98,
        104
    )

    print(engine.update_trade(trade, 102))
