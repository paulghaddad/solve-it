package tree

import "sort"

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

	rootRecord := records[0]
	rootNode := Node{ID: rootRecord.ID}

	for _, rec := range records[1:] {
		// create new node
		node := Node{ID: rec.ID}

		// insert into root's Children array
		rootNode.Children = append(rootNode.Children, &node)
	}

	return &rootNode, nil
}
