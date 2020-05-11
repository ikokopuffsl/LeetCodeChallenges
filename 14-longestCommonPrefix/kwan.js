/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  if (strs.length === 0) return "";

  const firstWord = strs[0];
  let commonPrefix = "";
  for (let i = 0; i < firstWord.length; i++) {
    for (let j = 1; j < strs.length; j++) {
      if (strs[j][i] !== firstWord[i]) {
        return commonPrefix;
      }
    }
    commonPrefix += firstWord[i];
  }
  return commonPrefix;
};
