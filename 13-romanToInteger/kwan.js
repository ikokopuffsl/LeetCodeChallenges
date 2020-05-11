/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  let roman = s.split("");
  let integer = 0;
  let iFlag = false;
  let xFlag = false;
  let cFlag = false;
  for (const [i, letter] of roman.entries()) {
    if (letter === "I") {
      integer += 1;
      iFlag = true;
    } else if (letter === "V") {
      if (iFlag) {
        integer += 3;
        iFlag = false;
      } else {
        integer += 5;
      }
    } else if (letter === "X") {
      if (iFlag) {
        integer += 8;
        iFlag = false;
      } else {
        integer += 10;
      }
      xFlag = true;
    } else if (letter === "L") {
      if (xFlag) {
        integer += 30;
        xFlag = false;
      } else {
        integer += 50;
      }
    } else if (letter === "C") {
      if (xFlag) {
        integer += 80;
        xFlag = false;
      } else {
        integer += 100;
      }
      cFlag = true;
    } else if (letter === "D") {
      if (cFlag) {
        integer += 300;
        cFlag = false;
      } else {
        integer += 500;
      }
    } else if (letter === "M") {
      if (cFlag) {
        integer += 800;
        cFlag = false;
      } else {
        integer += 1000;
      }
    }
  }
  return integer;
};
