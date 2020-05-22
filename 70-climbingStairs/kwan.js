/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  // 0 and 1 step are our base case
  // We can only get to step 0 one way, do nothing
  // and get to step 1 one way, take one step
  let uniqueStepsAtN = [1, 1];

  // Now we can always look back at 1 step and 2 steps to
  // see how many unique ways they had and add them up
  // This is the bottom up approach
  // https://www.youtube.com/watch?v=NFJ3m9a1oJQ
  let uniqueStepsAtN = [1, 1];

  for (let i = 2; i < n + 1; i++) {
    uniqueStepsAtN.push(uniqueStepsAtN[i - 1] + uniqueStepsAtN[i - 2]);
  }

  return uniqueStepsAtN[n];
};
