from random import randint

# A Task is a unit of work with (0-many) prerequisites and (0-many)
# postrequisites -- that is, subsequent Tasks.
# TODO add typing to the other values
class Task:
    def __init__(self, name: str):
        self.uid = randint(1, 1000000)
        self.name = name
        self.populateDefaultValues()

    def populateDefaultValues(self):
        self.description = ""
        self.pending_prerequisites = set()  # uids
        self.completed = False  # whether the work for this Task is complete

        # TODO make these sets
        self.completed_prerequisites = set()
        self.postrequisites = set()
    
    # Unique ID accessor
    def get_uid(self):
        return self.uid

    # Prefer this function.
    def add_prerequisite(self, prereq):
        self.pending_prerequisites.add(prereq.get_uid())
        prereq.add_postrequisite(self)
    
    # Needed for bidirectionality -- do not call though
    def add_postrequisite(self, postreq):
        self.postrequisites.add(postreq.get_uid())
    
    # PRIVATE FUNCTION DO NOT CALL
    def complete_prerequisite(self, prereq):
        self.pending_prerequisites.remove(prereq.get_uid())
        self.completed_prerequisites.add(prereq.get_uid())

    def no_prereqs(self) -> bool:
        return len(self.pending_prerequisites) == 0

    def get_completed(self) -> bool:
        return self.completed
    
    def set_completed(self):
        self.completed = True

    def __eq__(self, other):
        return self.uid == other.uid
    
    def __lt__(self, other):
        return self.uid < other.uid

    def __repr__(self):
        return "({0}:{1}\nprereq:{2} \ncompleted:{3} \npostreq:{4})\n\n".format(self.uid, self.name,
                            ["\t" + str(p) for p in self.pending_prerequisites.values()],
                            ["\t" + str(p) for p in self.completed_prerequisites],
                            len(self.postrequisites))

