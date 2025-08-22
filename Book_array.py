size = 5

stack = []

def push(book_title):
    if len(stack) >= size:
        print("Error: Stack is full. Cannot push.")
        return
    stack.append(book_title)
    print(f'"{book_title}" has been pushed to the stack.')

def pop():
    if len(stack) == 0:
        print("Error: Stack is empty. Cannot pop.")
        return
    removed = stack.pop()
    print(f'"{removed}" has been popped from the stack.')

def peek():
    if len(stack) == 0:
        print("Error: Stack is empty.")
        return
    print(f'Top of stack: "{stack[-1]}"')

def display():
    if len(stack) == 0:
        print("Stack is empty.")
        return
    print("\nStack contents (Top to Bottom):")
    for i in reversed(stack):
        print(f"- {i}")

while True:
    print("\n--- Stack Operations Menu ---")
    print("1. Push (Add Book)")
    print("2. Pop (Remove Book)")
    print("3. Peek (Top Book)")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        book = input("Enter book title to push: ")
        push(book)
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
