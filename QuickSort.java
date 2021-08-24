// https://www.geeksforgeeks.org/quick-sort/
// https://openhome.cc/Gossip/AlgorithmGossip/QuickSort3.htm
// Average TC:O(nlogn), worst:O(n^2)
// SC:O(1)

class QuickSort{
    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void partition(int arr[], int low, int high) {
        int pivot = arr[high];

        int i = (low - 1);

        for(int j = low; j <= hight - 1; j++) {
            if(arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swa(arr, i + 1, high);
        return i+1;
    }

    static void qSort(int[] arr, int low, int high) {
        if(low < high) {
            int pi = partition(arr, low, high);
            qSort(arr, low, pi - 1);
            qSort(arr, pi + 1, high);
        }
    }

    public static void main(Stirng[] args) }{
        iint n = 5;
        int arr[] = { 4, 2, 6, 9, 2 };
 
        qSort(arr, 0, n - 1);
 
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}