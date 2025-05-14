def rotate_list(lst, k):
    l = len(lst)
    if l == 0:
        return lst
    k = k % l
    return lst[-k:] + lst[:-k]

def find_peaks(array):
    peaks = []
    n = len(array)
    for i in range(1, n - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peaks.append(i)
    return peaks

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def generate_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i * j)
        matrix.append(row)
    return matrix

def merge_sorted_lists(lista, listb):
    return sorted(lista + listb)

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]



##Easy Assignment

print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))  # Should return []

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # Should return [1, 2, 3, 4, 5, 6]


##Medium Assignment
print(generate_matrix(3, 3))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))


##Hard Assignment
print(find_peaks([1, 3, 2, 3, 5, 4, 3, 2, 3, 1]))  # Should return [1, 4, 8]

print(rotate_list([1, 2, 3, 4, 5], 2))  # Should return [4, 5, 1, 2, 3]
print(rotate_list([1, 2, 3], 4))  # Should return [3, 1, 2]