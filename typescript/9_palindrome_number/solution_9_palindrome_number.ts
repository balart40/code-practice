function isPalindrome(x: number): boolean {
    var num : string;
    var num_int: number;
    num = String(x);
    if (x < 0) {
        num.slice(1 , -1);
    }
    num_int = Number(num.split('').reverse().join(''));
    num_int = (x > 0) ? num_int : -1 * num_int;
    return x == num_int
};