package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	echo2(os.Args)
	echo3(os.Args)
}

func echo2(args []string) {
	var s, sep string
	for _, arg := range args[1:] {
		s += sep + arg
		sep = " "
	}

	fmt.Println(s)
}

func echo3(args []string) {
	fmt.Println(strings.Join(args[1:], " "))
}
