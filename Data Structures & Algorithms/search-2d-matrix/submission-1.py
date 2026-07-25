class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the value in the matrix and return true, else false
        # grab the middle most array and check its first value.
        # if the first value is greater than target move right array pointer below it
        # if the target is within the first and last value, look within the arary (will now have return)
        # else move the left array pointer one past the middle array
        leftArray, rightArray = 0, len(matrix) - 1
        while leftArray <= rightArray:
            middleArray = (rightArray + leftArray) // 2
            if matrix[middleArray][0] > target:
                rightArray = middleArray - 1
            elif matrix[middleArray][len(matrix[middleArray]) - 1] >= target:
                #handle within array
                array = matrix[middleArray]
                l, r = 0, len(array) - 1
                while l <= r:
                    middle = (r + l) // 2
                    if array[middle] == target:
                        return True
                    elif array[middle] > target:
                        r = middle - 1
                    else:
                        l = middle + 1 
                return False
            else: 
                leftArray = middleArray + 1
        return False