/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  digits[digits.length - 1] += 1;

  let i = 1;
  while (digits[digits.length - i] === 10) {
    digits[digits.length - i] = 0;
    i += 1;
    if (i > digits.length) {
      return [1].concat(digits);
    }
    digits[digits.length - i] += 1;
  }

  return digits;
};
