class AutonomousAgent:
    """
    A class representing an autonomous agent capable of performing specific tasks
    with minimal human intervention.
    """

    def __init__(self, name: str, capabilities: list[str]):
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


class SystemMonitor:
    """
    A class to monitor the performance and health of the autonomous agent system.
    """

    def __init__(self):
        """
        Initialize the system monitor with default metrics.
        """
        self.performance_metrics = {
            "response_time": [],
            "throughput": []
        }

    def log_performance(self, response_time: float, throughput: int) -> None:
        """
        Log performance metrics for the system.

        :param response_time: The response time of the system.
        :param throughput: The throughput of the system.
        """
        self.performance_metrics["response_time"].append(response_time)
        self.performance_metrics["throughput"].append(throughput)

    def get_average_response_time(self) -> float:
        """
        Calculate the average response time from logged data.

        :return: The average response time.
        """
        return sum(self.performance_metrics["response_time"]) / len(self.performance_metrics["response_time"])

    def get_average_throughput(self) -> float:
        """
        Calculate the average throughput from logged data.

        :return: The average throughput.
        """
        return sum(self.performance_metrics["throughput"]) / len(self.performance_metrics["throughput"])


class SecurityManager:
    """
    A class to manage security aspects of the autonomous agent system.
    """

    def __init__(self):
        """
        Initialize the security manager with default settings.
        """
        self.encryption_enabled = False
        self.access_control_list = []

    def enable_encryption(self) -> None:
        """
        Enable data encryption for the system.
        """
        self.encryption_enabled = True

    def disable_encryption(self) -> None:
        """
        Disable data encryption for the system.
        """
        self.encryption_enabled = False

    def add_user_to_acl(self, user: str) -> None:
        """
        Add a user to the access control list.

        :param user: The user to be added.
        """
        if user not in self.access_control_list:
            self.access_control_list.append(user)

    def remove_user_from_acl(self, user: str) -> None:
        """
        Remove a user from the access control list.

        :param user: The user to be removed.
        """
        if user in self.access_control_list:
            self.access_control_list.remove(user)

    def is_user_authorized(self, user: str) -> bool:
        """
        Check if a user is authorized based on the access control list.

        :param user: The user to be checked.
        :return: True if the user is authorized, False otherwise.
        """
        return user in self.access_control_list