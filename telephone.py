class LinearHashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [None] * capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return 
            index = (index + 1) % self.capacity
        self.table[index] = (key, value)

    def lookup(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity 
        return "Not found"

    def display(self):
        for item in self.table:
            if item is not None:
                print(f"Name: {item[0]}, Number: {item[1]}")


class QuadraticHashTable(LinearHashTable):
    def insert(self, key, value):
        index = self.hash(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            i += 1
            index = (index + i*i) % self.capacity
        self.table[index] = (key, value)

    def lookup(self, key):
        index = self.hash(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = (index + i*i) % self.capacity
        return "Not found"


class TelephoneBook:
    def __init__(self,method):
        if method == "linear":
            self.book = LinearHashTable()
        elif method == "quadratic":
            self.book = QuadraticHashTable()
        else:
            raise ValueError("Invalid method. Choose 'linear' or 'quadratic'.")

    def insert(self, name, number):
        self.book.insert(name, number)

    def lookup(self, name):
        return self.book.lookup(name)

    def display(self):
        self.book.display()


if __name__ == "__main__":
    method = input("Enter the hashing method (linear or quadratic): ")
    book = TelephoneBook(method)

    while True:
        print("\n1. Insert a record")
        print("2. Lookup a record")
        print("3. Display all records")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the client's name: ")
            number = input("Enter the client's telephone number: ")
            book.insert(name, number)
        elif choice == 2:
            name = input("Enter the client's name to lookup: ")
            print(book.lookup(name))
        elif choice == 3:
            book.display()
        elif choice == 4:
            print("Program Exited")
            break
        else:
            print("Invalid choice. Please try again.")