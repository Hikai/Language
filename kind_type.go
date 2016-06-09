package main

import (
	"fmt"
	"reflect"
)

func main() {
	a := "abcd"
	b := 0
	c := true
	fmt.Println(reflect.TypeOf(a))
	fmt.Println(reflect.TypeOf(b))
	fmt.Println(reflect.TypeOf(c))
}
