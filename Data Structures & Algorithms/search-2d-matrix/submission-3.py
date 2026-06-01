class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        starting = 0
        ending = len(matrix[0]) -1
        while starting<len(matrix) and ending >=0:
            if matrix[starting][ending] == target :
                return True
            elif matrix[starting][ending] > target:
                ending-=1
            else:
                starting+=1
        return False
        