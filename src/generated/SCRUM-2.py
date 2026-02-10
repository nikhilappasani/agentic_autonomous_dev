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
        Perform a specified task if it is within the agent's capabilities.

        :param task: The task to be performed.
        :return: True if the task is performed successfully, False otherwise.
        """
        if task in self.capabilities:
            print(f"{self.name} is performing task: {task}")
            return True
        else:
            print(f"Task '{task}' is not within {self.name}'s capabilities.")
            return False

    def add_capability(self, new_capability: str) -> None:
        """
        Add a new capability to the agent's list of capabilities.

        :param new_capability: The new capability to be added.
        """
        if new_capability not in self.capabilities:
            self.capabilities.append(new_capability)
            print(f"Added new capability: {new_capability}")
        else:
            print(f"Capability '{new_capability}' already exists.")

    def list_capabilities(self) -> list[str]:
        """
        List all capabilities of the agent.

        :return: A list of the agent's capabilities.
        """
        return self.capabilities


def main():
    """
    Main function to demonstrate the use of the AutonomousAgent class.
    """
    # Create an instance of AutonomousAgent
    agent = AutonomousAgent(name="Agent001", capabilities=["task1", "task2"])

    # Perform tasks
    agent.perform_task("task1")
    agent.perform_task("task3")

    # Add a new capability
    agent.add_capability("task3")

    # List all capabilities
    capabilities = agent.list_capabilities()
    print(f"Current capabilities: {capabilities}")


if __name__ == "__main__":
    main()