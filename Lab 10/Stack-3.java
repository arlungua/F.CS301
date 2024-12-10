public class Stack {
    private int[] stack;
    private int size;
    private int capacity;
    private int potential; 

    public Stack() {
        stack = new int[1];
        size = 0;
        capacity = 1;
        potential = 0;
    }

    public void push(int item) {
        if (size >= capacity) {
            resize();
        }
        stack[size++] = item;
        potential++; 
    }

    public int pop() {
        if (size > 0) {
            potential--; 
            return stack[--size];
        }
        return -1;
    }

    private void resize() {
        capacity *= 2;
        int[] newStack = new int[capacity];
        System.arraycopy(stack, 0, newStack, 0, size);
        stack = newStack;
    }

    public int size() {
        return size;
    }

    public int getPotential() {
        return potential;
    }

    public static void main(String[] args) {
        Stack stack = new Stack();
        for (int i = 0; i < 10; i++) {
            stack.push(i);
            System.out.println(
                    "Stack size after pushing " + i + ": " + stack.size() + ", Potential = " + stack.getPotential());
        }

        for (int i = 0; i < 5; i++) {
            stack.pop();
            System.out.println(
                    "Stack size after popping " + i + ": " + stack.size() + ", Potential = " + stack.getPotential());
        }
    }
}
