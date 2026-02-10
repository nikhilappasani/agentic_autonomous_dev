class AutonomousAgent:
    """
    A class to represent an autonomous agent capable of performing specific tasks with minimal human intervention.
    """

    def __init__(self, name: str, capabilities: list[str]):
        """
        Initialize the autonomous agent with a name and a list of capabilities.

        :param name: The name of the agent.
        :param capabilities: A list of capabilities the agent possesses.
        """
        self.name = name
        self.capabilities = capabilities

    def perform_task(self, task: str) -> bool:
        """
        Perform a task if it is within the agent's capabilities.

        :param task: The task to be performed.
        :return: True if the task is performed successfully, False otherwise.
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

        :param capability: The capability to be added.
        """
        if capability not in self.capabilities:
            self.capabilities.append(capability)
            print(f"Capability '{capability}' added to {self.name}.")
        else:
            print(f"{self.name} already has the capability: {capability}")

    def remove_capability(self, capability: str) -> None:
        """
        Remove a capability from the agent.

        :param capability: The capability to be removed.
        """
        if capability in self.capabilities:
            self.capabilities.remove(capability)
            print(f"Capability '{capability}' removed from {self.name}.")
        else:
            print(f"{self.name} does not have the capability: {capability}")

    def list_capabilities(self) -> list[str]:
        """
        List all capabilities of the agent.

        :return: A list of capabilities.
        """
        return self.capabilities


def main():
    """
    Main function to demonstrate the usage of the AutonomousAgent class.
    """
    agent = AutonomousAgent(name="Agent001", capabilities=["navigate", "analyze data", "report"])
    
    # Perform tasks
    agent.perform_task("navigate")
    agent.perform_task("cook")

    # Add and remove capabilities
    agent.add_capability("cook")
    agent.perform_task("cook")
    agent.remove_capability("analyze data")

    # List capabilities
    print(f"Current capabilities of {agent.name}: {agent.list_capabilities()}")


if __name__ == "__main__":
    main()