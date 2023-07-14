package codepractice.esta.problem_9_palindrome_number;

public class Solution_9_palindrome_number {
    public boolean isPalindrome(int x) {
        String xs = String.valueOf(x);
        int left = 0;
        int right = xs.length() - 1;
        while( left < right ) {
            if( xs.charAt(left) != xs.charAt(right)) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
}
