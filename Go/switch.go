package main

import (
	"fmt"
)

func main() {
	a := 1
	switch a {
	case 1 :
		fmt.Println("!")
	case 2 :
		fmt.Println("@")
	default :
		fmt.Println("?")
	}	
}
