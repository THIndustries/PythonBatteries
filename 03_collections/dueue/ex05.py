from collections import deque


class TextEditor(deque):

    def __init__(self):
        super(TextEditor, self).__init__()
        self.dq = deque()
        self.temp = []

    def add_text(self, text):
        self.dq.append(text)

    def undo(self):
        self.temp.append(self.dq.pop())

    def redo(self):
        self.dq.append(self.temp.pop())

    def get_text(self):
        return ''.join(self.dq)

editor = TextEditor()
editor.add_text("Hello, ")

assert editor.get_text() == "Hello, "

editor.add_text("World!")
assert editor.get_text() == "Hello, World!"

editor.add_text(" How are you!")
assert editor.get_text() == "Hello, World! How are you!"

editor.undo()
assert editor.get_text() == "Hello, World!"

editor.redo()
assert editor.get_text() == "Hello, World! How are you!"

editor.undo()
assert editor.get_text() == "Hello, World!"

editor.undo()
assert editor.get_text() == "Hello, "
