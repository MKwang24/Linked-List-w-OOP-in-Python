

class Node:
    ''' Each node in the link list '''
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

class Queue:
    ''' Linked List class '''
    def __init__(self, l =[]):
        self.length = 0
        self.head = None
        self.tail = None

        if len(l)!=0:
            for ll in l:
                self.append(ll)

    def __str__(self):
        ''' (Queue) -> str
        Returns a string representation of the queue
        >>> Queue(['a', 'bc']).__str__()
        "['a', 'bc']"
        >>> print(Queue(['a', 'bc']))
        ['a', 'bc']
        '''
        node = self.head
        l = []
        while node != None:
            l.append(node.cargo)
            node = node.next

        return(str(l))

    def append(self, cargo):
            '''(Queue, type_of_cargo) -> NoneType
            Adds an element at the tail of the linked list, as the last element.
             >>> q = Queue([1])
             >>> q.append(2)
             >>> print(q)
             [1, 2]
            '''
            node = Node(cargo)

            if self.length == 0:

                self.head = node
                self.tail = node
                self.length += 1

            else:
                self.tail.next = node
                self.tail = node
                self.length += 1


    def find_min_value_position(self):
        '''(Queue) -> int
        Returns the position in the queue of the minimal cargo value. If the
        minimal value   appears several times, the position closest to the head
        of the Queue is returned.

        >>> Queue([1]).find_min_value_position()
        0
        >>> Queue([1,0]).find_min_value_position()
        1
        >>> Queue([0,1]).find_min_value_position()
        0
        >>> Queue([2,0,1,0,4]).find_min_value_position()
        1
        >>> q = Queue([64, 25, 12, 22])
        q.find_min_value_position()
        2
        '''
        position = 0
        min_index = 0

        if self.length == 0:
            return -1
        else:
            min_value = self.head.cargo
            node = self.head.next

            while node!= None:
                if node.cargo < min_value:
                    min_value = node.cargo
                    min_index = position +1
                node = node.next
                position += 1
                #print(min_value, min_index)
            return min_index

    def concatenate(self, other):
        '''(Queue, Queue) -> NoneType
        Appends the second queue at the end of the first input queue.

        >>> q1 = Queue([1,0,0])
        >>> q2 = Queue([2])
        >>> q1.concatenate(q2)
        >>> print(q1)
        [1, 0, 0, 2]
        >>> q1 = Queue([1,0,0])
        >>> q2 = Queue([])
        >>> q1.concatenate(q2)
        >>> print(q1)
        [1, 0, 0]
        >>> q1 = Queue([])
        >>> q2 = Queue([1])
        >>> q1.concatenate(q2)
        >>> print(q1)
        [1]
        '''
        # TODO: YOUR CODE
        self.tail.next = other.head
    def min_value(self):
        '''(Queue) -> type-of-cargo
        Returns the minimal cargo value in the queue. If the list is empty,
        the function returns None. The min value is not removed from the queue.

        >>> q = Queue()
        >>> print(q.min_value())
        None
        >>> q = Queue([1])
        >>> q.min_value()
        1
        >>> q = Queue([1,0,0])
        >>> q.min_value()
        0
        '''
        # TODO: YOUR CODE
        if self.length == 0:
            return
        else:    
            min_value = self.head.cargo
            node = self.head.next

            while node!= None:
                if node.cargo < min_value:
                    min_value = node.cargo
                node = node.next
            return min_value

    def remove_min(self):
        '''(Queue) -> NoneType
        Removes the first occurence of the minimal cargo value from the input
        Queue. If the input Queue is empty, nothing is removed. If the Queue
        has one element, that element is removed and the queue becomes empty.
        The legth of the input Queue is also decreased by 1.

        >>> q = Queue([1,0])
        >>> q.remove_min()
        >>> print(q)
        [1]
        >>> q = Queue([1,0,2,0])
        >>> q.remove_min()
        >>> print(q)
        [1, 2, 0]
        >>> q = Queue([1])
        >>> q.remove_min()
        >>> print(q)
        []
        >>> q = Queue()
        >>> q.remove_min()
        >>> print(q)
        []
        >>> q = Queue([0,3])
        >>> q.remove_min()
        >>> print(q)
        [3]
        '''
        # TODO: YOUR CODE
        data = self.min_value()
        if self.head is None:
            return None
        else:
            cur  = self.head
            prev = None
            while cur.cargo != data and cur.next is not None:
                prev = cur
                cur = cur.next

            # when found
            if cur.cargo == data:
                # if head
                if cur == self.head:
                    if cur.next is None:
                        self.head = None
                    else:
                        self.head = cur.next
                else:
                    if cur.next is None:
                        prev.next = None
                    else:
                        prev.next = cur.next
            else:
                return None        


def selectionSort(unsorted_linked_list):
    '''(Queue) -> Queue
    Returns a copy of the input Queue sorted in ascending order
    >>> print(selectionSort(Queue([5, 2,1,3])))
    [1, 2, 3, 5]
    >>> print(selectionSort(Queue([])))
    []
    >>> print(selectionSort(Queue([1])))
    [1]
    >>> print(selectionSort(Queue([2,1])))
    [1, 2]
    >>> print(selectionSort(Queue([64, 25, 12, 22, 11])))
    [11, 12, 22, 25, 64]
    '''
    # TODO: YOUR CODE
    ull = unsorted_linked_list
    node = ull.head
    num_list = []
    while node != None:
        num_list.append(node.cargo)
        node = node.next
    num_list.sort()
    return Queue(num_list)
