"""
-------------------------------------------------------
Data Structures Utilities
-------------------------------------------------------
Author:  Michael Moriarty
ID:      170409170
Email:   mori9170@mylaurier.ca
Section: CP164 A
__updated__ = "2021-06-10"
-------------------------------------------------------
"""
from List_array import List
from Priority_Queue_array import Priority_Queue
from Queue_circular import Queue
from Stack_array import Stack


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    for i in range(len(source) - 1, -1, -1):
        stack.push(source[i])
        del source[i]

    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())

    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()

    test_1 = s.is_empty()
    print("Test 1 Expects True: " + str(test_1))

    s.push(source[0])
    print("Push: " + str(source[0]))

    test_2 = s.is_empty()
    print("Test 2 Expects False: " + str(test_2))

    print("Peek expects " + str(source[0]) + ": " + str(s.peek()))

    while not s.is_empty():
        v = s.pop()
        print("Popped: {}".format(v))

    test_3 = s.is_empty()
    print("Test 3 Expects True: " + str(test_3))

    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not len(source) == 0:
        queue.insert(source[0])
        del source[0]

    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not queue.is_empty():
        target.append(queue.remove())

    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print("Expects True: " + str(q.is_empty()))

    for item in a:
        q.insert(item)

    print("Expects False: " + str(q.is_empty()))

    print("""Expects:
{}

Gets:
{}""".format(str(a[0]), str(q.peek())))

    while not q.is_empty():
        q.remove()

    print("Expects True: " + str(q.is_empty()))

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not len(source) == 0:
        pq.insert(source[0])
        del source[0]

    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not pq.is_empty():
        target.append(pq.remove())

    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print("Expects True: " + str(pq.is_empty()))
    pq.insert(a[0])
    pq.insert(a[1])
    pq.insert(a[2])
    print("""Value one expects {}: {}
Value two expects {}: {}
Value three expects {}: {}""".format(a[0], pq._values[0], a[1], pq._values[1], a[2], pq._values[2]))
    print("Expects False: " + str(pq.is_empty()))
    print("Lowest value: " + str(pq.peek()))

    while not pq.is_empty():
        print("Removed item: " + str(pq.remove()))
    print("Expects False: " + str(pq.is_empty()))

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while len(source) != 0:
        llist.append(source[0])
        del source[0]

    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not llist.is_empty():
        target.append(llist[0])
        llist.remove(llist[0])

    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    print("Expects True: " + str(lst.is_empty()))
    for item in source:
        lst.append(item)
    print("Expects False: " + str(lst.is_empty()))
    print("First item expects {}: {}".format(source[0], lst[0]))
    print("max expects {}, got: {}".format(max(source), lst.max()))
    print("max expects {}, got: {}".format(min(source), lst.min()))
    rem = lst.remove(source[0])
    print("Remove item is {}, got: {}".format(source[0], rem))
    lst.insert(-len(lst), 101)
    print("First element expects 101, got: {}".format(lst[0]))

    count = 0
    val = source[0]
    for item in source:
        if val == item:
            count += 1

    print("Count expects {}. got: {}".format(count, lst.count(source[0])))
    print("Index expects {}, got: {}".format(0, lst.index(101)))
    print("Find expects {}, got: {}".format(101, lst.find(101)))

    while not lst.is_empty():
        lst.remove_front()

    print("Expects True: " + str(lst.is_empty()))

    return
