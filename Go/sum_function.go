package main

import (
	"fmt"
)

func sum(a, b int) (x int) {
	x = a + b
	return
}

func main() {
	fmt.Println(sum(1, 2))
}
