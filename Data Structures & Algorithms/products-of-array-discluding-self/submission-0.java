class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int zeros = 0;
        int zeroIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                zeros++;
                zeroIndex = i;
            } else {
            product *= nums[i];
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (zeros > 1) {
                nums[i] = 0;
            } else if (zeros == 1){
                if (i == zeroIndex) {
                    nums[i] = product;
                } else {
                    nums[i] = 0;
                }
            } else {
                    nums[i] = product / nums[i];
                }
        }
        return nums;
    }
}  
