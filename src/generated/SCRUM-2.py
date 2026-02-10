class AutonomousAgent:
    """
    A class to represent an autonomous agent capable of performing specific tasks with minimal human intervention.
    """

    def __init__(self, name: str, tasks: list[str]) -> None:
        """
        Initialize the autonomous agent with a name and a list of tasks.

        :param name: The name of the agent.
        :param tasks: A list of tasks the agent is capable of performing.
        """
        self.name = name
        self.tasks = tasks
        self.task_status = {task: False for task in tasks}

    def perform_task(self, task: str) -> bool:
        """
        Perform a specified task if it is within the agent's capabilities.

        :param task: The task to be performed.
        :return: True if the task was performed successfully, False otherwise.
        """
        if task in self.tasks:
            # Simulate task execution
            self.task_status[task] = True
            print(f"Task '{task}' performed by agent '{self.name}'.")
            return True
        else:
            print(f"Task '{task}' is not within the capabilities of agent '{self.name}'.")
            return False

    def get_task_status(self, task: str) -> bool:
        """
        Get the status of a specified task.

        :param task: The task whose status is to be checked.
        :return: True if the task has been performed, False otherwise.
        """
        return self.task_status.get(task, False)

    def list_tasks(self) -> list[str]:
        """
        List all tasks the agent is capable of performing.

        :return: A list of tasks.
        """
        return self.tasks

    def reset_tasks(self) -> None:
        """
        Reset the status of all tasks to not performed.
        """
        self.task_status = {task: False for task in self.tasks}
        print(f"All tasks have been reset for agent '{self.name}'.")


# Example usage
if __name__ == "__main__":
    agent = AutonomousAgent(name="Agent001", tasks=["task1", "task2", "task3"])
    agent.perform_task("task1")
    print(agent.get_task_status("task1"))
    agent.reset_tasks()
    print(agent.get_task_status("task1"))