class Solution {

    public String encode(List<String> strs) {
        StringBuilder sB = new StringBuilder();
        for(int i=0; i<strs.size(); i++){
            sB.append(strs.get(i).length());
            sB.append('#');
            sB.append(strs.get(i));
        }
        return sB.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();

        for(int i=0; i<str.length(); i++){
            int j = i;
            while(str.charAt(i) != '#'){
                i++;
            }
            int wrdLen = Integer.parseInt(str.substring(j, i));
            String wrd = str.substring(i+1, i+wrdLen+1);
            res.add(wrd);
            i += wrdLen;
        }
        return res;
    }
}
