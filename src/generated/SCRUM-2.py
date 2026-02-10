class AutonomousAgent:
    """
    A class representing an autonomous agent capable of performing specific tasks with minimal human intervention.
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
        :return: A message indicating the result of the task attempt.
        """
        if task in self.tasks:
            return f"{self.name} is performing the task: {task}."
        else:
            return f"Task '{task}' is not within {self.name}'s capabilities."

    def add_task(self, task: str) -> None:
        """
        Add a new task to the agent's list of capabilities.

        :param task: The task to be added.
        """
        if task not in self.tasks:
            self.tasks.append(task)
            print(f"Task '{task}' added to {self.name}'s capabilities.")
        else:
            print(f"Task '{task}' is already in {self.name}'s capabilities.")

    def remove_task(self, task: str) -> None:
        """
        Remove a task from the agent's list of capabilities.

        :param task: The task to be removed.
        """
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from {self.name}'s capabilities.")
        else:
            print(f"Task '{task}' is not in {self.name}'s capabilities.")

    def list_tasks(self) -> list[str]:
        """
        List all tasks the agent is capable of performing.

        :return: A list of tasks.
        """
        return self.tasks


def main() -> None:
    """
    Main function to demonstrate the functionality of the AutonomousAgent class.
    """
    agent = AutonomousAgent(name="Agent007", tasks=["data analysis", "report generation"])
    print(agent.perform_task("data analysis"))
    print(agent.perform_task("email sending"))
    agent.add_task("email sending")
    print(agent.perform_task("email sending"))
    agent.remove_task("report generation")
    print(agent.list_tasks())


if __name__ == "__main__":
    main()