# Agent class
class Agent:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.path = []
        self.constraints = []
