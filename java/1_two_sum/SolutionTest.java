public class SolutionTest {
    private Solution Solution = new Solution()

        @Test
        public void testTwoSum() {
            int[] nums = {2, 7, 11, 15};
            int target = 9;
            int[] expected = {0, 1};

            int[] actual = solution.twoSum(nums, target);

            Assert.assertEquals(actual, expected);
        }


}