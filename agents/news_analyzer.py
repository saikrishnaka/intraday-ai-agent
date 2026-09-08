class NewsAnalyzer:

    def analyze(self, news_items):
        results = []

        positive_words = [
            "profit",
            "growth",
            "order",
            "approval",
            "upgrade",
            "expansion"
        ]

        negative_words = [
            "loss",
            "fraud",
            "downgrade",
            "penalty",
            "decline",
            "investigation"
        ]

        for news in news_items:
            headline = news.get("headline", "").lower()

            positive_score = sum(
                word in headline for word in positive_words
            )

            negative_score = sum(
                word in headline for word in negative_words
            )

            if positive_score > negative_score:
                sentiment = "POSITIVE"
            elif negative_score > positive_score:
                sentiment = "NEGATIVE"
            else:
                sentiment = "NEUTRAL"

            results.append({
                "headline": news.get("headline"),
                "symbol": news.get("symbol"),
                "sentiment": sentiment,
                "impact_score": positive_score - negative_score
            })

        return results


if __name__ == "__main__":
    analyzer = NewsAnalyzer()

    sample_news = [
        {
            "symbol": "DEMO1",
            "headline": "Company reports strong profit growth"
        }
    ]

    print(analyzer.analyze(sample_news))
