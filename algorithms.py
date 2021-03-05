import random
import time

class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(600), 600)
        self.name = name

    def reset(self, canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color):
        self.array = random.sample(range(600), 600)
        self.update(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color)

    def update(self, canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, swap1=None, swap2=None, ):
        canvas.configure(bg=mainScreenColor)
        canvas.delete("all")

        k = int(canvasWidth/len(self.array))

        for i in range(len(self.array)):
            colour = linesColor

            if swap1 == self.array[i]:
                colour = swap1Color
            elif swap2 == self.array[i]:
                colour = swap2Color

            canvas.create_rectangle(i*k, self.array[i], i*k+k, canvasHeight, fill=colour)
        
        canvas.pack()  
        canvas.update()


class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self, canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.update(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, self.array[i], self.array[min_idx])


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self, canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, self.array[j], self.array[j+1])


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self, canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color):
        for i in range(len(self.array)):
            cursor = self.array[i]
            idx = i
            while idx > 0 and self.array[idx-1] > cursor:
                self.array[idx] = self.array[idx-1]
                idx -= 1
            self.array[idx] = cursor
            self.update(canvas, mainScreenColor, linesColor, canvasHeight, canvasWidth, swap1Color, swap2Color, self.array[idx], self.array[i])


class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

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


class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

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