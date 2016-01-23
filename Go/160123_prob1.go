// Key is G-o

package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	key_back := [7]int{108, 108, 104, 105, 107, 97, 105}
	url := [6]int{113, 72, 86, 106, 112, 70}
	var result int;
	fmt.Println("Key : hiki + ?");
	if (len(os.Args) < 2) || (len(os.Args) != 8) {
		os.Exit(1);
	}
	for i := 0; i < 7; i++ {
		int_args, err := strconv.Atoi(os.Args[i + 1])
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
		if key_back[i] == int_args {
			result += 1;
		}
	}
	if result == 7 {
		fmt.Print("http://goo.gl/")
		for i := 0; i < 6; i++ {
			fmt.Print(string(url[i]))
		}
		fmt.Println("\nLanguage");
	}
}