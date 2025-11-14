# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited=[]

def dfs_stack(adjacent_graph, start_node):
    not_go_node_stack = []
    not_go_node_stack.append(start_node)

    while not_go_node_stack :
        cur_node = not_go_node_stack.pop()
        visited.append(cur_node)
        next_node_list = adjacent_graph[cur_node]

        for next_node in next_node_list:
            if next_node not in visited:
                not_go_node_stack.append(next_node)

    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!