class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if cells == None or len(cells) == 0:
            return cells
        has_cycle = False
        hash_set = set()
        cycle = 0
        
        for i in range(N):
            nextday = self.nextdays(cells)
            key = str(nextday)
            if key not in hash_set:
                hash_set.add(key)
                cycle += 1
            else:
                has_cycle = True
                break
            cells = nextday
        if has_cycle:
            N = N % cycle
            for i in range(N):
                cells = self.nextdays(cells)
        return cells
    
    def nextdays(self, cells: List[int]):
        temp = [0] * len(cells)
        for i in range(1, len(cells) - 1):
            if cells[i-1] == cells[i+1]:
                temp[i] = 1
            else:
                temp[i] = 0
        return temp
            
            
                
        