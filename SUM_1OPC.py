#Ejercicio que indica la posición de dos valores del arreglo que al sumarse da como resultado el target
class Solution(object):
    def twoSum(self, nums, target):
        listaUbicaciones = []
        x= 0
        j= x+1
        for x in range(len(nums)):
            for j in range(len(nums)):
                while target == nums[x] +nums[j] and j>x:
                    if nums[x]!= nums[j] :
                        listaUbicaciones.append(nums.index(nums[x]))
                        listaUbicaciones.append(nums.index(nums[j]))
                        break
                    elif nums[x] == nums[j] :
                        listaUbicaciones.append(x)
                        listaUbicaciones.append(j)
                        break
        return listaUbicaciones

X= Solution().twoSum([2,5,5,11],10)
print(X)