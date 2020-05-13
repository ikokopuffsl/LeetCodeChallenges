/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if (s.iength === 0) return true;
    
    const comp = {
        "{": "}",
        "(": ")",
        "[": "]",
    };
    const stack = [];
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '{' || s[i] === '(' || s[i] === '[' ) {
            stack.push(s[i])
        }
        else if (s[i] === '}' || s[i] === ')' || s[i] === ']' ) {
            if (comp[stack[stack.length-1]] === s[i]) {
                stack.pop();
            }
            else {
                return false;
            }
        }
    }
    if (stack.length === 0) return true;
    return false;
};
