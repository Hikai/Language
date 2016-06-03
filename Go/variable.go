package main

import (
	"fmt"
)

var a, b = 1, 2
var (
	c int32 = 3
	d int64 = 1000
)
const CONST = 3.14

func main() {
	e, f := "c3", "d4"
	fmt.Println(a, b, c, d, e, f)
	fmt.Println(CONST)
}
