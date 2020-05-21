/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  if (nums.length === 0) return 0;
  // let total = [nums[0]]
  // for (let i = 1; i < nums.length; i++) {
  //     if (nums[i] > (total[i-1]+nums[i]) {
  //         total.push(nums[i])
  //     }
  //     else{
  //         total.push((total[i-1] + nums[i]))
  //     }
  // }

  // let max = nums[0]
  // for (let i = 1; i< nums.length; i++) {
  //     if (max <= nums[i]) {
  //        max = nums[i]
  //     }
  //     else if ((max+nums[i]) >= max) {
  //         max += nums[i]
  //     }
  //     else {
  //         // Do nothing
  //     }
  // }

  // for (let i = 1; i < nums.length; i++) {
  //   nums[i] = Math.max(nums[i], nums[i] + nums[i - 1]);
  //     console.log(nums[i])
  // }
  // return Math.max(...nums)

  let max_array = [nums[0]];
  for (let i = 1; i < nums.length; i++) {
    if (max_array[i - 1] + nums[i] < nums[i]) {
      max_array.push(nums[i]);
    } else {
      max_array.push(nums[i] + max_array[i - 1]);
    }
  }
  return Math.max(...max_array);
};
