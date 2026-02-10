class AutonomousAgent:
    """
    A class to represent an autonomous agent capable of performing specific tasks with minimal human intervention.
    """

    def __init__(self, name: str, capabilities: list[str]):
        """
        Initialize the autonomous agent with a name and a list of capabilities.

        :param name: The name of the agent.
        :param capabilities: A list of tasks the agent can perform.
        """
        self.name = name
        self.capabilities = capabilities

    def perform_task(self, task: str) -> bool:
        """
        Perform a task if it is within the agent's capabilities.

        :param task: The task to be performed.
        :return: True if the task was performed, False otherwise.
        """
        if task in self.capabilities:
            print(f"{self.name} is performing the task: {task}")
            return True
        else:
            print(f"{self.name} cannot perform the task: {task}")
            return False

    def add_capability(self, capability: str) -> None:
        """
        Add a new capability to the agent.

        :param capability: The new capability to be added.
        """
        if capability not in self.capabilities:
            self.capabilities.append(capability)
            print(f"Added capability: {capability} to {self.name}")
        else:
            print(f"{self.name} already has the capability: {capability}")

    def list_capabilities(self) -> list[str]:
        """
        List all capabilities of the agent.

        :return: A list of capabilities.
        """
        return self.capabilities


def main():
    """
    Main function to demonstrate the use of the AutonomousAgent class.
    """
    agent = AutonomousAgent(name="Agent007", capabilities=["data analysis", "report generation"])
    agent.perform_task("data analysis")
    agent.perform_task("image recognition")
    agent.add_capability("image recognition")
    agent.perform_task("image recognition")
    print(f"Capabilities of {agent.name}: {agent.list_capabilities()}")


if __name__ == "__main__":
    main()