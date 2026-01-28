class AutonomousAgent:
    """
    A class representing an autonomous agent capable of performing specific tasks with minimal human intervention.
    """

    def __init__(self, environment: str, capabilities: list[str]) -> None:
        """
        Initialize the autonomous agent with its environment and capabilities.

        :param environment: The environment in which the agent operates.
        :param capabilities: A list of capabilities the agent possesses.
        """
        self.environment = environment
        self.capabilities = capabilities

    def perform_task(self, task: str) -> bool:
        """
        Perform a specified task if it is within the agent's capabilities.

        :param task: The task to be performed.
        :return: True if the task was performed successfully, False otherwise.
        """
        if task in self.capabilities:
            print(f"Performing task: {task}")
            return True
        else:
            print(f"Task '{task}' is not within capabilities.")
            return False

    def add_capability(self, capability: str) -> None:
        """
        Add a new capability to the agent.

        :param capability: The capability to be added.
        """
        if capability not in self.capabilities:
            self.capabilities.append(capability)
            print(f"Added capability: {capability}")
        else:
            print(f"Capability '{capability}' already exists.")

    def remove_capability(self, capability: str) -> None:
        """
        Remove an existing capability from the agent.

        :param capability: The capability to be removed.
        """
        if capability in self.capabilities:
            self.capabilities.remove(capability)
            print(f"Removed capability: {capability}")
        else:
            print(f"Capability '{capability}' does not exist.")

    def list_capabilities(self) -> list[str]:
        """
        List all capabilities of the agent.

        :return: A list of capabilities.
        """
        return self.capabilities


def main() -> None:
    """
    Main function to demonstrate the usage of the AutonomousAgent class.
    """
    agent = AutonomousAgent(environment="Warehouse", capabilities=["pick", "place", "scan"])
    agent.perform_task("pick")
    agent.perform_task("deliver")
    agent.add_capability("deliver")
    agent.perform_task("deliver")
    agent.remove_capability("scan")
    print("Current capabilities:", agent.list_capabilities())


if __name__ == "__main__":
    main()