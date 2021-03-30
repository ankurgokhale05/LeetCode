import heapq
class Leaderboard:

    def __init__(self):
        self.leader_map = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leader_map:
            self.leader_map[playerId] = score
        else:
            self.leader_map[playerId] += score
        
    def top(self, K: int) -> int:
        heap = []
        for score in self.leader_map.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while len(heap) > 0:
            res += heapq.heappop(heap)
        return res
            
        

    def reset(self, playerId: int) -> None:
        if playerId not in self.leader_map:
            return 
        else:
            self.leader_map[playerId] = 0