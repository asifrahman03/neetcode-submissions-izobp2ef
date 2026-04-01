class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<>();
        int total = 0;
        for(String c : tokens){
            if(!isOperator(c)){
                s.push(Integer.parseInt(c));
            }
            if(c.equals("+")){
                int denom = s.pop();
                int numer = s.pop();
                total += (numer+denom);
                s.push(total);
                total = 0;
            }
            else if(c.equals("-")){
                int denom = s.pop();
                int numer = s.pop();
                total += (numer-denom);
                s.push(total);
                total = 0;
            }
            else if(c.equals("*")){
                int denom = s.pop();
                int numer = s.pop();
                total += (numer*denom);
                s.push(total);
                total = 0;
            }
            else if(c.equals("/")){
                int denom = s.pop();
                int numer = s.pop();
                total += (numer/denom);
                s.push(total);
                total = 0;
            }
        }
        return s.peek();
    }
    private boolean isOperator(String c){
        return c.equals("+") || c.equals("*") || c.equals("-") || c.equals("/");
    }
}
