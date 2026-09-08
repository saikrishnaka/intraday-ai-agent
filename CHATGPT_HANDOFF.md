# CHATGPT HANDOFF — INTRADAY AI AGENT

## IMPORTANT
This document is a handoff from a previous ChatGPT conversation.
Read this entire file before making changes.

Continue the existing project from its current state.
Do NOT restart the project from scratch.

The project is for EDUCATIONAL PAPER TRADING / SIMULATION ONLY.
Do NOT connect to a broker, place real orders, or use real money.

---

# 1. PROJECT

Repository:
saikrishnaka/intraday-ai-agent

Project name:
Intraday AI Agent

Goal:
Build an AI-powered intraday market research and paper-trading simulation system.

Long-term concept:
The agent should analyze market conditions, news, indicators and multiple trading strategies, select suitable strategies according to the current market regime, rank simulated candidates, create simulated trade plans with stop-loss and target, and evaluate simulated trades.

Current market metadata:
NSE / NIFTY

Current simulated stocks:
DEMO1
DEMO2

---

# 2. CURRENT ARCHITECTURE

Current pipeline:

Market Data
    ↓
Regime Detection
    ↓
Market Analysis
    ↓
Strategy Selection
    ↓
Decision Engine
    ↓
Confidence Engine
    ↓
Ranking Engine
    ↓
Trade Planner
    ↓
Paper Trading Engine

News Analyzer exists but is not yet fully integrated into the final ranking pipeline.

---

# 3. CURRENT FILE STRUCTURE

config/settings.json
ontology/README.md
ontology/market_ontology.json

strategies/strategy_engine.py

risk/risk_engine.py

data/__init__.py
data/market_data.py

agents/market_analyzer.py
agents/news_analyzer.py
agents/strategy_selector.py
agents/decision_engine.py
agents/regime_detector.py
agents/confidence_engine.py
agents/ranking_engine.py
agents/agent.py

paper_trading/paper_engine.py
paper_trading/trade_planner.py

main.py

---

# 4. COMPLETED COMPONENTS

## MarketData

data/market_data.py

Provides sample simulated NSE/NIFTY market data.

DEMO1:
price = 100.0
volume = 150000
RSI = 62
VWAP position = above
momentum = positive

DEMO2:
price = 200.0
volume = 90000
RSI = 48
VWAP position = below
momentum = weak

---

## MarketAnalyzer

agents/market_analyzer.py

Analyzes each simulated stock using:
- RSI
- VWAP position
- momentum

Produces a score and market regime/trend information.

---

## NewsAnalyzer

agents/news_analyzer.py

Basic keyword-based news sentiment analyzer.

Positive keywords include:
profit
growth
order
approval
upgrade
expansion

Negative keywords include:
loss
fraud
downgrade
penalty
decline
investigation

Outputs:
- headline
- symbol
- sentiment
- impact_score

It has been tested successfully.

Important:
NewsAnalyzer currently exists but actual sample news is not yet integrated into the main final ranking flow.

---

## StrategyEngine

strategies/strategy_engine.py

Available strategies currently include:

trend_following
breakout
momentum
mean_reversion
vwap
support_resistance

---

## StrategySelector

agents/strategy_selector.py

Uses market regime and trend to select a strategy.

TRENDING + BULLISH:
trend_following

TRENDING:
breakout

RANGING:
mean_reversion

Other:
momentum

---

## DecisionEngine

agents/decision_engine.py

Scores strategies using:
- RSI
- momentum
- VWAP

Current strategies scored:
trend_following
breakout
momentum
mean_reversion
vwap

The highest score is selected.

---

## RegimeDetector

agents/regime_detector.py

Detects:

HIGH_VOLATILITY
TRENDING
RANGING

based on:
- trend
- volatility

Current sample:
trend = BULLISH
volatility = MEDIUM

Therefore:
market_regime = TRENDING

---

## ConfidenceEngine

agents/confidence_engine.py

Calculates confidence using:
- RSI
- VWAP
- momentum
- market regime
- decision score

Confidence levels:
HIGH
MEDIUM
LOW

DEMO1 currently gets a high confidence score with the sample data.

---

## RankingEngine

agents/ranking_engine.py

Combines:
- strategy score
- confidence score

Formula:

total_score = strategy_score * 20 + confidence_score

Then sorts descending and assigns:
rank = 1, 2, 3...

---

## TradePlanner

paper_trading/trade_planner.py

Creates simulated trade plans.

Supports:
trend_following
breakout
momentum
mean_reversion
vwap

Creates:
- symbol
- direction
- entry
- stop_loss
- target
- risk_reward

Status:
PAPER_ONLY

---

## RiskEngine

risk/risk_engine.py

Calculates simulated risk/reward.

Rejects invalid prices and zero-risk trades.

Status:
paper_trade_only

---

## PaperTradingEngine

paper_trading/paper_engine.py

Creates simulated trades.

Status:
PAPER

Can update simulated trades based on current price.

For LONG:
current price <= stop_loss → STOP_LOSS
current price >= target → TARGET

For SHORT:
current price >= stop_loss → STOP_LOSS
current price <= target → TARGET

It has been tested successfully for target and stop-loss behavior.

---

# 5. INTEGRATED AGENT

agents/agent.py

IntradayAgent currently initializes:

MarketData
MarketAnalyzer
NewsAnalyzer
StrategySelector
DecisionEngine
RegimeDetector
ConfidenceEngine
RankingEngine
TradePlanner
PaperTradingEngine

The run() method currently:

1. Gets sample market data.
2. Detects market regime.
3. Updates market data regime.
4. Performs market analysis.
5. Selects strategies.
6. Runs DecisionEngine for each stock.
7. Calculates confidence.
8. Creates simulated trade plans.
9. Creates simulated paper trades.
10. Updates paper trades using current simulated price.
11. Creates rankings.
12. Returns the complete result.

---

# 6. CURRENT RANKING ISSUE

The agent runs successfully.

The user reported seeing:
rank = 2

This is NOT automatically an error.

With the current sample data, expected behavior is approximately:

DEMO1:
- RSI 62
- VWAP above
- momentum positive
- TRENDING/BULLISH
- strong strategy score
- high confidence
- should normally be Rank 1

DEMO2:
- RSI 48
- VWAP below
- weak momentum
- lower confidence
- should normally be Rank 2

Before changing any code, inspect the actual output.

Command:

python main.py | tail -30

Check which symbol has rank 2.

If DEMO2 has rank 2:
ranking is behaving as expected.

If DEMO1 has rank 2:
inspect RankingEngine and decision/confidence results before modifying anything.

---

# 7. TESTS ALREADY COMPLETED

Market data:
PASS

Market analyzer:
PASS

News analyzer:
PASS

Strategy engine:
PASS

Decision engine:
PASS

Regime detector:
PASS

Confidence engine:
PASS

Ranking engine:
PASS

Risk engine:
PASS

Trade planner:
PASS

Paper trading target:
PASS

Paper trading stop-loss:
PASS

Full:
python main.py
PASS

---

# 8. CURRENT DEVELOPMENT STYLE

The user prefers:
- Telugu explanations
- English technical terms/code
- one step at a time
- exact terminal commands
- simple instructions
- after completing a step, continue to the next step

Avoid giving many terminal commands at once unless necessary.

---

# 9. NEXT DEVELOPMENT ROADMAP

After confirming the ranking output:

Phase 1:
Fix/confirm ranking behavior.

Phase 2:
Integrate NewsAnalyzer into the main agent.

Phase 3:
Improve multi-strategy scoring.

Phase 4:
Make strategy selection market-regime aware.

Phase 5:
Improve confidence scoring.

Phase 6:
Create better simulated entry / stop-loss / target logic.

Phase 7:
Add backtesting using historical/sample datasets.

Phase 8:
Add simulated portfolio tracking.

Phase 9:
Add performance metrics such as:
- win rate
- simulated P&L
- drawdown
- risk/reward statistics
- strategy performance

Phase 10:
Create a daily simulated market research report.

---

# 10. SAFETY / PROJECT BOUNDARY

This is a paper-trading educational project.

Keep all current examples simulated.

Do NOT:
- connect to a real brokerage
- place real orders
- automate real-money trading
- request or store broker passwords
- request OTPs
- request API keys or secrets

Future automation should remain simulation-only.

---

# 11. HOW TO CONTINUE THIS PROJECT

When opening this project in a new ChatGPT account:

1. Upload this CHATGPT_HANDOFF.md file.
2. The GitHub repository contains the actual project code.
3. Tell ChatGPT:

"Read CHATGPT_HANDOFF.md completely and continue the Intraday AI Agent project from the exact current state. Do not restart from scratch. The immediate task is to inspect the ranking output and determine why rank 2 is appearing."

Then provide terminal output/screenshots when requested.

---

# 12. FIRST TASK AFTER HANDOFF

Run:

python main.py | tail -30

Then inspect the ranking section.

Do not rewrite the architecture until the actual output is confirmed.

END OF HANDOFF
