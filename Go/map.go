package main

import (
	"fmt"
)

func main() {
	a := make(map[string]int)
	a["a"] = 1
	a["b"] = 2
	fmt.Println(a, len(a))
	fmt.Println(a["a"], a["b"])
	delete(a, "a")
	fmt.Println(a, len(a))
}
