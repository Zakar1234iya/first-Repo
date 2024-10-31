
# .----.       .-.                _        
# `--. :       : :.-.            :_;         
#   ,',' .--.  : `'.' .--.  .--. .-. .--.                #zakari1234a@gmail.com
# .'.'_ ' .; ; : . `.' .; ; : ..': :' .; ;             
# :____;`.__,_;:_;:_;`.__,_;:_;  :_;`.__,_;
                                         
from six.moves import cStringIO
import astunparse



class Node:
    def __init__(self , value  ):
        self.value= value
        self.next = None

head = Node(1)
node_1 = Node (11)
node_2 = Node(21)
node_3 = Node(31)
node_4 = Node(41)
node_5 = Node(51)
tail = Node(61)

head.next = node_3
node_1.next = tail
node_2.next = node_5
node_3.next = node_2
node_4.next = node_1
node_5.next = node_4


# def getlength(head):
#     loai = 0
#     while head:
#         loai +=1
#         head = head.next
#     return loai

# def getmiddle(head):
#     loai = getlength(head)
#     mid_node = int(loai /2)
#     while mid_node:
#         head = head.next
#         mid_node -=1
#     return head.value

# print(getmiddle(head))
        
# def print2node():
#     counter = node_1.next 
#     while head:
#         loai +=1
#         head = head.next
#     return loai




new_head = Node(100)
new_head.next = head
head = new_head

new_tail = Node(200)
last = head
while last.next is not None:
    last = last.next
last.next = new_tail

    

while head:
    print(head.value)
    head=head.next





# print(head.value)




























# print(node_2.value)
# print(node_2.next.next.next.next.next)
# print(node_4)



# current=head
# while current:
#     print(current.value)
#     current = current.next




