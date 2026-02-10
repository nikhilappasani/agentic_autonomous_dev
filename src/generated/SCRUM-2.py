class AutonomousAgent:
    """
    A class to represent an autonomous agent capable of performing specific tasks with minimal human intervention.
    """

    def __init__(self, name: str, tasks: list[str]):
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
            print(f"Task '{task}' added to agent {self.name}.")
        else:
            print(f"Task '{task}' is already in the list of tasks for agent {self.name}.")

    def remove_task(self, task: str) -> None:
        """
        Remove a task from the agent's list of capabilities.

        :param task: The task to be removed.
        """
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from agent {self.name}.")
        else:
            print(f"Task '{task}' is not in the list of tasks for agent {self.name}.")

    def list_tasks(self) -> list[str]:
        """
        List all tasks the agent is capable of performing.

        :return: A list of tasks.
        """
        return self.tasks


# Example usage:
if __name__ == "__main__":
    agent = AutonomousAgent(name="Agent001", tasks=["task1", "task2"])
    print(agent.perform_task("task1"))
    agent.add_task("task3")
    print(agent.list_tasks())
    agent.remove_task("task2")
    print(agent.list_tasks())