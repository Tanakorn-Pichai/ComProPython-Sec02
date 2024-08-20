def find_single_occurrence_numbers(numbers: list) -> list:
    count_dict = {}
    if 1 <= len(numbers) <= 1000:

        for num in numbers:
            count_dict[num] = count_dict.get(num, 0) + 1

        single_occurrence_numbers = [num for num in numbers if count_dict[num] == 1]
        return single_occurrence_numbers
    else:
        return "null"


print(find_single_occurrence_numbers([4, 5, 6, 4, 7, 5, 8]))

print(find_single_occurrence_numbers([1, 2, 2, 3, 3, 4, 4]))

print(find_single_occurrence_numbers([1, 2, 3, 4, 5, 6]))
print(find_single_occurrence_numbers([1, 1, 1, 1, 1]))
