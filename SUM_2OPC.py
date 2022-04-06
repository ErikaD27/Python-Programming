#Ejercicio que indica la posición de dos valores del arreglo que al sumarse da como resultado el target
class Solution(object):
    def twoSum(self, nums, target):
        dicc = {}
        inter = 0
        for i, v in enumerate(nums):
            inter = target - v
            if inter in dicc:
                return [dicc[inter], i]
            dicc[v] = i

X=Solution().twoSum([3,3],6)
print(X)