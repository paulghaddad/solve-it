package linkedlist

import (
	"errors"
)

// ErrEmptyList is the error when performing invalid operations on empty lists
var ErrEmptyList error = errors.New("cannot perform operation on empty list")

// List is the type implementing a linked list
type List struct {
	head *Node
	tail *Node
}

// Node is the type implementing a linked list node
type Node struct {
	Val  interface{}
	prev *Node
	next *Node
}

// NewList is the factory function for creating a new linked list
func NewList(args ...interface{}) *List {
	var l List

	for _, a := range args {
		l.PushBack(a)
	}

	return &l
}

// Next is the pointer to the next node
func (e *Node) Next() *Node {
	return e.next
}

// Prev is the pointer to the previous node
func (e *Node) Prev() *Node {
	return e.prev
}

// PushFront inserts value at front
func (l *List) PushFront(v interface{}) {
	if l.head == nil {
		newNode := &Node{v, nil, nil}
		l.head = newNode
		l.tail = newNode
		return
	}

	head := l.head
	newNode := &Node{v, nil, head}
	head.prev = newNode
	l.head = newNode
}

// PushBack inserts value at back
func (l *List) PushBack(v interface{}) {
	tail := l.tail
	node := Node{v, nil, nil}

	if tail == nil {
		l.head = &node
		l.tail = &node
		return
	}

	node.prev = tail
	tail.next = &node
	l.tail = &node
}

// PopFront removes value at front
func (l *List) PopFront() (interface{}, error) {
	if l.head == nil {
		return nil, ErrEmptyList
	}

	headNode := l.head
	nextNode := headNode.next
	if nextNode == nil {
		l.head = nil
		l.tail = nil
		return headNode.Val, nil
	}

	nextNode.prev = nil
	l.head = nextNode

	return headNode.Val, nil
}

// PopBack removes value at back
func (l *List) PopBack() (interface{}, error) {
	if l.tail == nil {
		return nil, ErrEmptyList
	}

	tailNode := l.tail
	prevNode := tailNode.prev
	if prevNode == nil {
		l.head = nil
		l.tail = nil
		return tailNode.Val, nil
	}

	prevNode.next = nil
	l.tail = prevNode

	return tailNode.Val, nil
}

// Reverse reverses the linked list
func (l *List) Reverse() *Node {
	if l.head == nil {
		return l.head
	}

	prevNode := l.First()
	l.tail = prevNode
	nextNode := prevNode.next
	prevNode.next = nil
	prevNode.prev = nextNode

	for nextNode != nil {
		tmp := nextNode.next
		nextNode.next = prevNode
		nextNode.prev = tmp
		prevNode = nextNode
		nextNode = nextNode.prev
	}

	l.head = prevNode

	return prevNode
}

// First is the pointer to the first node (head)
func (l *List) First() *Node {
	return l.head
}

// Last is the pointer to the last node (tail)
func (l *List) Last() *Node {
	return l.tail
}
