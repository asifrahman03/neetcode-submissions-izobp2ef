class Solution {
    public String minWindow(String s, String t) {
        if(t.length() > s.length()){
            return "";
        }
        HashMap<Character, Integer> hM = new HashMap<>();
        for(int i=0; i<t.length(); i++){
            hM.put(t.charAt(i), hM.getOrDefault(t.charAt(i), 0)+1);
        }
        int need = hM.size();
        int minLen = s.length()+1;
        int start = 0;
        int have = 0;
        int l = 0; 
        for(int r = 0; r<s.length(); r++){
            if(hM.containsKey(s.charAt(r))){
                hM.put(s.charAt(r), hM.get(s.charAt(r))-1);
                if(hM.get(s.charAt(r)) == 0){
                    have++;
                }
                while(have == need){
                    if(r-l+1 < minLen){
                        minLen = r-l+1;
                        start = l;
                    }
                    char removed = s.charAt(l++);
                    if(hM.containsKey(removed)){
                        if(hM.get(removed) == 0){
                            have--;
                        }
                        hM.put(removed, hM.get(removed)+1);
                    }
                }
            }
        }
        if(minLen > s.length()){
            return "";
        }
        return s.substring(start,  start + minLen);
    }
}
