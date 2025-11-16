# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

from collections import deque
visited=[]
def bfs_queue(adj_graph, start_node):
    visited = []
    queue = deque()
    queue.append(start_node)
    while queue:
        cur_node = queue.popleft()
        visited.append(cur_node)
        next_node_list = adj_graph[cur_node]
        for next in next_node_list:
            if next not in visited:
                queue.append(next)

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!