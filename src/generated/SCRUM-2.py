class AutonomousAgent:
    """
    A class to represent an autonomous agent capable of performing specific tasks
    with minimal human intervention.
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
            print(f"Capability '{capability}' added to {self.name}.")
        else:
            print(f"{self.name} already has the capability '{capability}'.")

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
    # Create an autonomous agent with initial capabilities
    agent = AutonomousAgent(name="Agent001", capabilities=["task1", "task2"])

    # Perform tasks
    print(agent.perform_task("task1"))
    print(agent.perform_task("task3"))

    # Add a new capability
    agent.add_capability("task3")

    # Perform the newly added task
    print(agent.perform_task("task3"))

    # List all capabilities
    print("Agent Capabilities:", agent.list_capabilities())


if __name__ == "__main__":
    main()