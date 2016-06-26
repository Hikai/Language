package main

import (
	"fmt"
	"net/http"
	"os"
)

func web_get(str string) {
	if len(str) <= 0 {
		return
	}
	request, err := http.Get(str)
	if err != nil {
		fmt.Println("Error : ", err)
		os.Exit(1)
	}
	fmt.Println("Request : \n", request)
}

func main() {
	web_get("http://www.google.com")
}
