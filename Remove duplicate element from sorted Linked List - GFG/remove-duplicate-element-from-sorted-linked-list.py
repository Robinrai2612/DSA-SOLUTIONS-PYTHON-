def removeDuplicates(head):
    # Check if the linked list is empty or has only one node
    if head is None or head.next is None:
        return head
    
    # Initialize a pointer to the head of the list
    current = head
    
    # Traverse the linked list
    while current is not None:
        # Compare the current node's data with the next node's data
        if current.next is not None and current.data == current.next.data:
            # Skip the next node (remove the duplicate)
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next
    
    return head

# Function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the 
    #linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print('')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        removeDuplicates(a.head)
        a.printList()
# } Driver Code Ends