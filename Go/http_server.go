package main

import (
    "fmt"
    "net/http"
)

func hello_world(writer http.ResponseWriter, request *http.Request) {
    fmt.Fprintf(writer, "Hello, World!")
}

func render_index(wrier http.ResponseWriter, p *Page) {
    t, _ := template.Parsefiles("index.html")
    t.Execute(w, p)
}

func main() {
    http.HandleFunc("/", hello_world)
    http.HandleFunc("/index", render_index)
    http.ListenAndServe(":80", nil)
}
