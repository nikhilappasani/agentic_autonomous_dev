class AutonomousAgent:
    """
    A class representing an autonomous agent capable of performing specific tasks with minimal human intervention.
    """

    def __init__(self, name: str, tasks: list[str]):
        """
        Initialize the autonomous agent with a name and a list of tasks.

        :param name: The name of the agent.
        :param tasks: A list of tasks the agent is capable of performing.
        """
        self.name = name
        self.tasks = tasks
        self.state = "idle"

    def perform_task(self, task: str) -> bool:
        """
        Perform a specified task if it is within the agent's capabilities.

        :param task: The task to be performed.
        :return: True if the task was performed successfully, False otherwise.
        """
        if task in self.tasks:
            self.state = "performing task"
            # Simulate task performance
            print(f"{self.name} is performing task: {task}")
            self.state = "idle"
            return True
        else:
            print(f"Task '{task}' is not within {self.name}'s capabilities.")
            return False

    def get_status(self) -> str:
        """
        Get the current status of the agent.

        :return: The current state of the agent.
        """
        return self.state


class SystemMonitor:
    """
    A class to monitor the performance and status of the autonomous agent.
    """

    def __init__(self, agent: AutonomousAgent):
        """
        Initialize the system monitor with a reference to an autonomous agent.

        :param agent: The autonomous agent to be monitored.
        """
        self.agent = agent

    def check_agent_status(self) -> str:
        """
        Check and return the current status of the monitored agent.

        :return: The current status of the agent.
        """
        return self.agent.get_status()

    def log_performance_metrics(self, task: str, success: bool) -> None:
        """
        Log the performance metrics of a task performed by the agent.

        :param task: The task that was performed.
        :param success: Whether the task was performed successfully.
        """
        status = "success" if success else "failure"
        print(f"Task '{task}' performed with {status}.")


# Example usage
if __name__ == "__main__":
    agent = AutonomousAgent(name="Agent001", tasks=["task1", "task2", "task3"])
    monitor = SystemMonitor(agent=agent)

    task_to_perform = "task1"
    success = agent.perform_task(task_to_perform)
    monitor.log_performance_metrics(task=task_to_perform, success=success)

    print(f"Agent status: {monitor.check_agent_status()}")
