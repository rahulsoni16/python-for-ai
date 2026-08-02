# Lists 
import numbers


my_lists=[1, 2, 3, 4, 5]
print(my_lists)

age = 25
has_license = True

my_list = [age, has_license, "Hello", 3.14, [1, 2, 3]]
print(my_list[0])  # Accessing the first element    
print(my_list[-1])  # Accessing the last element
print(my_list[4])  # Accessing the nested list
print(my_list[-1][1])  # Accessing the second element of the nested list

 # Finding the index of an element
my_list.append("New Element")  # Adding an element to the end of the list
print(my_list)
my_list.remove(3.14)  # Removing an element from the list
print(my_list)
my_list.insert(3, 3.14)  # Inserting an element at a specific index
print(my_list)

print(my_list[4][1])
# my_list.insert(my_list[4][1], 6)
# my_list.insert(my_list[4][1], 10)

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sorting the list in ascending order
print(numbers) 

# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Accessing a value by key
person["age"] = 31  # Updating a value
person["country"] = "USA"  # Adding a new key-value pair
print(person)
del person["city"]  # Removing a key-value pair
print(person)
print(person.keys())
print(person.values())
print(person.items())  # Getting all key-value pairs as tuples

if "name" in person:
    print("Name is present in the dictionary.")

person.update({"age": 32, "city": "Los Angeles", "phone": "123-456-7890"})  # Updating multiple key-value pairs
print(person)

# Tuples are immutable sequences, typically used to store related pieces of data.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Accessing the first element


# Sets are unordered collections of unique elements.
empty_set = set()  # Creating an empty set
numbers_set = {1, 2, 3, 4, 4, 5}
print(numbers_set)

fruits = set(["apple", "banana", "cherry"])
fruits.add("orange")  # Adding an element to the set
fruits.update(["grape", "kiwi"])  # Adding multiple elements to the set
print(fruits)
fruits.add("banana")  # Adding a duplicate element (will not be added)
fruits.remove("banana")  # Removing an element from the set
print(fruits)