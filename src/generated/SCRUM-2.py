class AutonomousAgent:
    """
    A class representing an autonomous agent capable of performing specific tasks with minimal human intervention.
    """

    def __init__(self, name: str):
        """
        Initialize the autonomous agent with a name.

        :param name: The name of the agent.
        """
        self.name = name
        self.state = "idle"

    def perform_task(self, task: str) -> str:
        """
        Perform a specified task.

        :param task: The task to be performed by the agent.
        :return: A message indicating the task status.
        """
        self.state = "performing task"
        # Simulate task performance
        result = f"Agent {self.name} is performing task: {task}"
        self.state = "idle"
        return result

    def get_status(self) -> str:
        """
        Get the current status of the agent.

        :return: The current state of the agent.
        """
        return f"Agent {self.name} is currently {self.state}."


class SystemMonitor:
    """
    A class to monitor the performance and status of the autonomous agent system.
    """

    def __init__(self):
        """
        Initialize the system monitor.
        """
        self.logs = []

    def log_event(self, event: str) -> None:
        """
        Log an event in the system.

        :param event: The event to be logged.
        """
        self.logs.append(event)

    def get_logs(self) -> list:
        """
        Retrieve the logs of the system.

        :return: A list of logged events.
        """
        return self.logs


def main():
    """
    Main function to demonstrate the autonomous agent system.
    """
    agent = AutonomousAgent(name="Agent001")
    monitor = SystemMonitor()

    # Perform a task
    task_result = agent.perform_task("Data Analysis")
    monitor.log_event(task_result)

    # Get agent status
    status = agent.get_status()
    monitor.log_event(status)

    # Retrieve and print logs
    logs = monitor.get_logs()
    for log in logs:
        print(log)


if __name__ == "__main__":
    main()