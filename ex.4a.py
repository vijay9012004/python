class CarQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity 

    def is_full(self):
        return len(self.queue) >= self.capacity

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, car_number):
        if self.is_full():
            print(f"Parking full. Car {car_number} cannot enter.")
        else:
            self.queue.append(car_number)
            print(f"Car {car_number} entered the parking queue.")

    def dequeue(self):
        if self.is_empty():
            print(" No cars to exit. Parking is empty.")
        else:
            leaving_car = self.queue.pop(0)
            print(f" Car {leaving_car} has exited the parking lot.")

    def display(self):
        if self.is_empty():
            print(" No cars in the parking queue.")
        else:
            print(" Cars currently in queue:", ' , '.join(self.queue))


def main():
    parking = CarQueue(capacity=5)

    while True:
        print("\n----- Parking Lot Menu -----")
        print("1. Car Enter (Enqueue)")
        print("2. Car Exit (Dequeue)")
        print("3. Display Queue")
        print("4. Exit Program")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            car_number = input("Enter car number: ")
            parking.enqueue(car_number)
        elif choice == '2':
            parking.dequeue()
        elif choice == '3':
            parking.display()
        elif choice == '4':
            print("Exiting the parking system.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
