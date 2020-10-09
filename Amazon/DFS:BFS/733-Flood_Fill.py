'''
Standard Depth First Search. Watch out for the boundary conditions. We have to update pixel color 4 directionally to the one which was updated to newColor with same starting color.
Time Complexity : O(n)
Space Complexity: O(n)
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr:int, sc:int, newColor:int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.fill(image, sr, sc,image[sr][sc], newColor)
        return image
    
    
    def fill(self, image, sr, sc, color, newColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color:
            return 0
        image[sr][sc] = newColor
        self.fill(image, sr - 1, sc,color, newColor)
        self.fill(image, sr + 1, sc,color, newColor)
        self.fill(image, sr, sc - 1,color, newColor)            
        self.fill(image, sr, sc + 1,color, newColor)