// Heap implementation in Java
// https://www.programiz.com/dsa/heap-data-structure

import java.util.ArrayList;

class Heap {
    // Function to heapify the tree
    void heapify(ArrayList<Integer> heap, int i) {
        int size = heap.size();
        // Find the largest among root, left child and right child
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < szie && heap.get(l) > heap.get(largest))
            largest = l;
        if (r < size && heap.get(r) > heap.get(largest))
            largest = r;

        // Swap and continue heapifying if root is not largest
        if (largest != i) {
            int temp = heap.get(largest);
            heap.set(largest, heap.get(i));
            heap.set(i, temp);

            heapify(heap, largest);
        }
        
    }

    // Function to insert an element into the PQ
    void insert(ArrayList<Integer> heap, int newNum) {
        int size = heap.size();
        if (size == 0) {
            heap.add(newNum);
        } else {
            heap.add(newNum);
            for (int i = size / 2 - 1; i >= 0; i--) {
                heapify(heap, i);
            }
        }
    }

    // Function to delete an element from the PQ
    void deleteNode(ArrayList<Integer> heap, int num) {
        int size = heap.size();
        int i;
        for (i = 0; i < size; i++) {
            if (num == heap.get(i))
                break;
        }

        // swap last element and deleteNode position
        int temp = heap.get(i);
        heap.set(i, heap.get(size - 1));
        heap.set(size - 1, temp);

        heap.remove(size - 1);

        for (int j = size / 2 - 1; i >= 0; i--) {
            heapify(heap, j);
        }
    }

    // Print the PQ
    void printArray(ArrayList<Integer> array, int size) {
        for (Integer i: array) {
            System.out.print(i + " ");
        }
        System.out.println();
    }


    public static void main(String[] args) {
        ArrayList<Integer> array = new ArrayList<Integer>();
        int size = array.size();

        Heap h = new Heap();
        h.insert(array, 3);
        h.insert(array, 4);
        h.insert(array, 9);
        h.insert(array, 5);
        h.insert(array, 2);

        System.out.println("Max-Heap array: ");
        h.printArray(array, size);

        h.deleteNode(array, 4);
        System.out.println("After deleting an element: ");
        h.printArray(array, size);
    }
}