import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
    
        n = len(points)
        visited = [False] * n
        min_heap = [(0, 0)] 
        total_cost = 0
        edges_used = 0

        def manhattan_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        while edges_used < n:
            cost, curr_point = heapq.heappop(min_heap)
            if visited[curr_point]:
                continue

            visited[curr_point] = True
            total_cost += cost
            edges_used += 1

            for next_point in range(n):
                if not visited[next_point]:
                    dist = manhattan_dist(points[curr_point], points[next_point])
                    heapq.heappush(min_heap, (dist, next_point))

        return total_cost
