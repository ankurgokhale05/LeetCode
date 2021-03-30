class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def findShips(topRight, bottomLeft):
            # terminal condition
            if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
                return 0
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))
            
            if not sea.hasShips(topRight, bottomLeft):
                return 0
            midX = (topRight.x + bottomLeft.x) // 2
            midY = (topRight.y + bottomLeft.y) // 2
            mid = Point(midX, midY)
            
            top_left_quadrant = findShips(Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1))
            top_right_quadrant = findShips(topRight, Point(mid.x+1, mid.y +1))
            bottom_right_quadrant = findShips(Point(topRight.x, mid.y), Point(mid.x+1,bottomLeft.y))
            bottom_left_quadrant = findShips(Point(mid.x, mid.y), bottomLeft)
            
            return top_left_quadrant + top_right_quadrant + bottom_right_quadrant + bottom_left_quadrant
        return findShips(topRight , bottomLeft)
            
            
            