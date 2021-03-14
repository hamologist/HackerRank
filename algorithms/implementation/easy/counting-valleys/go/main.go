package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
)

func countingValleys(path []byte) int {
	valleys := 0
	level := 0

	for _, step := range path {
		if step == 'U' {
			level++

			if level == 0 {
				valleys++
			}
		} else {
			level--
		}
	}

	return valleys
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	temp, _, err := reader.ReadLine()
	checkError(err)

	n, err := strconv.Atoi(string(temp))
	pathData := make([]byte, n)
	_, err = io.ReadFull(reader, pathData)
	checkError(err)

	result := countingValleys(pathData)

	writer := bufio.NewWriter(stdout)
	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
