package main

import (
	"fmt"
)

func main() {
	a := []int{1, 3, 5}
	fmt.Println(a)
	fmt.Println(a[0], a[1], a[2])
	fmt.Println(len(a))
	fmt.Println(a[0:1], a[:1])
	fmt.Println(a[1:])
}
