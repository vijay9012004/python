class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, book_title):
        new_node = Node(book_title)
        new_node.next = self.top
        self.top = new_node
        print(f'"{book_title}" pushed onto the stack.')

    def pop(self):
        if self.top is None:
            print("Error: Stack is empty. Cannot pop.")
            return
        popped = self.top.data
        self.top = self.top.next
        print(f'"{popped}" popped from the stack.')

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print(f'Top of stack: "{self.top.data}"')

    def display(self):
        if self.top is None:
            print("Stack is empty.")
            return
        temp = self.top
        print("\nStack contents (Top to Bottom):")
        while temp:
            print(f"- {temp.data}")
            temp = temp.next

stack = Stack()

while True:
    print("\n--- Linked List Stack Menu ---")
    print("1. Push (Add Book)")
    print("2. Pop (Remove Book)")
    print("3. Peek (Top Book)")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        book = input("Enter book title to push: ")
        stack.push(book)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.peek()
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
