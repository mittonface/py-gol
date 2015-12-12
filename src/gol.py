class World:

    def __init__(self):
        self.cells = set()

    def size(self):
        return len(self.cells)

    def empty(self):
        return len(self.cells) == 0

    def add_cell(self, x, y):
        self.cells.add((x, y))
