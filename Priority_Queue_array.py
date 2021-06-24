"""
-------------------------------------------------------
Array version of the Priority Queue ADT.
-------------------------------------------------------
Author:  Michael Moriarty
ID:      170409170
Email:   mori9170@mylaurier.ca
Section: CP164 A
__updated__ = "2021-06-10"
-------------------------------------------------------
"""
from copy import deepcopy


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
        self._values = []
        self._first = None

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
        return len(self._values) == 0

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
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is appended to the end of the the priority queue
        Python list, and _first is updated as appropriate to the index of
        value with the highest priority.
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        if len(self._values) == 0:
            self._first = 0

        else:
            if value < self._values[self._first]:
                self._first = len(self._values)

        self._values.append(deepcopy(value))

        return

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
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"

        value = deepcopy(self._values[self._first])

        return value

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
        assert len(self._values) > 0, "Cannot remove from an empty priority queue"

        value = deepcopy(self._values[self._first])

        del self._values[self._first]

        self._set_first()

        return value

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper function to set the value of _first.
        _first is the index of the value with the highest
        priority in the priority queue. None if queue is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        if len(self._values) == 0:
            self._first = None

        else:
            self._first = 0
            for i in range(len(self._values)):
                if self._values[i] < self._values[self._first]:
                    self._first = i

        return

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values from source is preserved.
        Use: target1, target2 = source.split_key(key)
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
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        while not len(self._values) == 0:
            r = self._values[self._first]

            # going into target1
            if r < key:
                if len(target1._values) == 0:
                    target1._first = 0

                else:
                    if r < target1._values[target1._first]:
                        target1._first = len(target1._values)

                target1._values.append(r)
            # going into target2
            if r >= key:
                if len(target1._values) == 0:
                    target1._first = 0

                else:
                    if r < target1._values[target1._first]:
                        target1._first = len(target1._values)

                target2._values.append(r)

            del self._values[self._first]
            self._set_first()

        return target1, target2