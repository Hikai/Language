// 150904 Reversing Prob2
package main

import
(
	"fmt"
)

func main() {
	ans := [7]int{54, 40, 41, 124, 62, 124, 95}
	var input, key [7]int
	var count int
	xorWonbon := [7]int{1104, 99, 103, 75, 115, 36, 84}
	// 1126, 75, 78, 55, 77, 88, 11
	for i := 0; i < 7; i++ {
		fmt.Print("Input : ")
		fmt.Scanf("%d\n", &input[i])
	}
	// Calculator to xor.
	for j := 0; j < 7; j++ {
		key[j] = xorWonbon[j] ^ input[j]
	}
	for k := 0; k < 7; k++ {
		if ans[k] == key[k] {
			count = count + 1
		}
	}
	// Clear
	if count == 7 {
		fmt.Print(": ")
		for l := 0; l < 7; l++ {
			fmt.Print(string(ans[l]))
		}
	}
}