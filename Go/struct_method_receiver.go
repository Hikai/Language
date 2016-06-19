package main

import (
	"fmt"
)

const PI = 3.14

type circle struct {
	r int
	pi float64
}

func (c *circle) circle_area() float64 {
	return float64(c.r * c.r) * c.pi
}

func main() {
	a := circle {r: 3, pi: PI}
	fmt.Println(a.circle_area())
}
