/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let slow = 0;

  for (let i = 1; i < nums.length; i++) {
    if (nums[slow] !== nums[i]) {
      slow += 1;
      nums[slow] = nums[i];
    }
  }

  return slow + 1;
};
