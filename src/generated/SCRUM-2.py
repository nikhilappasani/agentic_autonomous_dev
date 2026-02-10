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
            return f"{self.name} successfully performed the task: {task}."
        else:
            return f"{self.name} cannot perform the task: {task}. Capability not found."

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

    def remove_capability(self, capability: str) -> None:
        """
        Remove a capability from the agent.

        :param capability: The capability to be removed.
        """
        if capability in self.capabilities:
            self.capabilities.remove(capability)
            print(f"Capability '{capability}' removed from {self.name}.")
        else:
            print(f"{self.name} does not have the capability '{capability}' to remove.")

    def list_capabilities(self) -> list[str]:
        """
        List all capabilities of the agent.

        :return: A list of capabilities.
        """
        return self.capabilities


# Example usage
if __name__ == "__main__":
    agent = AutonomousAgent(name="Agent007", capabilities=["navigate", "analyze data"])
    print(agent.perform_task("navigate"))
    print(agent.perform_task("cook"))
    agent.add_capability("cook")
    print(agent.perform_task("cook"))
    agent.remove_capability("analyze data")
    print(agent.list_capabilities())