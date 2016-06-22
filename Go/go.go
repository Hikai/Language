package main

import (
	"fmt"
)

func print(arg string) {
	for i := 0; i < 5; i++ {
		fmt.Println(arg)
	}
}

func main() {
	go print("a")
	print("b")
}
