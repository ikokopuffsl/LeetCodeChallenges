/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let number = x.toString();
  let isNegative = number.search("-") >= 0 ? true : false;
  if (isNegative) {
    number = number.substring(1, number.length);
  }
  let numberArray = number.split("");

  let reversed = numberArray.reverse().join("");

  let result;
  if (isNegative) {
    result = reversed * -1;
  } else {
    result = reversed;
  }

  if (Math.abs(result) > 2147483648) {
    return 0;
  } else {
    return result;
  }
};
