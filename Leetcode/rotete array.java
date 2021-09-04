// https://www.geeksforgeeks.org/array-rotation/

// METHOD 2 (Rotate one by one)
// TC:O(n*d)
// SC:O(1)

class RotateArray {

    void leftRotate(int[] arr, int d, int n) {
        for (int i = 0; i < d; i++) {
            leftRotateByOne(arr, n);
        }
    }

    void leftRotateByOne(int[] arr, int n) {
        int temp = arr[0];
        for (int i = 0; i < n-1; i++) {
            arr[i] = arr[i+1];
        }
        arr[n-1] = temp;
    }

    void printArray(int[] arr, int n) {
        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void main(String[] args)
    {
        RotateArray rotate = new RotateArray();
        int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
        rotate.leftRotate(arr, 2, 7);
        rotate.printArray(arr, 7);
    }
}


// https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
// Method 4 (The Reversal Algorithm) :
// TC:O(n)
// SC:O(1)

class LeftRotate {

    static void leftRotate(int[] arr, int d) {
        if (d == 0) return;

        d = d % arr.length;

        reverseArray(arr, 0, d-1);
        reverseArray(arr, d+1, arr.length - 1);
        reverseArray(arr, 0, arr.length - 1);
    }

    static void reverseArray(int[] arr, int start, int end) {
        int temp;
        while(start < end) {
            tmep = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }


    static void printArray(int arr[])
    {
        for (int i = 0; i < arr.length; i++)
            System.out.print(arr[i] + " ");
    }

    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
        int d = 2;
  
        leftRotate(arr, d); // Rotate array by d
        printArray(arr);
    }
}