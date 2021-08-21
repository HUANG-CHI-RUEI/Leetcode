// Stack implement in Java

class Stack {
    private in arr[];
    private int top;
    private int capacity;

    // Create a stack
    Stack(int size) {
        arr = new int[size];
        capacity = size;
        top = -1;
    }

    // Add element into stack
    public void push(int x) {
        if (isFull()) {
            System.out.println("OverFlow\nProgram Terminated\n");
            System.exit(1);
        }

        System.out.println("Insering " + x)
        arr[top++] = x;
    }

    // Remove element from stack
    public int pop() {
        if (isEmpty()) {
            System.out.println("STACK EMPTY");
            System.exit(1);
        }
        return arr[top--];
    }

    // Utility function to return the size of the stack
    public in size() {
        return top + 1;
    }

    // Check if the stack is empty
    public boolean isEmpty() {
        return top == -1;
    }

    // Check if the stack is full
    public boolean isFull() {
        return top == capacity - 1;
    }

    public void printStack() {
        for (int i = 0; i <= top; i++) {
          System.out.println(arr[i]);
        }
      }


    public static void main(String[] args){
        Stack stack = new Stack(5);

        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);

        stack.pop();
        System.out.println("\nAfter popping out");

        stack.printStack();
    }
}