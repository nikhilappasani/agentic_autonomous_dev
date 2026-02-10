class AutonomousAgent:
    """
    A class to represent an autonomous agent capable of performing specific tasks with minimal human intervention.
    """

    def __init__(self, name: str, capabilities: list[str]) -> None:
        """
        Initialize the autonomous agent with a name and a list of capabilities.

        :param name: The name of the agent.
        :param capabilities: A list of capabilities the agent possesses.
        """
        self.name = name
        self.capabilities = capabilities

    def perform_task(self, task: str) -> str:
        """
        Perform a task if it is within the agent's capabilities.

        :param task: The task to be performed.
        :return: A message indicating the result of the task attempt.
        """
        if task in self.capabilities:
            return f"{self.name} is performing the task: {task}."
        else:
            return f"{self.name} cannot perform the task: {task}."

    def add_capability(self, capability: str) -> None:
        """
        Add a new capability to the agent.

        :param capability: The capability to be added.
        """
        if capability not in self.capabilities:
            self.capabilities.append(capability)

    def remove_capability(self, capability: str) -> None:
        """
        Remove a capability from the agent.

        :param capability: The capability to be removed.
        """
        if capability in self.capabilities:
            self.capabilities.remove(capability)

    def list_capabilities(self) -> list[str]:
        """
        List all capabilities of the agent.

        :return: A list of the agent's capabilities.
        """
        return self.capabilities


def main() -> None:
    """
    Main function to demonstrate the use of the AutonomousAgent class.
    """
    agent = AutonomousAgent(name="Agent001", capabilities=["navigate", "analyze data", "report"])
    
    print(agent.perform_task("navigate"))
    print(agent.perform_task("cook"))

    agent.add_capability("cook")
    print(agent.perform_task("cook"))

    agent.remove_capability("analyze data")
    print(agent.list_capabilities())


if __name__ == "__main__":
    main()