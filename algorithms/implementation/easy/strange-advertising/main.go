package main

import (
    "fmt"
)

func main() {
    var n, ans int
    shares := 5
    fmt.Scanf("%d", &n)

    for i := 0; i < n; i++ {
        ans += (shares / 2)
        shares = (shares / 2) * 3
    }

    fmt.Println(ans)
}
