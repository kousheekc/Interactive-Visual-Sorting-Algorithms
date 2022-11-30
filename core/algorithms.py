
class SelectionSort:
    def __init__(self):
        pass

    def algorithm(self, array):
        states = []
        for i in range(len(array)):
            min_idx = i
            for j in range(i+1, len(array)):
                if array[j] < array[min_idx]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
            states.append([array[:], i, min_idx])
        return states

class BubbleSort:
    def __init__(self):
        pass

    def algorithm(self, array):
        states = []
        for i in range(len(array)):
            for j in range(len(array)-1-i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
            states.append([array[:], j, j+1])
        return states

class InsertionSort:
    def __init__(self):
        pass

    def algorithm(self, array):
        states = []
        for i in range(len(array)):
            cursor = array[i]
            idx = i
            while idx > 0 and array[idx-1] > cursor:
                array[idx] = array[idx-1]
                idx -= 1
            array[idx] = cursor
            states.append([array[:], idx, i])
        return states


class MergeSort:
    def __init__(self):
        self.states = []

    def algorithm(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]

            # Recursive call on each half
            self.algorithm(left)
            self.algorithm(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0
            
            # Iterator for the main list
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # The value from the left half has been used
                    array[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    array[k] = right[j]

                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k]=right[j]
                j += 1
                k += 1

            self.states.append([array[:], None, None])
            print(array)

        return self.states          

class QuickSort:
    def __init__(self):
        pass
    
    def algorithm(self, array, start=-1, end=-1):
        swaps = []
        print("yoo")
        if (end == -1):
            start = 0
            end = len(array) - 1

        if start < end:
            pivot, swap = self.partition(array, start, end)
            print(pivot)
            swaps.append(swap)

            self.algorithm(array, start, pivot-1)
            self.algorithm(array, pivot+1, end)
        else:
            print("returning")
            for swap in swaps:
                yield swap

    def partition(self, array, start, end):
        x = array[end]
        i = start-1
        swap = [None, None]
        for j in range(start, end+1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    swap = [array[i], array[j]]
        return i, swap