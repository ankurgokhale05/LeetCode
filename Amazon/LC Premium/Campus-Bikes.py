'''
Time Complexity: O(MNlog(MN))
Space Complexity: O(MN)
Used Distance to (Worker, Bike) pair in Hashmap
We need to sort dictionary based on Distance. In Java there is TreeMap. In python we have Sorted Dictionary.


from sortedcontainers import SortedDict
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        if workers == None or len(workers) == 0 or bikes == None or len(bikes) == 0:
            return []
        od = SortedDict()
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist = self.calculateManhattanDist(workers[i], bikes[j])
                if dist not in od:
                    od[dist] = []
                od[dist].append((i, j))
        # allocate the bikes to specific workers
        
        result = [-1] * len(workers)
        bikes_assigned = [False] * len(bikes)
        count = 0
        for dist in od.keys():
            li = od[dist]
            for wb in li:
                worker = wb[0]
                bike = wb[1]
                if result[worker] == -1 and bikes_assigned[bike] == False:
                    result[worker] = bike
                    bikes_assigned[bike] = True
                    count += 1
                if count == len(workers):
                    return result
        return result
        

    def calculateManhattanDist(self, workers, bikes):
        return abs(workers[0] - bikes[0]) + abs(workers[1] - bikes[1])

'''
'''
Time Complexity: O(MN)
Space Complexity: O(2000) ~ O(1)

'''

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        if workers == None or len(workers) == 0 or bikes == None or len(bikes) == 0:
            return []
        #od = SortedDict()
        od = [-1] * 2000
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist = self.calculateManhattanDist(workers[i], bikes[j])
                if od[dist] == -1:
                    od[dist] = []
                od[dist].append((i,j))
        # allocate the bikes to specific workers
        
        result = [-1] * len(workers)
        bikes_assigned = [False] * len(bikes)
        count = 0
        for dist in range(len(od)):
            li = od[dist]
            if li != -1:
                for wb in li:
                    worker = wb[0]
                    bike = wb[1]
                    if result[worker] == -1 and bikes_assigned[bike] == False:
                        result[worker] = bike
                        bikes_assigned[bike] = True
                        count += 1
                    if count == len(workers):
                        return result
        return result
        

    def calculateManhattanDist(self, workers, bikes):
        return abs(workers[0] - bikes[0]) + abs(workers[1] - bikes[1])