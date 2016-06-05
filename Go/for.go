package main

import (
	"fmt"
)

func main() {
	for i := 0; i < 3; i++ {
		fmt.Print(i, " ")
	}
	j := 0
	for j < 5 {
		fmt.Println(j)
		j++
	}
}
