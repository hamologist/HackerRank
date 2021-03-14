package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func jumpingOnClouds(clouds []int) int {
	jumps := 0
	position := 0

	for position < len(clouds) - 1 {
		if position + 2 < len(clouds) && clouds[position + 2] == 0 {
			position += 2
			jumps++
		} else {
			position++
			jumps++
		}
	}

	return jumps
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	output, err := os.Create(os.Getenv("OUTPUT_PATH"))
	if err != nil {
		panic(err)
	}
	defer output.Close()

	temp, _, err := reader.ReadLine()
	if err != nil {
		panic(err)
	}

	n, err := strconv.Atoi(string(temp))
	if err != nil {
		panic(err)
	}

	cloudData, err := ioutil.ReadAll(reader)
	if err != nil {
		panic(err)
	}

	clouds := make([]int, n)
	for i, cloud := range strings.Split(strings.TrimSuffix(string(cloudData), "\n"), " ") {
		val, err := strconv.Atoi(cloud)
		if err != nil {
			panic(err)
		}
		clouds[i] = val
	}

	writer := bufio.NewWriter(output)
	fmt.Fprintf(writer, "%d\n", jumpingOnClouds(clouds))

	writer.Flush()
}
