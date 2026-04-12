finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    max_index = len(finding_numbers) - 1
    min_index = 0
    target_index = (max_index + min_index) // 2

    find_count = 0

    while min_index <= max_index :
        find_count += 1
        if finding_target == finding_numbers[target_index]:
            print(find_count)
            return True
        elif finding_target > finding_numbers[target_index]:
            min_index = target_index + 1
            target_index = (max_index + min_index) // 2
        else:
            max_index = target_index - 1
            target_index = (max_index + min_index) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)