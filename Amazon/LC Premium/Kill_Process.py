'''
Time Complexity: O(N)
Space Complexity: O(N)
'''

from collections import deque
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        mapping = {}
        for p_pid, p_id in zip(ppid, pid):
            if p_pid not in mapping:
                mapping[p_pid] = [p_id]
            else:
                mapping[p_pid].append(p_id)
        queue = deque()
        queue.append(kill)
        output = []
        while queue:
            next_node = queue.popleft()
            output.append(next_node)
            if next_node in mapping:
                for node in mapping[next_node]:
                    queue.append(node)
                del mapping[next_node]
        return output