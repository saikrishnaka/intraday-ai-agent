class RiskEngine:

    def create_paper_trade_plan(self, symbol, entry, stop_loss, target):
        if entry <= 0 or stop_loss <= 0 or target <= 0:
            return {"status": "rejected", "reason": "Invalid price"}

        risk = abs(entry - stop_loss)
        reward = abs(target - entry)

        if risk == 0:
            return {"status": "rejected", "reason": "Stop-loss cannot equal entry"}

        risk_reward = reward / risk

        return {
            "status": "paper_trade_only",
            "symbol": symbol,
            "entry": entry,
            "stop_loss": stop_loss,
            "target": target,
            "risk_reward": round(risk_reward, 2)
        }


if __name__ == "__main__":
    engine = RiskEngine()

    plan = engine.create_paper_trade_plan(
        "DEMO",
        100,
        98,
        104
    )

    print(plan)
