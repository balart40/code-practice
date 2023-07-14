package codepractice.esta.problem_1_two_sum;

import org.testng.Assert;
import org.testng.annotations.Test;


public class Solution_1_two_sumTest {
    private Solution_1_two_sum solution = new Solution_1_two_sum();

        @Test
        public void testTwoSum() {
            int[] nums = {2, 7, 11, 15};
            int target = 9;
            int[] expected = {0, 1};

            int[] actual = solution.twoSum(nums, target);

            Assert.assertEquals(actual, expected);
        }


}