class MinStack {
    Stack<Integer> stack;
    Stack<Integer> minS;
    public MinStack() {
        stack = new Stack<>();
        minS = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if(minS.empty()){
            minS.push(val);
        }else if(minS.peek() >= val){
            minS.push(val);
        }
    }
    
    public void pop() {
        int removed = stack.pop();
        if(minS.peek() == removed){
            minS.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minS.peek();
    }
}
