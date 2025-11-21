seat_count = 9
vip_seat_array = [4, 7]

memo = {
}

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    remain_seat_array = []
    fixed_count = len(fixed_seat_array)

    for i in range(len(fixed_seat_array)):
        memo[fixed_seat_array[i]] = fixed_seat_array[i]

    for i in range(1, total_count + 1):
        if i not in fixed_seat_array and i not in remain_seat_array:
            remain_seat_array.append(i)

    print(memo)
    print(remain_seat_array)

    for i in range(len(remain_seat_array)):
        current_value = remain_seat_array[i]
        prev_value = current_value - 1
        next_value = current_value + 1

        if current_value in memo:
            if prev_value in memo and prev_value >= 1:
                memo[next_value] = current_value
            elif next_value in memo and next_value <= total_count :
                memo[prev_value] = current_value
        else:
            memo[current_value] = current_value

    return fixed_seat_array


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))