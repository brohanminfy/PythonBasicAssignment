def get_stats(numbers):
    if not numbers:
        return (0, 0, 0, 0)
    
    min_num = min(numbers)
    max_num = max(numbers)
    total_sum = sum(numbers)
    avg = total_sum / len(numbers)
    
    return (min_num, max_num, total_sum, avg)


print(get_stats([1, 2, 3, 4, 5]))  #     Should return (1, 5, 15, 3.0)