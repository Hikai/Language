package main

import (
	"fmt"
	"time"
)

func Gugu(operand int) {
	for i := 1; i < 10; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(operand, " * ", i, " = ", operand*i)
	}
}

func main() {
	go Gugu(2)
	Gugu(5)
}
