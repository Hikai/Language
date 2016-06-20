package main

import (
	"fmt"
)

func GuGu(a int) {
	for i := 1; i < 10; i++ {
		fmt.Println(a, "*", i, "=", a*i)
	}
}

func main() {
	var operand int
	fmt.Scanln(&operand)
	GuGu(operand)
}
