class Solution {

    public String encode(List<String> strs) {
        StringBuilder merged = new StringBuilder("");
        for(String s : strs){
            merged.append(s.length());
            merged.append('#');
            merged.append(s);
        }
        return merged.toString();
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') j++;

            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1 + length;
            strs.add(str.substring(j + 1, i));
        }
        return strs;
    }
}
