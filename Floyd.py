
def floyd_warshall(cost_matrix):
    
    n = len(cost_matrix)
    # Create a distance matrix, initialized to the input cost matrix
    dist = [[cost_matrix[i][j] for j in range(n)] for i in range(n)]

    # Perform the algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Update the distance if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def main():
    print("Enter the number of offices:")
    n = int(input().strip())

    print("Enter the cost matrix row by row (use a large value like 999999 for no direct connection):")
    cost_matrix = []
    for i in range(n):
        row = list(map(int, input().strip().split()))
        cost_matrix.append(row)

    # Apply Floyd-Warshall algorithm
    shortest_paths = floyd_warshall(cost_matrix)

    print("\nMinimum cost to connect all offices:")
    for row in shortest_paths:
        print(" ".join(map(lambda x: f"{x:7}", row)))

if __name__ == "__main__":
    main()
