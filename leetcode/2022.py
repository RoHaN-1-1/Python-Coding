#Convert 1D Array into 2D Array
class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m *n:
            return []

        result = []
        for i in range(0,m):
            row = original[i*n:(i+1)*n]
            result.append(row)
        return result