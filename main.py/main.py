from agents.agent import IntradayAgent

def main():
    agent = IntradayAgent()
    result = agent.run()

    print("=== INTRADAY AI AGENT ===")
    print(result)

if __name__ == "__main__":
    main()
