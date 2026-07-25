class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (char c :  s.toCharArray()) {
            if (map.containsKey(c)) {
                map.put(c, map.get(c)+ 1);
            } else {
                map.put(c, 1);
            }
        }
        for (char c : t.toCharArray()) {
            if (!map.containsKey(c)) {
                return false;
            }
            if (map.get(c) > 0) {
                map.put(c, map.get(c) - 1);
            } else {
                return false;
            }
        }

        return true;
    }
}
