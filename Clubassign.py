import heapq

class Node:
    def __init__(self, N):
        self.parent = None
        self.path_cost = 0
        self.cost = 0
        self.student_id = -1
        self.club_id = -1
        self.assigned = [False] * N

def new_node(x, y, assigned, parent, N):
    node = Node(N)
    node.assigned = assigned[:]
    if y != -1:
        node.assigned[y] = True
    node.parent = parent
    node.student_id = x
    node.club_id = y
    return node

def calculate_cost(cost_matrix, x, y, assigned, N):
    cost = 0
    available = [True] * N
    for i in range(x + 1, N):
        min_cost = float('inf')
        min_index = -1
        for j in range(N):
            if not assigned[j] and available[j] and cost_matrix[i][j] < min_cost:
                min_index = j
                min_cost = cost_matrix[i][j]
        cost += min_cost
        available[min_index] = False
    return cost

def print_assignments(min_node):
    if min_node.parent is None:
        return
    print_assignments(min_node.parent)
    print(f"Assign Student {chr(min_node.student_id + ord('A'))} to Club {min_node.club_id}")

def find_min_cost(cost_matrix):
    N = len(cost_matrix)
    pq = []
    root = new_node(-1, -1, [False] * N, None, N)
    root.path_cost = root.cost = 0
    root.student_id = -1
    heapq.heappush(pq, (root.cost, root))
    
    while pq:
        _, min_node = heapq.heappop(pq)
        i = min_node.student_id + 1
        if i == N:
            print_assignments(min_node)
            return min_node.cost
        for j in range(N):
            if not min_node.assigned[j]:
                child = new_node(i, j, min_node.assigned, min_node, N)
                child.path_cost = min_node.path_cost + cost_matrix[i][j]
                child.cost = child.path_cost + calculate_cost(cost_matrix, i, j, child.assigned, N)
                heapq.heappush(pq, (child.cost, child))
    return 0

if __name__ == "__main__":
    N = int(input("Enter the number of students and clubs (N): "))
    cost_matrix = []
    print("Enter the cost matrix (NxN):")
    for _ in range(N):
        row = list(map(int, input().split()))
        cost_matrix.append(row)
    print("\nOptimal Cost is", find_min_cost(cost_matrix))
