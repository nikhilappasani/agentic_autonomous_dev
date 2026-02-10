class AutonomousAgent:
    """
    A class to represent an autonomous agent capable of performing specific tasks
    with minimal human intervention.
    """

    def __init__(self, name: str, tasks: list[str]) -> None:
        """
        Initialize the autonomous agent with a name and a list of tasks.

        :param name: The name of the agent.
        :param tasks: A list of tasks the agent is capable of performing.
        """
        self.name = name
        self.tasks = tasks

    def perform_task(self, task: str) -> str:
        """
        Perform a specified task if it is within the agent's capabilities.

        :param task: The task to be performed.
        :return: A message indicating the result of the task execution.
        """
        if task in self.tasks:
            return f"Agent {self.name} is performing task: {task}"
        else:
            return f"Task '{task}' is not within the capabilities of agent {self.name}."

    def add_task(self, task: str) -> None:
        """
        Add a new task to the agent's list of capabilities.

        :param task: The task to be added.
        """
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task: str) -> None:
        """
        Remove a task from the agent's list of capabilities.

        :param task: The task to be removed.
        """
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self) -> list[str]:
        """
        List all tasks the agent is capable of performing.

        :return: A list of tasks.
        """
        return self.tasks


def main() -> None:
    """
    Main function to demonstrate the usage of the AutonomousAgent class.
    """
    # Create an instance of AutonomousAgent
    agent = AutonomousAgent(name="Agent001", tasks=["task1", "task2"])

    # Perform a task
    print(agent.perform_task("task1"))

    # Add a new task
    agent.add_task("task3")

    # List all tasks
    print("Tasks:", agent.list_tasks())

    # Remove a task
    agent.remove_task("task2")

    # List all tasks after removal
    print("Tasks after removal:", agent.list_tasks())


if __name__ == "__main__":
    main()