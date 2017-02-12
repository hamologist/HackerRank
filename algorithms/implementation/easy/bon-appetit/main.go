package main

import (
    "fmt"
)

func main() {
    var n, k, b, actual int

    fmt.Scanf("%d %d", &n, &k)
    c := make([]int, n)
    for i := range c {
        fmt.Scanf("%d", &c[i])
    }
    fmt.Scanf("%d", &b)

    for i := range c {
        if i != k {
            actual += c[i]
        }
    }
    actual /= 2

    if actual == b {
        fmt.Println("Bon Appetit")
    } else {
        fmt.Println(b - actual)
    }
}
