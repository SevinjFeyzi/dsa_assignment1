class MinHeap:
    def __init__(self, arr=[]):
        """
        Initializes a MinHeap with an optional initial array.

        Parameters:
        - arr (list): An optional initial array. Default is an empty list.
        """
        self.heap = []
        for element in arr:
            self.insert(element)

    def insert(self, element):
        """
        Inserts an element into the MinHeap.

        Parameters:
        - element: The element to be inserted.
        """
        self.heap.append(element)
        self._heapify_up()

    def get_min(self):
        """
        Returns the smallest value in the MinHeap without altering the data structure.

        Returns:
        - The smallest value in the MinHeap, or None if the heap is empty.
        """
        if not self.is_empty():
            return self.heap[0]
        return None

    def extract_min(self):
        """
        Removes and returns the smallest value from the MinHeap.

        Returns:
        - The smallest value in the MinHeap, or None if the heap is empty.
        """
        if not self.is_empty():
            if len(self.heap) == 1:
                return self.heap.pop()
            else:
                min_val = self.heap[0]
                self.heap[0] = self.heap.pop()
                self._heapify_down()
                return min_val
        return None

    def is_empty(self):
        """
        Checks if the MinHeap is empty.

        Returns:
        - True if the MinHeap is empty, False otherwise.
        """
        return len(self.heap) == 0

    def __len__(self):
        """
        Returns the number of values stored in the MinHeap.

        Returns:
        - The number of values in the MinHeap.
        """
        return len(self.heap)

    def _heapify_up(self):
        """
        Restores the heap property by moving the last element up to its correct position.
        """
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        """
        Restores the heap property by moving the first element down to its correct position.
        """
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
