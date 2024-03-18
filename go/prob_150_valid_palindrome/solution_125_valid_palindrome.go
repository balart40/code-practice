package prob_150_valid_palindrome

import "unicode"

func isPalindrome(s string) bool {
	left := 0
	right := len(s) - 1
	for left < right {
		l := rune(s[left])
		r := rune(s[right])
		if !unicode.IsLetter(l) && !unicode.IsDigit(l) {
			left++
		} else if !unicode.IsLetter(r) && !unicode.IsDigit(r) {
			right--
		} else if unicode.ToLower(l) == unicode.ToLower(r) {
			left++
			right--
		} else {
			return false
		}
	}
	return true
}
