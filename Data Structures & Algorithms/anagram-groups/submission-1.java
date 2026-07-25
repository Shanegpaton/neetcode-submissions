class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        ArrayList<List<String>> toReturn = new ArrayList<List<String>>(strs.length);
        for (String string : strs) {
            int[] array = new int[26];
            char[] charArray = string.toCharArray();
            for (char c : charArray) {
                //convert c to number 1-26
                array[c - 'a']++; 
            }
            if (map.containsKey(Arrays.toString(array))) {
                // add to list at inded in char array
                toReturn.get(map.get(Arrays.toString(array))).add(string);
            } else {
                ArrayList<String> subArray = new ArrayList<String>();
                subArray.add(string);
                toReturn.add(subArray);
                map.put(Arrays.toString(array), toReturn.size() - 1);
            }
            // hash the array into a key

        }
    return toReturn;

    }
}
