from task import *

# Has all the tasks
# Tasks keep track of their dependencies
# The task manager takes care of "chaining" of work.

class TaskManager:
    def __init__(self, name: str):
        self.name = name
        self.tasks = {} # indexed by uid
    
    def add_task(self, task: Task):
        self.tasks[task.get_uid()] = task

    # Use this one
    def make_task(self, task_name: str) -> Task:
        task = Task(task_name)
        self.add_task(task)
        return task