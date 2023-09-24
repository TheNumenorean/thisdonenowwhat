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
        self.pending_prerequisites = {}  # indexed by uid

        # TODO make these sets
        self.completed_prerequisites = []
        self.postrequisites = []
    
    def add_prerequisite(self, prereq):
        self.pending_prerequisites[prereq.uid] = prereq
        prereq.add_postrequisite(self)
    
    # Needed for bidirectionality
    def add_postrequisite(self, postreq):
        self.postrequisites.append(postreq)
    
    # PRIVATE FUNCTION DO NOT CALL
    def complete_prerequisite(self, prereq):
        del self.pending_prerequisites[prereq.uid]
        self.completed_prerequisites.append(prereq)

    def can_complete(self) -> bool:
        return len(self.pending_prerequisites.keys()) == 0
    
    # Returns a status bool, false if it was not completed successfully
    def complete(self) -> bool:
        if not self.can_complete():
            return False
        for req in self.postrequisites:
            # print("completing prerequisite{0}".format(req.uid))
            req.complete_prerequisite(self)
        return True

    def __eq__(self, other):
        return self.uid == other.uid
    
    def __lt__(self, other):
        return self.uid < other.uid

    def __repr__(self):
        return "({0}:{1}\nprereq:{2} \ncompleted:{3} \npostreq:{4})\n\n".format(self.uid, self.name,
                            ["\t" + str(p) for p in self.pending_prerequisites.values()],
                            ["\t" + str(p) for p in self.completed_prerequisites],
                            len(self.postrequisites))

