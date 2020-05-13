/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function (l1, l2) {
  if (l1 === null && l2 === null) return null;
  if (l1 === null) return l2;
  if (l2 === null) return l1;

  let result;
  let train;
  if (l1.val < l2.val) {
    train = l1;
    l1 = l1.next;
  } else {
    train = l2;
    l2 = l2.next;
  }
  result = train;
  while (l1 && l2) {
    if (l1.val < l2.val) {
      train.next = l1;
      l1 = l1.next;
    } else {
      train.next = l2;
      l2 = l2.next;
    }
    train = train.next;
  }

  train.next = l1 || l2;

  return result;
};
