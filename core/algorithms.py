
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

    def algorithm(self, array, start=-1, end=-1, aux=[]):
        if (end == -1):
            start = 0
            end = len(array) - 1
            aux = array[:]

        if start == end:
            return

        mid = (start + end) // 2
        self.algorithm(aux, start, mid, array)
        self.algorithm(aux, mid+1, end, array)

        i = start
        j = mid + 1
        
        k = start
        
        while i <= mid and j <= end:
            if aux[i] <= aux[j]:
                array[k] = aux[i]
                self.states.append([array[:], k, i])

                k += 1
                i += 1
            else:
                array[k] = aux[j]
                self.states.append([array[:], k, j])

                k += 1
                j += 1

        while i <= mid:
            array[k] = aux[i]
            k += 1
            i += 1

        while j <= end:
            array[k] = aux[j]
            k += 1
            j += 1

        return self.states          

class QuickSort:
    def __init__(self):
        self.states = []

    def algorithm(self, array, start=-1, end=-1):
        if (end == -1):
            start = 0
            end = len(array) - 1

        if start < end:
            pivot = self.partition(array, start, end)

            self.algorithm(array, start, pivot - 1)
            self.algorithm(array, pivot + 1, end)

        return self.states
    
    def partition(self, array, start, end):
        pivot = array[end]

        i = start - 1

        for j in range(start, end):
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
                # self.states.append([array[:], i, j])


        array[i + 1], array[end] = array[end], array[i + 1]
        self.states.append([array[:], i+1, end])
        return i + 1