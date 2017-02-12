package main

import (
    "fmt"
)

func main() {
    var n, sock, ans int
    var c = make(map[int]int)
    fmt.Scanf("%d", &n)

    for i := 0; i < n; i++ {
        fmt.Scanf("%d", &sock)
        c[sock]++
    }

    for _, v := range c {
        ans += v / 2
    }

    fmt.Println(ans)
}
