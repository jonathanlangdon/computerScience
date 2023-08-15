# practice creating getters and setters (usually not done in Python)


class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getCompleted(self):
        return self.completed

    def setTitle(self, new_title):
        self.title = new_title if isinstance(new_title, str) else None

    def setDescription(self, new_desc):
        self.description = new_desc if isinstance(new_desc, str) else None

    def setCompleted(self, new_comp):
        self.completed = new_comp if isinstance(new_comp, bool) else None
