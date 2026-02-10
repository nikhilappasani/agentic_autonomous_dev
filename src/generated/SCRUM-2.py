class AutonomousAgent:
    """
    A class representing an autonomous agent capable of performing specific tasks with minimal human intervention.
    """

    def __init__(self, environment: str, capabilities: list[str]) -> None:
        """
        Initialize the autonomous agent with its operating environment and capabilities.

        :param environment: The environment in which the agent operates.
        :param capabilities: A list of capabilities the agent possesses.
        """
        self.environment = environment
        self.capabilities = capabilities

    def perform_task(self, task: str) -> bool:
        """
        Perform a specified task if it is within the agent's capabilities.

        :param task: The task to be performed by the agent.
        :return: True if the task was performed successfully, False otherwise.
        """
        if task in self.capabilities:
            # Simulate task execution
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
            print(f"Capability '{capability}' not found.")

    def list_capabilities(self) -> list[str]:
        """
        List all capabilities of the agent.

        :return: A list of capabilities.
        """
        return self.capabilities


class EnvironmentInterface:
    """
    A class representing the interface between the autonomous agent and its environment.
    """

    def __init__(self, environment_data: dict) -> None:
        """
        Initialize the environment interface with environment data.

        :param environment_data: A dictionary containing environment data.
        """
        self.environment_data = environment_data

    def update_environment(self, key: str, value: any) -> None:
        """
        Update the environment data with a new key-value pair.

        :param key: The key to update in the environment data.
        :param value: The value to associate with the key.
        """
        self.environment_data[key] = value
        print(f"Updated environment: {key} = {value}")

    def get_environment_data(self) -> dict:
        """
        Retrieve the current environment data.

        :return: A dictionary containing the environment data.
        """
        return self.environment_data


class DataProcessingModule:
    """
    A class representing a data processing module for the autonomous agent.
    """

    def __init__(self, data: list[any]) -> None:
        """
        Initialize the data processing module with initial data.

        :param data: A list of data items to be processed.
        """
        self.data = data

    def process_data(self) -> list[any]:
        """
        Process the data and return the processed results.

        :return: A list of processed data items.
        """
        # Simulate data processing
        processed_data = [item for item in self.data if item is not None]
        print(f"Processed data: {processed_data}")
        return processed_data

    def add_data(self, new_data: any) -> None:
        """
        Add new data to the processing module.

        :param new_data: The new data item to be added.
        """
        self.data.append(new_data)
        print(f"Added data: {new_data}")

    def clear_data(self) -> None:
        """
        Clear all data from the processing module.
        """
        self.data.clear()
        print("Cleared all data.")