current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

from collections import deque


# 내 풀이- 어떤 경우에는 정답과 달랐지만 => 결국 해결하였다.
def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    # dfs는 안된다. 왜냐하면 갈수있는 동서남북을 다 탐색후 가장 순서상 먼저인것을 가야하는데, 마지막에 넣은 갈수있는곳으로 가서 그렇다.

    #문제의 원인이 이것이었다.
    # 애초에 문제 입력 조건을 이렇게 준다
    # d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽
    # 북, 동, 남, 서
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    #  북, 서, 남, 동,
    # dr = [-1, 0, 1, 0]
    # dc = [0, -1, 0, 1]

    cur_r = r
    cur_c = c
    cur_d = d
    clean_count = 0
    stack = []
    queue = deque()

    row_length = len(room_map)
    col_length = len(room_map[0])

    while (1):
        cur_position_data = room_map[cur_r][cur_c]
        cur_d_store = cur_d
        # print(cur_d_store);
        if cur_position_data == 0:
            clean_count += 1
            room_map[cur_r][cur_c] = 'v'

        cur_d = cur_d
        for i in range(1, 5):
            cur_d = (cur_d + 3) % 4
            if 0 <= cur_r + dr[cur_d] < row_length and 0 <= cur_c + dc[cur_d] < col_length and \
                    room_map[cur_r + dr[cur_d]][cur_c + dc[cur_d]] == 0:
                queue.append([cur_r + dr[cur_d], cur_c + dc[cur_d], cur_d])
                break;

        # print(queue)

        # 만약 아무것도 넣지 못했으면, 후진을 하자
        if len(queue) == 0:
            # 후진을 하되 바라보는 방향은 같아야한다
            cur_d = cur_d_store
            # print("후진 : ", cur_d);
            cur_d_tmp = (cur_d + 2) % 4
            if 0 <= cur_r + dr[cur_d_tmp] < row_length and 0 <= cur_c + dc[cur_d_tmp] < col_length and \
                    room_map[cur_r + dr[cur_d_tmp]][cur_c + dc[cur_d_tmp]] != 1:
                cur_r = cur_r + dr[cur_d_tmp]
                cur_c = cur_c + dc[cur_d_tmp]

            else:
                return clean_count

        else:
            # 빼서 이동하자
            tmp = queue.popleft()
            cur_r = tmp[0]
            cur_c = tmp[1]
            # 새로운 칸 이동한 후에는 새로 탐색해야하므로 초기화를 해버리자
            queue = deque()
            cur_d = tmp[2]

            # print(queue);


# 북 동 남 서
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]


# 방향 전환
# def get_d_index_when_rotate_to_left(d):
#     return (d + 3) % 4
#
#
# # 후진
# def get_d_index_when_go_back(d):
#     return (d + 2) % 4
#
#
# def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
#     n = len(room_map)
#     m = len(room_map[0])
#     count_of_departments_cleaned = 1  # 청소하는 칸의 개수
#     room_map[r][c] = 2
#     queue = deque([[r, c, d]])
#
#     # 큐가 비어지면 종료
#     while queue:
#         r, c, d = queue.popleft()
#         temp_d = d
#
#         for i in range(4):
#             temp_d = get_d_index_when_rotate_to_left(temp_d)
#             new_r, new_c = r + dr[temp_d], c + dc[temp_d]
#
#             # a
#             if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
#                 count_of_departments_cleaned += 1
#                 room_map[new_r][new_c] = 2
#                 queue.append([new_r, new_c, temp_d])
#                 break
#
#             # c
#             elif i == 3:  # 갈 곳이 없었던 경우
#                 new_r, new_c = r + dr[get_d_index_when_go_back(d)], c + dc[get_d_index_when_go_back(d)]
#                 queue.append([new_r, new_c, d])
#
#                 # d
#                 if room_map[new_r][new_c] == 1:  # 뒤가 벽인 경우
#                     return count_of_departments_cleaned

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6, 3, 1, current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7, 4, 1, current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6, 2, 0, current_room_map4))
