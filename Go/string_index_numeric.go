package main

import (
	"fmt"
)

func main() {
	a := "abcd"
	for i := 0; i < len(a); i++ {
		fmt.Printf("%c ", a[i])
		fmt.Println(a[i])
	}
}
