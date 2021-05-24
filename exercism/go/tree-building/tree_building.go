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

	for i, r := range records {
		node := Node{ID: r.ID}
		if i != r.ID || r.ID == 0 && r.Parent > 0 || r.Parent > 0 && r.Parent >= node.ID {
			return nil, fmt.Errorf("not in sequence or has bad parent")
		}

		if r.ID != 0 {
			parent := nodes[r.Parent]
			parent.Children = append(parent.Children, &node)
		}

		nodes[r.ID] = &node
	}

	return nodes[0], nil
}
