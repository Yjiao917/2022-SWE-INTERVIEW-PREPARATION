class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l = 0
        r = m * n - 1
        while (l < r):
            mid = (l + r) // 2
            if (matrix[mid // n][mid % n] < target):
                l = mid + 1
            else:
                r = mid
        
        return matrix[l // n][l % n] == target