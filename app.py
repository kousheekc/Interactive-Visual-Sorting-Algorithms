from core.algorithms import SelectionSort, BubbleSort, InsertionSort, MergeSort, QuickSort
from ui.interface import Interface

def main():
    algos = {"Selection Sort": SelectionSort(), "Bubble Sort": BubbleSort(), "Insertion Sort": InsertionSort(), "Merge Sort": MergeSort(), "Quick Sort": QuickSort()}
    interface = Interface(algos)

    loop_active = True

    while loop_active:
        interface.update()


if __name__ == '__main__':
    main()