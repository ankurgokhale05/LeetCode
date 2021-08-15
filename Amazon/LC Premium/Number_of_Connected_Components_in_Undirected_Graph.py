class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def bfs(node, seen):
            queue = collections.deque([node])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
        count = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                seen.add(node)
                bfs(node, seen)
                count += 1
        return count
        