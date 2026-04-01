class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();

        for(String str : strs){
            encoded.append(str.length());
            encoded.append('#');
            encoded.append(str);
        }

        return encoded.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int k = 0;
        for(int i=0; i<str.length(); i++){
            if(str.charAt(i) == '#'){
                String wrdLenStr = str.substring(k, i);
                int wrdLen = Integer.parseInt(wrdLenStr);
                String word = str.substring(i+1, i + 1+ wrdLen);
                res.add(word);
                k = i + 1 + wrdLen;
                i += wrdLen;
            }
        }
        return res;
    }
}
