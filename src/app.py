from src.agents.intake_agent import IntakeAgent
from src.agents.classifier_agent import ClassifierAgent
from src.agents.analyzer_agent import AnalyzerAgent
from src.agents.task_agent import TaskAgent
from src.agents.support_agent import SupportAgent
from src.agents.action_agent import ActionAgent
from src.agents.logger_agent import LoggerAgent



class AbboAgentsAI:
    def __init__(self):
        self.intake = IntakeAgent()
        self.classifier = ClassifierAgent()
        self.analyzer = AnalyzerAgent()
        self.task_agent = TaskAgent()
        self.support_agent = SupportAgent()
        self.action_agent = ActionAgent()
        self.logger = LoggerAgent()

    def run(self, message):
        intake_output = self.intake.run(message)
        type_msg = self.classifier.run(message)
        summary = self.analyzer.run(message)

        print("Message Type:", type_msg)

        if type_msg == "task":
            result = self.task_agent.run(summary)
        elif type_msg == "support":
            result = self.support_agent.run(summary)
        else:
            result = f"Email Summary:\n{summary}"

        final = self.action_agent.run(result)
        self.logger.save("last_output", final)

        return final


if __name__ == "__main__":
    agent = AbboAgentsAI()
    test_msg = "Hello, our payment system is down and customers are complaining."
    print(agent.run(test_msg))
