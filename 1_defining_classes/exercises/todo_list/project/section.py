from todo_list.project.task import Task
from typing import List


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda x: x.name == task_name, self.tasks))
            task.completed = True
            return f"Completed task {task_name}"
        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        for completed_task in completed_tasks:
            self.tasks.remove(completed_task)
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        result = f"Section {self.name}"
        for task in self.tasks:
            result += f"\n{task.details()}"
        return result


section = Section("New section")
task = Task("Tst", "27.04.2020")
print(section.add_task(task))
print(section.complete_task("Tst"))
print(task.completed)
