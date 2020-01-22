#Node list

class nodelist:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

node2 = nodelist(2)
node1 = nodelist(1,node2)

def ListLength(headNode:nodelist):
    length = 0
    currentNode = headNode
    while currentNode != None:
        length +=1
        currentNode = currentNode.next
    return length

print(ListLength(node1))