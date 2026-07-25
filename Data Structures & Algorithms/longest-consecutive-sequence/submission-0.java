class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int max = 0;
        for ( int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0, end = nums.length - 1; i <= end; i++) {
            int currentMax = 1;
            int check = nums[i] - 1;
            while(map.containsKey(check) && i < end) {
                //find check index and move to the end--
                int checkIndex = map.get(check);
                //int temp = nums[checkIndex];
                nums[checkIndex] = nums[end];
                //nums[i] = temp;
                check--;
                currentMax++;
                end--;
            }
            check = nums[i] + 1;
            while(map.containsKey(check) && i < end) {
                //find check index and move to the end--
                int checkIndex = map.get(check);
                nums[checkIndex] = nums[end];
                end--;
                check++;
                currentMax++;
            }
            if (currentMax > max) {
                max = currentMax;
            }
        }
        return max;
    }
}
// checkIndex = 2
// currentMax = 2
// max = 1
// check = 7
// i = 1
// end = 4
// nums =[ 3, 6 ,7, 0, 7]
// map = [3:0 , 6:1 , 5:2, 0:3, 7:4]
