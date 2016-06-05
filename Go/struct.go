package main

import (
	"fmt"
)

type Quad struct {
	a int
	b int
}

func main() {
	a := Quad{2, 2}
	fmt.Println(a.a, a.b)
	a.a = 4
	a.b = 6
	fmt.Println(a.a, a.b)
	b := &a
	fmt.Println(b)
}
