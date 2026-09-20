class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_element = Element(value)
        new_element.prev = self.head
        if self.head is None:
            self.tail = new_element
        else:
            self.head.next = new_element
        self.head = new_element

    def pop_head(self):
        if self.head is None:
            raise IndexError("pop from empty linked list")

        value = self.head.value
        self.head = self.head.prev
        if self.head is None:
            self.tail = None
        else:
            self.head.next = None
        return value

    def pop_tail(self):
        if self.tail is None:
            raise IndexError("pop from empty linked list")

        value = self.tail.value
        self.tail = self.tail.next
        if self.tail is None:
            self.head = None
        else:
            self.tail.prev = None
        return value

    def peek_tail(self):
        if self.tail is None:
            raise IndexError("empty linked list")
        return self.tail.value

    def peek_head(self):
        if self.head is None:
            raise IndexError("empty linked list")
        return self.head.value


class Lifo:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        return self.stack.push(value)

    def pop(self):
        return self.stack.pop_head()
    
    def peek(self):
        return self.stack.peek_head()


class Fifo:
    def __init__(self):
        self.queue = LinkedList()

    def push(self, value):
        return self.queue.push(value)

    def pop(self):
        return self.queue.pop_tail()

    def peek(self):
        return self.queue.peek_tail()


def validate(pushed, popped):
    stack = Lifo()
    j = 0

    for value in pushed:
        stack.push(value)

        while j < len(popped):
            try:
                top = stack.peek()
            except IndexError:
                break

            if top != popped[j]:
                break

            stack.pop()
            j += 1

    return j == len(popped)


if __name__ == "__main__":
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 3, 5, 4, 2]

    if validate(pushed, popped):
        print('Validation passed')
    else:
        print('Validation failed')

    pushed = [1, 2, 3]
    popped = [3, 1, 2]

    if validate(pushed, popped):
        print('Validation passed')
    else:
        print('Validation failed')