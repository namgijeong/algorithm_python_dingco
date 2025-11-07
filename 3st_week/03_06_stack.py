class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#내풀이
#맨끝에서만 빼고 집어넣는다
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, value):
#         if self.is_empty():
#             self.head = Node(value)
#             cur = self.head
#         else:
#             cur = self. head
#             while cur.next is not None:
#                 cur = cur.next
#
#             new_node = Node(value)
#             cur.next = new_node
#
#         return cur
#
#     # pop 기능 구현
#     def pop(self):
#         if self.is_empty():
#             return None
#         else:
#             cur = self.head
#             cur_length = 1
#             while cur.next is not None:
#                 cur = cur.next
#                 cur_length += 1
#
#             cur = self.head
#             for i in range(cur_length-1):
#                 cur = cur.next
#
#             delete_node = cur.next
#             cur.next = None
#             return delete_node
#
#     def peek(self):
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#
#         return cur
#
#     # isEmpty 기능 구현
#     def is_empty(self):
#         if self.head is None:
#             return True
#         else:
#             return False


#강의 풀이 
#head부분에 새로운 값을 추가하고
#head부분에서 값을 뺀다
class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            print("stack is Empty")
            return

        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "stack is Empty"

        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(4)
#print(stack.peek().data)
print(stack.peek())

stack.push(3)
#print(stack.peek().data)
print(stack.peek())

stack.push(5)
#print(stack.peek().data)
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())