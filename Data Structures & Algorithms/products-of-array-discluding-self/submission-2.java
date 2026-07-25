class Solution {
    public int[] productExceptSelf(int[] nums) {
        HashMap<Integer, Integer> calc = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (!calc.containsKey(nums[i])) {
                int product = 1;
                for (int j = 0; j < nums.length; j++) {
                    if (j != i) {
                        product *= nums[j];
                    }
                }
                calc.put(nums[i], product);
            }
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = calc.get(nums[i]);
        }
       
        return nums;
    }
}  