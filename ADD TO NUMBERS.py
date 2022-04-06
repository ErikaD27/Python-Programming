class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = list(reversed([int(x) for x in l1]))
        l4 = list(reversed([int(x) for x in l2]))
        n1, n2, suma, cadena1, cadena2 = 0, 0, 0 ,"",""
        cadena1 ="".join(map(str,l3))
        cadena2 ="".join(map(str,l4))
        n1 = int(cadena1)
        n2 = int(cadena2)
        suma = n1+n2
        l5 = list(reversed([int(x) for x in str(suma)]))
        return l5
x = Solution().addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])
print(x)