class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str : strs){
            sb.append(str.length());
            sb.append('#');
            sb.append(str);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        int r = 0;
        while(r < str.length()){
            if(str.charAt(r) == '#'){
                String clen = str.substring(i, r);
                int len = Integer.parseInt(clen);
                String word = str.substring(r+1, r+len+1);

                res.add(word);
                i = r + len + 1;
                r += len;
            }
            r++;
        }
        return res;
    }
}
