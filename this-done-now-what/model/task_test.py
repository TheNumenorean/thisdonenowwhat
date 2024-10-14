from task import *

# Test creation of a Task
end: Task = Task("Finish!")
assert(end.can_complete())
# print(end)

work: Task = Task("Do some work")
end.add_prerequisite(work)
assert(not end.can_complete())
# print(work, end)

assert(work.can_complete())
# print(work, end)
assert(work.complete())
# print(work, end)
assert(end.can_complete())
# print(work, end)

assert(end.complete())
# print(work, end)


# Test creation of a Task
end: Task = Task("Finish!")
assert(end.can_complete())

work: Task = Task("Do some work")
end.add_prerequisite(work)
assert(not end.can_complete())
assert(not end.try_autocomplete())
assert(not end.complete())

assert(work.try_autocomplete())
assert(work.complete())
assert(end.can_complete()) # in fact, it already is

assert(end.complete())
# print(work, end)
