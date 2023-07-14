package codepractice.esta.problem_1_two_sum;

import java.util.HashMap;

public class Solution_1_two_sum {
    public int[] twoSum(int[] nums, int target) {
        int numToSearch = 0;
        int found = 0;
        HashMap<Integer, Integer> my_dict = new HashMap<Integer, Integer>();
        for( int i = 0; i < nums.length; i++) {
            numToSearch = target - nums[i];
            if (my_dict.containsKey(numToSearch)) {
                return new int[] { my_dict.get(numToSearch), i};
            }
            my_dict.put(nums[i], i);
        }
        return new int[] {};
    }
}