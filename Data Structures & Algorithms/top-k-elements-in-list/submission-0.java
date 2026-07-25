class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> intMap = new HashMap<Integer, Integer>();
        List<Integer>[] bucket = new List[nums.length + 1];
        int[] res = new int[k];
        // init the list in bucket 
        for ( int i = 0; i < bucket.length; i++) {
            bucket[i] = new ArrayList<Integer>();
        }
        // store the frequency in a hashmap 
        for (int num : nums) {
                intMap.put(num, intMap.getOrDefault(num , 0) + 1); 
        }
        // add the entrys freq into the bucket
        for (Map.Entry<Integer, Integer> entry : intMap.entrySet()) {
           bucket[entry.getValue()].add(entry.getKey());
        }
        //loop through bucket
        int index = 0;
        for (int i = bucket.length - 1; i > 0 && index < k; i--) {
            for (int n : bucket[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return res;
    }
}
