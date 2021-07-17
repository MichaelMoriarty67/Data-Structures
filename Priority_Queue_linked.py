"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Winter 2020
__updated__ = "2021-07-15"
-------------------------------------------------------
"""
from copy import deepcopy


class _PQ_Node:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """

        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
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
        A copy of value is inserted into the priority queue.
        Values are stored in priority order. 
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        curr = self._front
        prev = None

        while curr is not None:

            # found spot to insert
            if curr._value > value:

                # first spot insertion
                if prev is None:
                    self._front = _PQ_Node(value, self._front)
                    self._count += 1
                    break

                # any spot insertion
                else:
                    prev._next = _PQ_Node(value, curr)
                    self._count += 1
                    break

            # last spot insertion
            if curr._next is None:
                self._rear._next = _PQ_Node(value, None)
                self._rear = self._rear._next
                self._count += 1
                break

            # no spot inserted, go to next value
            temp = curr
            curr = curr._next
            prev = temp

        # empty queue insertion
        if self._count == 0:
            self._front = _PQ_Node(value, self._front)
            self._rear = self._front
            self._count += 1

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"

        value = deepcopy(self._front._value)

        self._front = self._front._next

        # check if empty
        if self._front is None:
            self._rear = None

        self._count -= 1

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"

        if self._count == 0:
            value = None
        else:
            value = deepcopy(self._front._value)

        return value

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """

        curr = self._front
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        while curr is not None:

            # inserting into empty target1
            if target1._count == 0:

                # removing from self pq
                self._front = self._front._next
                self._count -= 1

                # adding to target1 pq
                target1._front = curr
                target1._rear = target1._front
                target1._rear._next = None
                target1._count += 1

            else:

                # already in order, can just append
                self._front = self._front._next
                self._count -= 1

                target1._rear._next = curr
                target1._rear = target1._rear._next
                target1._rear._next = None
                target1._count += 1

            curr = self._front

            if curr is not None:

                # inserting into empty target1
                if target2._count == 0:

                    # removing from self pq
                    self._front = self._front._next
                    self._count -= 1

                    # adding to target1 pq
                    target2._front = curr
                    target2._rear = target2._front
                    target2._rear._next = None
                    target2._count += 1

                else:

                    # already in order, can just append
                    self._front = self._front._next
                    self._count -= 1

                    target2._rear._next = curr
                    target2._rear = target2._rear._next
                    target2._rear._next = None
                    target2._count += 1

                curr = self._front

        self._rear = None
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = pq1.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        curr = self._front
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        while curr is not None:

            if curr._value < key:

                # inserting into empty target1
                if target1._count == 0:

                    # removing from self pq
                    self._front = self._front._next
                    self._count -= 1

                    # adding to target1 pq
                    target1._front = curr
                    target1._rear = target1._front
                    target1._rear._next = None
                    target1._count += 1

                else:

                    # already in order, can just append
                    self._front = self._front._next
                    self._count -= 1

                    target1._rear._next = curr
                    target1._rear = target1._rear._next
                    target1._rear._next = None
                    target1._count += 1

                curr = self._front

            else:

                # inserting into empty target1
                if target2._count == 0:

                    # removing from self pq
                    self._front = self._front._next
                    self._count -= 1

                    # adding to target1 pq
                    target2._front = curr
                    target2._rear = target2._front
                    target2._rear._next = None
                    target2._count += 1

                else:

                    # already in order, can just append
                    self._front = self._front._next
                    self._count -= 1

                    target2._rear._next = curr
                    target2._rear = target2._rear._next
                    target2._rear._next = None
                    target2._count += 1

                curr = self._front

        self._rear = None
        return target1, target2

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are inserted 
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        curr1 = source1._front
        curr2 = source2._front

        while curr1 is not None or curr2 is not None:

            if curr1 is not None:

                if curr2 is None:
                    # first insert
                    if self._count == 0:
                        self._front = curr1
                        self._rear = curr1
                        self._count += 1

                        source1._front = source1._front._next
                        source1._count -= 1

                    else:
                        # appending at end
                        source1._front = source1._front._next
                        source1._count -= 1

                        self._rear._next = curr1
                        self._rear = curr1
                        self._rear._next = None
                        self._count += 1

                    # update curr
                    curr1 = source1._front

                else:
                    if curr1._value <= curr2._value:
                        # first insert
                        if self._count == 0:
                            self._front = curr1
                            self._rear = curr1
                            self._count += 1

                            source1._front = source1._front._next
                            source1._count -= 1

                        else:
                            # appending at end
                            source1._front = source1._front._next
                            source1._count -= 1

                            self._rear._next = curr1
                            self._rear = curr1
                            self._rear._next = None
                            self._count += 1

                        # update curr
                        curr1 = source1._front

            if curr2 is not None:

                if curr1 is None:
                    # first insert
                    if self._count == 0:
                        self._front = curr2
                        self._rear = curr2
                        self._count += 1

                        source2._front = source2._front._next
                        source2._count -= 1

                    else:
                        # appending at end
                        source2._front = source2._front._next
                        source2._count -= 1

                        self._rear._next = curr2
                        self._rear = curr2
                        self._rear._next = None
                        self._count += 1

                    # update curr
                    curr2 = source2._front

                else:
                    if curr2._value <= curr1._value:
                        # first insert
                        if self._count == 0:
                            self._front = curr2
                            self._rear = curr2
                            self._count += 1

                            source2._front = source2._front._next
                            source2._count -= 1

                        else:
                            # appending at end
                            source2._front = source2._front._next
                            source2._count -= 1

                            self._rear._next = curr2
                            self._rear = curr2
                            self._rear._next = None
                            self._count += 1

                        # update curr
                        curr2 = source2._front

        source1._rear = None
        source2._rear = None

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
        assert source._front is not None, "Cannot append an empty priority queue"

        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
