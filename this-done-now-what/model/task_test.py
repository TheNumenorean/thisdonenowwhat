from task import *
from task_manager import *

tm: TaskManager = TaskManager("Test")

# Test creation of a Task
end: Task = Task("Finish!")
tm.add_task(end)
# assert(end.can_complete())

# Add a dependent task
work: Task = tm.make_task("Do some work")
end.add_prerequisite(work)
# Can't finish end task
# assert(not end.can_complete())

# Finish work task, now can complete end task.
# assert(work.complete())
