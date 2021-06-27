#Easy -- https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1#

def findMid(head):
    # Code here
    # return the value stored in the middle node
    temp = head
    cnt = 0
    while temp is not None:
        cnt += 1
        temp = temp.next
    res = 1+ cnt//2
    cnt = 0
    temp = head
    while temp is not None:
        cnt += 1
        if cnt == res:
            return temp.data
        temp = temp.next
    


