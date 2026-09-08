from data.market_data import MarketData
from agents.market_analyzer import MarketAnalyzer
from agents.news_analyzer import NewsAnalyzer
from agents.strategy_selector import StrategySelector


class IntradayAgent:

    def __init__(self):
        self.market_data = MarketData()
        self.market_analyzer = MarketAnalyzer()
        self.news_analyzer = NewsAnalyzer()
        self.strategy_selector = StrategySelector()

    def run(self):
        market_data = self.market_data.get_sample_market_data()

        market_analysis = self.market_analyzer.analyze(
            market_data
        )

        selected_strategies = self.strategy_selector.select(
            market_analysis
        )

        return {
            "market": market_data,
            "analysis": market_analysis,
            "strategies": selected_strategies
        }


if __name__ == "__main__":
    agent = IntradayAgent()

    result = agent.run()

    print(result)
