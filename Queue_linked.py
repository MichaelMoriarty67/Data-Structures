"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author:  Michael Moriarty
ID:      170409170
Email:   mori9170@mylaurier.ca
Term:    A
__updated__ = "2021-07-15"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Values are stored in a
        linked structure.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """

        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """

        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        count = 0
        curr = self._front

        while curr is not None:
            count += 1
            curr = curr._next

        return count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        # if inserting into empty queue
        if self._count == 0:
            self._front = _Queue_Node(value, self._front)
            self._rear = self._front
            self._count += 1

        # appending to back of non-empty queue
        else:
            self._rear._next = _Queue_Node(value, None)
            self._rear = self._rear._next
            self._count += 1

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        value = deepcopy(self._front._value)
        self._front = self._front._next
        if self._front is None:
            self._rear = None

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        if self._front == None:
            value = None
        else:
            value = deepcopy(self._front._value)

        return value

    def _move_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"

        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        n = len(self)

        # adds self front to end of queue
        source._rear._next = self._front
        self._front = None

        # updates source rear to self rear
        source._rear = self._rear
        self._rear = None

        # updates counts of both
        self._count = 0
        source._count += n

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        curr1 = source1._front
        curr2 = source2._front

        while curr1 is not None or curr2 is not None:

            if curr1 is not None:
                source1._front = source1._front._next
                source1._count -= 1

                # if inserting into an empty queue
                if self._count == 0:
                    self._front = curr1
                    self._rear = self._front
                    self._count += 1

                # inserting into a non-empty queue
                else:
                    self._rear._next = curr1
                    self._rear = self._rear._next
                    self._rear._next = None
                    self._count += 1

                curr1 = source1._front

            if curr2 is not None:
                source2._front = source2._front._next
                source2._count -= 1

                # if inserting into an empty queue
                if self._count == 0:
                    self._front = curr2
                    self._rear = self._front
                    self._count += 1

                # inserting into a non-empty queue
                else:
                    self._rear._next = curr2
                    self._rear = self._rear._next
                    self._rear._next = None
                    self._count += 1

                curr2 = source2._front

        source1._rear = None
        source2._rear = None

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        curr = self._front
        target1 = Queue()
        target2 = Queue()

        while curr is not None:

            self._front = self._front._next
            self._count -= 1

            # append front node of self to target1
            if target1._count == 0:
                target1._front = curr
                target1._rear = target1._front
                target1._count += 1

            else:
                target1._rear._next = curr
                target1._rear = curr
                target1._rear._next = None
                target1._count += 1

            curr = self._front
            if curr is not None:
                # append front node of self to target2
                if target2._count == 0:
                    target2._front = curr
                    target2._rear = target2._front
                    target2._count += 1

                else:
                    target2._rear._next = curr
                    target2._rear = curr
                    target2._rear._next = None
                    target2._count += 1

                # reset value to front of queue
                curr = self._front

        return target1, target2

    def is_identical(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Values of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
