def generate_tree(paths):
    tree = {}
    for path in paths:
        parts = path.split('/')
        current_level = tree
        for part in parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
    return tree 

def transform_grades(grades):
    transformed = {}
    for student, scores in grades.items():
        average = sum(scores) / len(scores)
        highest = max(scores)
        lowest = min(scores)
        transformed[student] = {
            "average": round(average, 2),
            "highest": highest,
            "lowest": lowest
        }
    return transformed

def add_contact(contacts, name, **info):
    if name not in contacts:
        contacts[name] = {}
    for key, value in info.items():
        contacts[name][key] = value

def word_frequencies(text):
    words = text.split()
    frequencies = {}
    for word in words:
        word = word.lower()
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = value
    return merged

def invert_dictionary(d):
    return {v: k for k, v in d.items()}

##Easy 

print(invert_dictionary({"a": 1, "b": 2, "c": 3}))  # Should return {1: "a", 2: "b", 3: "c"}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  # Should return {"a": 1, "b": 3, "c": 4}


##Medium

text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
# Should return {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}

contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")  # Updates Alice's info

print(contacts)
# Should return:
# {
#   "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
#   "Bob": {"phone": "987-654-3210"}
# }

# Example usage:
grades = {
    "Alice": [85, 90, 95],
    "Bob": [70, 80, 90],
    "Charlie": [90, 92, 93]
}

##Hard

print(transform_grades(grades))
# Should return:
# {
#   "Alice": {"average": 90.0, "highest": 95, "lowest": 85},
#   "Bob": {"average": 80.0, "highest": 90, "lowest": 70},
#   "Charlie": {"average": 91.67, "highest": 93, "lowest": 90}
# }


paths = [
    "folder1/file1.txt",
    "folder1/folder2/file2.txt",
    "folder3/file3.txt"
]

print(generate_tree(paths))
# Should return:
# {
#   "folder1": {
#     "file1.txt": {},
#     "folder2": {
#       "file2.txt": {}
#     }
#   },
#   "folder3": {
#     "file3.txt": {}
#   }
# }