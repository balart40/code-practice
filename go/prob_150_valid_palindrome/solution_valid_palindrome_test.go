package prob_150_valid_palindrome

import "testing"

// TestIsPalindrome tests various cases for the isPalindrome function.
func TestIsPalindrome(t *testing.T) {
	// Define test cases
	testCases := []struct {
		input    string
		expected bool
	}{
		{"", true},                               // Test empty string
		{"A man, a plan, a canal: Panama", true}, // Test valid palindrome with punctuation and spaces
		{"race a car", false},                    // Test non-palindrome
		{"racecar", true},                        // Test simple palindrome
		{"12321", true},                          // Test numeric palindrome
		{"12345", false},                         // Test non-palindrome numbers
		{"Madam", true},                          // Test case-insensitive palindrome
	}

	// Iterate through test cases
	for _, tc := range testCases {
		t.Run(tc.input, func(t *testing.T) {
			result := isPalindrome(tc.input)
			if result != tc.expected {
				t.Errorf("isPalindrome(%q) = %v; want %v", tc.input, result, tc.expected)
			}
		})
	}
}
