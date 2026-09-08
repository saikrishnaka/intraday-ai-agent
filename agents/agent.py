from data.market_data import MarketData
from agents.market_analyzer import MarketAnalyzer
from agents.news_analyzer import NewsAnalyzer
from agents.strategy_selector import StrategySelector
from paper_trading.trade_planner import TradePlanner
from paper_trading.paper_engine import PaperTradingEngine


class IntradayAgent:

    def __init__(self):
        self.market_data = MarketData()
        self.market_analyzer = MarketAnalyzer()
        self.news_analyzer = NewsAnalyzer()
        self.strategy_selector = StrategySelector()
        self.trade_planner = TradePlanner()
        self.paper_engine = PaperTradingEngine()

    def run(self):
        market_data = self.market_data.get_sample_market_data()

        market_analysis = self.market_analyzer.analyze(
            market_data
        )

        selected_strategies = self.strategy_selector.select(
            market_analysis
        )

        trade_plans = []
        paper_trades = []

        for selected in selected_strategies:
            symbol = selected.get("symbol")
            strategy = selected.get("selected_strategy")

            stock = next(
                (
                    item
                    for item in market_data.get("stocks", [])
                    if item.get("symbol") == symbol
                ),
                None
            )

            if stock:
                plan = self.trade_planner.create_plan(
                    stock,
                    strategy
                )

                trade_plans.append(plan)

                if plan.get("status") == "PAPER_ONLY":
                    trade = self.paper_engine.create_trade(
                        plan["symbol"],
                        plan["direction"],
                        plan["entry"],
                        plan["stop_loss"],
                        plan["target"]
                    )

                    current_price = stock.get("price", plan["entry"])

                    updated_trade = self.paper_engine.update_trade(
                        trade,
                        current_price
                    )

                    paper_trades.append(updated_trade)

        return {
            "market": market_data,
            "analysis": market_analysis,
            "strategies": selected_strategies,
            "trade_plans": trade_plans,
            "paper_trades": paper_trades
        }


if __name__ == "__main__":
    agent = IntradayAgent()
    print(agent.run())
