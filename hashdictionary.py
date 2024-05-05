class Dictionary:
    def __init__(self):
        self.hash_table = {}

    
    def hash(self, key):
        hash_value = sum(ord(char) for char in key)
        return hash_value % 31  


    def insert(self, key, value):
        index = self.hash(key)
        if index not in self.hash_table:
            self.hash_table[index] = []
        self.hash_table[index].append((key, value))

    
    def find(self, key):
        index = self.hash(key)
        if index in self.hash_table:
            for k, v in self.hash_table[index]:
                if k == key:
                    return v
        return None  

    
    def delete(self, key):
        index = self.hash(key)
        if index in self.hash_table:
            for i, (k, v) in enumerate(self.hash_table[index]):
                if k == key:
                    del self.hash_table[index][i]
                    return  




dict_obj = Dictionary()

while True: 
    print("1.Enter the number of entries:")
    print("2.Enter the key to search:")
    print("3.Enter the key to delete:")
    print("4.Hash Table:")
    print("4.Exit:")

    ch = int(input("Entre Your Choice:"))

    if ch == 1:
        num_entries = int(input("Enter the number of entries: "))
        for _ in range(num_entries):
            key = input("Enter key: ")
            value = input("Enter value: ")
            dict_obj.insert(key, value)

    elif ch ==2:
        search_key = input("Enter the key to search: ")
        result = dict_obj.find(search_key)
        if result is not None:
            print(f"Value found: {result}")
        else:
            print("Key not found.")

    elif ch == 3:
        delete_key = input("Enter the key to delete: ")
        dict_obj.delete(delete_key)
        print("Key deleted.")

    elif ch == 4:
        print("Hash Table:")
        print(dict_obj.hash_table)
        
    elif ch == 5:
        print("Exit Program")
        break

    else: 
        print("Invalid")