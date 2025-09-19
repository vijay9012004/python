class Node:
    def __init__(self, car_number):
        self.car_number = car_number
        self.next = None

class CarQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, car_number):
        new_node = Node(car_number)
        if self.rear is None:  
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Car {car_number} entered the parking queue.")

    def dequeue(self):
        if self.is_empty():
            print("Parking is empty. No cars to exit.")
            return
        leaving_car = self.front.car_number
        self.front = self.front.next
        if self.front is None:  
            self.rear = None
        print(f"Car {leaving_car} has exited the parking lot.")

    def display(self):
        if self.is_empty():
            print("Parking queue is empty.")
            return
        current = self.front
        cars = []
        while current:
            cars.append(current.car_number)
            current = current.next
        print("Cars in parking queue:", " <- ".join(cars))



def main():
    parking = CarQueue()

    while True:
        print("\n1. Car Enter (Enqueue)")
        print("2. Car Exit (Dequeue)")
        print("3. Display Queue")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            car_number = input("Enter car number: ")
            parking.enqueue(car_number)
        elif choice == '2':
            parking.dequeue()
        elif choice == '3':
            parking.display()
        elif choice == '4':
            print("Exiting parking system.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
