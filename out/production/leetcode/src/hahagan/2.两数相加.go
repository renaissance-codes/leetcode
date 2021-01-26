/*
 * @lc app=leetcode.cn id=2 lang=golang
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head := new(ListNode)
	head.Val = 0
	head.Next = nil
	p := head
	for l1 != nil && l2 != nil {
		tmp := l1.Val + l2.Val + head.Val
		head.Val = tmp / 10
		r := new(ListNode)
		r.Next = nil
		r.Val = tmp % 10
		p.Next = r
		p = r
		l1 = l1.Next
		l2 = l2.Next
	}

	for l1 != nil {
		r := new(ListNode)
		tmp := l1.Val + head.Val
		r.Val = tmp % 10
		p.Next = r
		head.Val = tmp / 10
		l1 = l1.Next
		p = r

	}

	for l2 != nil {
		r := new(ListNode)
		tmp := l2.Val + head.Val
		r.Val = tmp % 10
		p.Next = r
		head.Val = tmp / 10
		l2 = l2.Next
		p = r
	}

	if head.Val > 0 {
		r := new(ListNode)
		r.Val = head.Val
		p.Next = r
	}

	return head.Next

}

// @lc code=end

