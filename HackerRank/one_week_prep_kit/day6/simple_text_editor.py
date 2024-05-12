class TextEditor:
    def __init__(self):
        self.text = ""  # Current state of the text
        self.history = []  # History stack to store previous states

    def append(self, new_text):
        # Append new_text to the end of the text
        self.history.append(self.text)
        self.text += new_text

    def delete(self, num_chars):
        # Delete the last num_chars characters from the text
        self.history.append(self.text)
        self.text = self.text[:-num_chars]

    def print_char(self, index):
        # Print the character at the given index
        print(self.text[index - 1])

    def undo(self):
        # Undo the last operation by restoring the previous state of the text
        if self.history:
            self.text = self.history.pop()


# Main function to process operations
def process_operations(n):
    editor = TextEditor()
    for _ in range(n):
        operation = input().strip().split()
        op_type = int(operation[0])
        if op_type == 1:  # Append operation
            editor.append(operation[1])
        elif op_type == 2:  # Delete operation
            editor.delete(int(operation[1]))
        elif op_type == 3:  # Print operation
            editor.print_char(int(operation[1]))
        elif op_type == 4:  # Undo operation
            editor.undo()


# Read the number of operations
n = int(input().strip())

# Process the operations
process_operations(n)


"""Test Input 1
8
1 abc
3 3
2 3
1 xy
3 2
4
4
3 1
"""