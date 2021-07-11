"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  Michael Moriarty
ID:      170409170
Email:   mori9170@mylaurier.ca
Term:    Spring 2021
__updated__ = "2021-07-08"
-------------------------------------------------------
"""
from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # your code here
        return

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = _List_Node(value, self._front)
        self._count += 1
        if self._rear is None:
            self._rear = self._front

        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._count == 0:
            self._front = _List_Node(value, self._front)
            self._rear = self._front

        else:
            self._rear._next = _List_Node(value, None)
            self._rear = self._rear._next

        self._count += 1
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if -(self._count) <= i <= self._count - 1:
            if i < 0:
                i = self._count + i

            if i == 0:
                self.prepend(value)
            else:
                count = 0
                current = self._top
                while current is not None:
                    if count == i - 1:
                        current._next = _List_Node(value, current._next)
                        break
                    else:
                        current = current._next
                        count += 1

        else:
            if i < 0:
                self.prepend(value)
            else:
                self.append(value)

        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        index = 0

        while current is not None:
            if current._value == key:
                break
            else:
                temp = current
                current = current._next
                previous = temp
                index += 1

        if current is None:
            previous = None
            index = -1

        return previous, current, index

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        curr = self._front
        prev = None
        index = 0

        def _linear_search_r_aux(index, prev, curr, key):
            if curr is None or curr._value == key:
                    # key not found
                if curr is None:
                    index = -1

            else:
                curr, prev, index = _linear_search_r_aux(
                    index + 1, curr, curr._next, key)

            return curr, prev, index

        current, previous, index = _linear_search_r_aux(
            index, prev, curr, key)

        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        prev, curr, i = self._linear_search(key)

        if i > 0 and i < self._count - 1:
            prev._next = curr._next
            value = deepcopy(curr._value)
            self._count -= 1

        if i == 0:
            self._front = curr._next
            value = deepcopy(curr._value)
            self._count -= 1
        if i == self._count - 1:
            prev._next = curr._next
            value = deepcopy(curr._value)
            self._rear = prev
            self._count -= 1

        if i < 0:
            value = None

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = deepcopy(self._front._value)

        self._front = self._front._next

        self._count -= 1

        if self._count == 0:
            self._rear = None

        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        curr = self._front
        prev = None

        while curr is not None:
            # if node has value of key
            if curr._value == key:

                # if removing from front of list
                if prev is None:
                    print(prev)
                    print(self._front)
                    self._front = self._front._next
                    self._count -= 1

                    # if list now empty, update rear
                    if self._count == 0:
                        self._rear = None

                    curr = curr._next

                # prev has next value, set it to curr next
                # don't update prev
                else:
                    prev._next = curr._next
                    curr = curr._next

                    # if just removed last element, update rear
                    if curr is None:
                        self._rear = prev

                    self._count -= 1

            # node doesn't have key value, got to next node
            else:
                temp = curr
                curr = curr._next
                prev = temp

        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        prev, curr, i = self._linear_search(key)

        if i > -1:
            value = deepcopy(curr._value)
        else:
            value = None

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        prev, curr, i = self._linear_search(key)

        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        if i < 0:
            i = self._count + i

        count = 0
        curr = self._front

        while curr is not None:
            if count == i:
                value = deepcopy(curr._value)
                break
            else:
                curr = curr._next
                count += 1

        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        if i < 0:
            i = self._count + i

        count = 0
        curr = self._front

        while curr is not None:
            if count == i:
                curr._value = deepcopy(value)
                value = deepcopy(curr._value)
                break
            else:
                curr = curr._next
                count += 1
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        prev, curr, i = self._linear_search(key)

        return i > -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        max_data = self._front._value
        current = self._front

        while current is not None:
            if current._value > max_data:
                max_data = deepcopy(current._value)

            current = current._next

        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        min_data = self._front._value
        current = self._front

        while current is not None:
            if current._value < min_data:
                min_data = deepcopy(current._value)

            current = current._next

        return min_data

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        number = 0
        current = self._front

        while current is not None:
            if current._value == key:
                number += 1
            current = current._next

        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        self._rear = self._front
        previous = None
        current = self._front

        while current is not None:
            temp = current._next
            current._next = previous
            previous = current
            current = temp

        self._front = previous
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        self._rear = self._front
        prev = None
        curr = self._front

        def reverse_r_aux(curr, prev):
            # base case
            if curr is None:
                True

            # recursive call
            else:
                reverse_r_aux(curr._next, curr)
                # or if curr == self._rear (?)
                if curr._next is None:
                    self._front = curr
                curr._next = prev

            return

        reverse_r_aux(curr, prev)

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        lst = []
        curr = self._front
        prev = None

        while curr is not None:
            if curr._value not in lst:
                lst.append(curr._value)
                print(lst)

                # move to the next node and update prev
                temp = curr
                curr = curr._next
                prev = temp

            else:
                prev._next = curr._next
                self._count -= 1

                # move to next node without changing prev
                curr = curr._next

        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (iterative version)
        Use: b = lst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """

        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            target_node = other._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical

    def is_identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != other._count:
            print("here")
            identical = False

        else:
            print("passed")

            def is_identical_aux_r(source_node, target_node):
                # base cases
                if source_node is None:
                    identical = True

                elif source_node._value != target_node._value:
                    identical = False

                # recursive call
                else:
                    identical = is_identical_aux_r(
                        source_node._next, target_node._next)

                return identical

            identical = is_identical_aux_r(self._front, other._front)

        return identical

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        count = (self._count // 2) + (self._count % 2 > 0)
        print(count)
        i = 0
        target1 = List()
        target2 = List()

        while self._front is not None:
            if i < count:
                if target1._count == 0:
                    target1._front = self._front
                    self._front = self._front._next
                    target1._rear = target1._front
                    self._count -= 1
                    target1._count += 1
                else:
                    target1._rear._next = self._front
                    self._front = self._front._next
                    target1._rear = target1._rear._next
                    target1._rear._next = None
                    self._count -= 1
                    target1._count += 1

                i += 1

            else:
                if target2._count == 0:
                    target2._front = self._front
                    self._front = self._front._next
                    target2._rear = target2._front
                    self._count -= 1
                    target2._count += 1
                else:
                    target2._rear._next = self._front
                    self._front = self._front._next
                    target2._rear = target2._rear._next
                    target2._rear._next = None
                    self._count -= 1
                    target2._count += 1

                i += 1

        self._rear = None

        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source self is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()

        while self._front is not None:
            if target1._count == 0:
                target1._front = self._front
                self._front = self._front._next
                target1._rear = target1._front
                self._count -= 1
                target1._count += 1
            else:
                target1._rear._next = self._front
                self._front = self._front._next
                target1._rear = target1._rear._next
                target1._rear._next = None
                self._count -= 1
                target1._count += 1

            if self._front is not None:
                if target2._count == 0:
                    target2._front = self._front
                    self._front = self._front._next
                    target2._rear = target2._front
                    self._count -= 1
                    target2._count += 1
                else:
                    target2._rear._next = self._front
                    self._front = self._front._next
                    target2._rear = target2._rear._next
                    target2._rear._next = None
                    self._count -= 1
                    target2._count += 1

        self._rear = None

        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        even = List()
        odd = List()
        curr = self._front
        prev = None
        index = 0

        def split_alt_aux_r(index, curr, prev):

            # base case
            if curr is None:
                index = self._count

            # recursive call
            else:
                index = split_alt_aux_r(index, curr._next, curr) - 1
                # even
                if index % 2 == 0:
                    if even._count == 0:
                        even._front = curr
                        even._rear = even._front
                        even._count += 1
                        if prev is None:
                            self._front = None
                            self._count -= 1
                            self._rear = None
                        else:
                            self._rear = prev
                            prev._next = None
                            self._count -= 1
                    else:
                        curr._next = even._front
                        even._front = curr
                        even._count += 1
                        if prev is None:
                            self._front = None
                            self._count -= 1
                            self._rear = None
                        else:
                            self._rear = prev
                            prev._next = None
                            self._count -= 1
                else:
                    # odd
                    if odd._count == 0:
                        odd._front = curr
                        odd._rear = odd._front
                        odd._count += 1
                        if prev is None:
                            self._front = None
                            self._count -= 1
                            self._rear = None
                        else:
                            self._rear = prev
                            prev._next = None
                            self._count -= 1
                    else:
                        curr._next = odd._front
                        odd._front = curr
                        odd._count += 1
                        if prev is None:
                            self._front = None
                            self._count -= 1
                            self._rear = None
                        else:
                            self._rear = prev
                            prev._next = None
                            self._count -= 1
            return index

        split_alt_aux_r(index, curr, prev)

        return even, odd

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self.append(value)

            source1_node = source1_node._next
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        current = source1._front

        def intersection_r_aux(curr):
            # base case
            if curr is None:
                True
            # recursive call
            else:
                intersection_r_aux(curr._next)
                # gets value, searches both source2 and
                # self. If in former and not in ladder,
                # appends a node with same value as value
                value = curr._value
                srch_t = source2._linear_search_r(value)
                if srch_t[2] > -1:
                    srch = self._linear_search_r(value)
                    if srch[2] == -1:
                        self._front = _List_Node(value, self._front)
                        self._count += 1
                        if self._rear is None:
                            self._rear = self._front
            return

        intersection_r_aux(current)

        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                self.append(value)
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                self.append(value)

            source2_node = source2_node._next
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front
        source2_node = source2._front

        # works but BAD algo, fix to make Big-O better
        def union_r_aux(source1_node, source2_node):
            # base case / when at end of both linked lists
            if source1_node is None and source2_node is None:
                True

            # recursive call
            else:

                if source1_node is not None:
                    print("calling 1")
                    union_r_aux(source1_node._next, source2_node)
                    value = source1_node._value
                    srch = self._linear_search_r(value)
                    if srch[2] == -1:
                        self._front = _List_Node(value, self._front)
                        self._count += 1
                        if self._rear is None:
                            self._rear = self._front

                if source2_node is not None:
                    print("calling 2")
                    union_r_aux(source1_node, source2_node._next)
                    value = source2_node._value
                    srch = self._linear_search_r(value)
                    if srch[2] == -1:
                        self._front = _List_Node(value, self._front)
                        self._count += 1
                        if self._rear is None:
                            self._rear = self._front
            return

        union_r_aux(source1_node, source2_node)

        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish, self
        is empty.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        return

    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        # your code here
        return

    def _move_front(self, rs):
        """
        -------------------------------------------------------
        Moves the front node from the rs List to the front
        of the current List. Private helper method.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the rs List and
            its count is updated. The rs List front and count are updated.
        -------------------------------------------------------
        """
        assert rs._front is not None, \
            "Cannot move the front of an empty List"

        # your code here
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        while source1._front is not None or source2._front is not None:

            if source1._front is not None:

                # check for first insertion
                if self._count == 0:
                    self._front = source1._front
                    source1._front = source1._front._next
                    self._front._next = None
                    self._rear = self._front
                    self._count += 1
                    source1._count -= 1
                else:
                    # append at end of linked list
                    self._rear._next = source1._front
                    source1._front = source1._front._next
                    self._rear = self._rear._next
                    self._rear._next = None
                    self._count += 1
                    source1._count -= 1

            if source2._front is not None:

                # check for first insertion
                if self._count == 0:
                    self._front = source2._front
                    source2._front = source2._front._next
                    self._front._next = None
                    self._rear = self._front
                    self._count += 1
                    source2._count -= 1
                else:
                    # append at end of linked list
                    self._rear._next = source2._front
                    source2._front = source2._front._next
                    self._rear = self._rear._next
                    self._rear._next = None
                    self._count += 1
                    source2._count -= 1

        # update front and rear of empty lists
        source1._rear = None
        source2._rear = None

        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
