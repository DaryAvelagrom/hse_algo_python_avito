class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_element = Element(value)

        if self.head is None:
            self.head = new_element
            self.tail = new_element
        else:
            self.tail.next = new_element
            self.tail = new_element


def merge_lists_tmp(list1, list2):
    cur1 = list1.head
    cur2 = list2.head

    tmp = Element(0)
    current = tmp

    while cur1 is not None and cur2 is not None:
        if cur1.value <= cur2.value:
            current.next = cur1
            cur1 = cur1.next
        else:
            current.next = cur2
            cur2 = cur2.next

        current = current.next

    if cur1 is not None:
        current.next = cur1
    else:
        current.next = cur2

    return tmp.next


def merge_lists_no_tmp(list1, list2):
    cur1 = list1.head
    cur2 = list2.head

    if cur1 is None:
        return cur2

    if cur2 is None:
        return cur1

    if cur1.value <= cur2.value:
        head = cur1
        cur1 = cur1.next
    else:
        head = cur2
        cur2 = cur2.next

    current = head

    while cur1 is not None and cur2 is not None:
        if cur1.value <= cur2.value:
            current.next = cur1
            cur1 = cur1.next
        else:
            current.next = cur2
            cur2 = cur2.next

        current = current.next

    if cur1 is not None:
        current.next = cur1
    else:
        current.next = cur2

    return head
