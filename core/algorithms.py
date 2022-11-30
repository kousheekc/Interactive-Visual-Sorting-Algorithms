
class SelectionSort:
    def __init__(self):
        pass

    def algorithm(self, array):
        for i in range(len(array)):
            min_idx = i
            for j in range(i+1, len(array)):
                if array[j] < array[min_idx]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
            yield [array[i], array[min_idx]]


class BubbleSort:
    def __init__(self):
        pass

    def algorithm(self, array):
        for i in range(len(array)):
            for j in range(len(array)-1-i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
            yield [array[j], array[j+1]]


class InsertionSort:
    def __init__(self):
        pass

    def algorithm(self, array):
        for i in range(len(array)):
            cursor = array[i]
            idx = i
            while idx > 0 and array[idx-1] > cursor:
                array[idx] = array[idx-1]
                idx -= 1
            array[idx] = cursor
            yield [array[idx], array[i]]


class MergeSort:
    def __init__(self):
        pass

    def algorithm(self, canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.algorithm(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, array[:mid])
        right = self.algorithm(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, array[mid:])
        return self.merge(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, left, right)

    def merge(self, canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self.update(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color)
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color)
        return result


class QuickSort:
    def __init__(self):
        pass
    
    def algorithm(self, canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, array=[], start=0, end=0):
        if array == []:
            array = self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, array,start,end)
            self.algorithm(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, array,start,pivot-1)
            self.algorithm(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color,array,pivot+1,end)

    def partition(self, canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, array, start, end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, array[i], array[j])
        return i