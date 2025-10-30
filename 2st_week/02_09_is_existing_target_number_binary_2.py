finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    array.sort()
    print(array)

    min_index = 0
    max_index = len(array) - 1
    mid_index = (min_index + max_index) // 2

    while min_index <= max_index:
        if array[mid_index] > target:
            max_index = mid_index + 1
        elif array[mid_index] == target:
            return True
        else:
            min_index = mid_index - 1
        mid_index = (min_index + max_index) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)