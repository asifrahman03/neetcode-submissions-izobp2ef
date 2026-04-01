class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        Stack<Character> goodParen = new Stack<>();
        backTrack(0, 0, n, goodParen, res);
        return res;
    }
    private void backTrack(int openC, int closedC, int totalPairs, Stack<Character> stack, List<String> res){
        StringBuilder sB = new StringBuilder();
        if(openC == closedC && closedC + openC == (totalPairs*2)){
            for(char c : stack){
                sB.append(c);
            }
            res.add(sB.toString());
            return;
        }
        if(openC < totalPairs){
            stack.push('(');
            backTrack(openC+1, closedC, totalPairs, stack, res);
            stack.pop();
        }
        if(closedC < openC){
            stack.push(')');
            backTrack(openC, closedC+1, totalPairs, stack, res);
            stack.pop();
        }
    }
}
