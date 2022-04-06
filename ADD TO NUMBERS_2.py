def addTwoNumbers(self, l1, l2):
    output = ListNode()
    nextNode = output.next
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        s = (val1 + val2 + carry) % 10
        carry = (val1 + val2 + carry) // 10

        nextNode = ListNode(s)
        nextNode = nextNode.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
        return output.next
x = addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])
print(x)