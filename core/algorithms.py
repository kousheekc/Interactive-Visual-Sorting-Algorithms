
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

            self.algorithm(left)
            self.algorithm(right)

            i = 0
            j = 0
            
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k]=right[j]
                j += 1
                k += 1

            self.states.append([array[:], None, None])

        return self.states          

class QuickSort:
    def __init__(self):
        self.states = []

    def algorithm(self, array, low=-1, high=-1):
        if (high == -1):
            low = 0
            high = len(array) - 1

        if low < high:
            pivot = self.partition(array, low, high)

            self.algorithm(array, low, pivot - 1)
            self.algorithm(array, pivot + 1, high)

        return self.states
    
    def partition(self, array, low, high):
        pivot = array[high]

        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
                # self.states.append([array[:], i, j])


        array[i + 1], array[high] = array[high], array[i + 1]
        self.states.append([array[:], i+1, high])
        return i + 1