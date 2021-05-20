package tree

import (
	"fmt"
	"sort"
)

// Record is a representation of tree nodes for the database
type Record struct {
	ID, Parent int
}

// Node is the recursive data type for the representation of the tree
type Node struct {
	ID       int
	Children []*Node
}

// Build constructs the recursive data type for the tree
func Build(records []Record) (*Node, error) {
	if len(records) == 0 {
		return nil, nil
	}

	// sort records by ID
	sort.Slice(records, func(i, j int) bool {
		return records[i].ID < records[j].ID
	})

	// check for integrity of tree
	for i := 0; i < len(records)-1; i++ {
		step := records[i+1].ID - records[i].ID

		if step != 1 {
			return nil, fmt.Errorf("duplicate nodes")
		}
	}

	// Create tree root
	rootRecord := records[0]
	rootNode := Node{ID: rootRecord.ID}

	// make sure there is a root node
	parent := findParent(&rootNode, rootRecord.Parent)
	if parent == nil {
		return nil, fmt.Errorf("no root node")
	}

	// make sure the root node doesn't have a parent
	if rootRecord.Parent > rootRecord.ID {
		return nil, fmt.Errorf("root node has a parent")
	}

	// check for any cycles
	seenIDs := make(map[int]bool)
	seenIDs[rootRecord.ID] = true
	for _, record := range records[1:] {
		if _, found := seenIDs[record.Parent]; found == false {
			return nil, fmt.Errorf("cycle present")
		}

		seenIDs[record.ID] = true
	}

	// build remaining nodes of tree
	for _, rec := range records[1:] {
		node := Node{ID: rec.ID}
		parent := findParent(&rootNode, rec.Parent)
		parent.Children = append(parent.Children, &node)
	}

	return &rootNode, nil
}

func findParent(root *Node, parentID int) *Node {
	if root.ID == parentID {
		return root
	}

	for _, child := range root.Children {
		if parent := findParent(child, parentID); parent != nil {
			return parent
		}
	}

	return nil
}
