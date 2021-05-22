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

	// Create tree root
	rootRecord := records[0]
	rootNode := Node{ID: rootRecord.ID}

	// Create map of Node pointers
	nodes := make(map[int]*Node)
	nodes[rootRecord.ID] = &rootNode

	// make sure there is a root node
	if _, found := nodes[rootRecord.Parent]; !found {
		return nil, fmt.Errorf("no root node")
	}

	// check for integrity of tree and cycles and build tree
	for i := 1; i < len(records); i++ {
		record := records[i]
		step := record.ID - records[i-1].ID

		if step != 1 {
			return nil, fmt.Errorf("duplicate nodes")
		}

		if _, found := nodes[record.Parent]; found == false {
			return nil, fmt.Errorf("cycle present")
		}

		node := Node{ID: record.ID}
		parent := nodes[record.Parent]
		parent.Children = append(parent.Children, &node)
		nodes[record.ID] = &node
	}

	return &rootNode, nil
}
