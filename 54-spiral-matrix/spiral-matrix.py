class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            # Pop n Append the first row 
            ret += matrix.pop(0)

            # PopNAppend the last element of every row
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            
            # reverse order last row
            if matrix:
                ret+=(matrix.pop()[::-1])
            
            # append first element of all rows/list in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
            
        return ret
