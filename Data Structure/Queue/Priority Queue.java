// Priority Queue implementation in Java
// https://www.programiz.com/dsa/priority-queue

import java.util.ArrayList;

class Heap {
    // Function to heapify the tree
    void heapify(ArrayList<Integer> pq, int i) {
        int size = pq.size();
        // Find the largest among root, left child and right child
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < szie && pq.get(l) > pq.get(largest))
            largest = l;
        if (r < size && pq.get(r) > pq.get(largest))
            largest = r;

        // Swap and continue heapifying if root is not largest
        if (largest != i) {
            int temp = pq.get(largest);
            pq.set(largest, pq.get(i));
            pq.set(i, temp);

            heapify(pq, largest);
        }
        
    }

    // Function to insert an element into the PQ
    void insert(ArrayList<Integer> pq, int newNum) {
        int size = pq.size();
        if (size == 0) {
            pq.add(newNum);
        } else {
            pq.add(newNum);
            for (int i = size / 2 - 1; i >= 0; i--) {
                heapify(pq, i);
            }
        }
    }

    // Function to delete an element from the PQ
    void deleteNode(ArrayList<Integer> pq, int num) {
        int size = pq.size();
        int i;
        for (i = 0; i < size; i++) {
            if (num == pq.get(i))
                break;
        }

        // swap last element and deleteNode position
        int temp = pq.get(i);
        pq.set(i, pq.get(size - 1));
        pq.set(size - 1, temp);

        pq.remove(size - 1);

        for (int j = size / 2 - 1; i >= 0; i--) {
            heapify(pq, j);
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