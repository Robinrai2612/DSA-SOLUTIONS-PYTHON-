class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Function to calculate the Manhattan distance between two points
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Create a list to store all edges with their distances
        edges = []
        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((manhattan_distance(points[i], points[j]), i, j))

        # Sort the edges by their distances in ascending order
        edges.sort()

        # Initialize a parent array for Union-Find
        parent = list(range(n))

        # Function to find the root parent of a node
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        # Initialize the minimum cost
        min_cost = 0

        # Kruskal's algorithm to build the minimum spanning tree
        for edge in edges:
            cost, u, v = edge
            root_u = find(u)
            root_v = find(v)

            # If the nodes are not in the same connected component, add this edge to the minimum spanning tree
            if root_u != root_v:
                parent[root_u] = root_v
                min_cost += cost

        return min_cost

