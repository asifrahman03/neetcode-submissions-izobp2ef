class Solution {
    List<String> res = new ArrayList<>();
    Stack<Character> goodParen = new Stack<>();
    public List<String> generateParenthesis(int n) {
        backTrack(0, 0, n);
        return res;
    }
    private void backTrack(int openC, int closedC, int totalPairs){
        StringBuilder sB = new StringBuilder();
        if(openC == closedC && closedC + openC == (totalPairs*2)){
            for(char c : goodParen){
                sB.append(c);
            }
            res.add(sB.toString());
            return;
        }
        if(openC < totalPairs){
            goodParen.push('(');
            backTrack(openC+1, closedC, totalPairs);
            goodParen.pop();
        }
        if(closedC < openC){
            goodParen.push(')');
            backTrack(openC, closedC+1, totalPairs);
            goodParen.pop();
        }
    }
}
