# Interactive Visual Sorting Algorithms
Interactive and Visual representation of various sorting algorithms using Python and Tkinter

In this project, I create a user interface for an interactive, visual representation for various sorting algorithms. A GIF is attached below which gives a demo of the features that are available.

<img src="media/sorting.gif">

## About The Project
A sorting algorithm is used to rearrange the elements of an array according to a specific comparision operator. For example, when dealing with numbers, one might want to sort numbers in ascending or descending order. Being able to sort large amounts of data in an efficient manner is useful since other algorithms may depends on data that is sorted or simply for producing an output that is easy for humans to read.

Sorting a set of data can be defined by two conditions:
1. The output is ordered (small to big or big to small)
2. The output is a permutation of the unsorted data (no elements removed or added)

### Algorithms:
* **Selection Sort** O(n^2)
* **Bubble Sort** O(n^2)
* **Insertion Sort** O(n^2)
* **Merge Sort** O(nlog(n))
* **Quick Sort** O(nlog(n))

The package is designed in a way that more algorithms can be easily added. 

## Getting Started

### Prerequisites
* The program was created using **Python3.7**
* The UI was created using **Tkinter** (preinstalled with Python)

### Installation
To install the Interactive Visual Sorting Algorithms app, clone this repository using the following command:
```
git clone https://github.com/kousheekc/Interactive-Visual-Sorting-Algorithms.git
```

## Usage
To run the app open a terminal and navigate to the folder you just cloned and run the following command:
```
python3 -m app
```
Once the app is running the interface is self-explanatory. The features of the app are listed below.

### Features:
* **Generate random unsorted array**
* **Drop down menu to select the sorting algorithm**
* **Sort button** begins the sorting algorithm
* **Clear button** clears the screen
* **A visual representation** of the array and sorting process that updates in realtime.
* And finally no UI is complete without an inbuilt **dark color scheme** :smiley:


## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contact
Kousheek Chakraborty - kousheekc@gmail.com

Project Link: [https://github.com/kousheekc/Interactive-Visual-Sorting-Algorithms](https://github.com/kousheekc/Interactive-Visual-Sorting-Algorithms)

### Unsorted

<img src="media/unsorted.png" width=640>

### Sorted

<img src="media/sorted.png" width=640>

### Sorting an array of length 20 using bubble sort

<img src="media/sorting.gif">

### Big array

<img src="media/big_array.png" width=640>

### Dark mode

<img src="media/dark_mode.png" width=640>
