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
	sort.Slice(records, func(i, j int) bool {
		return records[i].ID < records[j].ID
	})

	nodes := make(map[int]*Node)

	for i, record := range records {
		if i != record.ID {
			return nil, fmt.Errorf("invalid tree")
		}

		if record.ID == 0 && record.Parent > 0 {
			return nil, fmt.Errorf("root node has parent")
		}

		node := Node{ID: record.ID}
		if record.Parent > 0 && record.Parent >= node.ID {
			return nil, fmt.Errorf("cycle present")
		}

		if parent, found := nodes[record.Parent]; found {
			parent.Children = append(parent.Children, &node)
		}

		nodes[record.ID] = &node
	}

	return nodes[0], nil
}
