#!/usr/bin/python3.6  
# -*- coding: utf-8 -*-


class LinkedList(object):
    def __init__(self, value, next):
        super(LinkedList, self).__init__()
        self.value = value
        self.next = next
        #self.current_node = self

    def append(self, val):
        tmp = LinkedList(val, None)
        self.current_node.next = tmp
        self.current_node = tmp

        print("appended")

    def __str__(self):
        #print(self.__printable_string)
        tmp = str(self.value)
        next_node = self.next
        while True:

            tmp = "{} -> {}".format(tmp, next_node.value)
            #print(tmp)
            if next_node.next is None:
                break
            next_node = next_node.next
        return tmp

def reverse_linked_list(linked_list):
    if linked_list is None or linked_list.next is None:
        return linked_list
    last_node = linked_list
    current_node = linked_list.next
    next_node = linked_list.next.next
    while current_node is not None:


        last_node = current_node
        current_node.next = last_node

def get_middle_node(linked_list):
    if linked_list is None or linked_list.next is None:
        return linked_list
    pNode = linked_list
    qNode = linked_list.next
    while qNode.next is not None:
        pNode = pNode.next
        qNode = qNode.next.next
        if qNode is None:
            break
    return pNode.value







class BinaryDirectionLinkedList(LinkedList):
    def __init__(self, value, next, prev):
        super(BinaryDirectionLinkedList, self).__init__(value, next)
        self.prev = prev

if __name__ == "__main__":
    root = LinkedList(1, None)
    current_node = root
    for i in range(2, 20, 2):
        # tmp = LinkedList(i, None)
        # root.next = tmp
        tmp = LinkedList(i, None)
        current_node.next = tmp
        current_node = tmp
    # tmp = reverse_linked_list(root)
    print(root)
    print(get_middle_node(root))
    #print(tmp)


