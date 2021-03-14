package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func checkMagazine(magazine, note []string) bool {
	passes := true
	magazineMap := make(map[string]int)

	for _, word := range magazine {
		magazineMap[word] += 1
	}

	for _, word := range note {
		if count, ok := magazineMap[word]; ok && count > 0 {
			magazineMap[word] -= 1
		} else {
			passes = false
			break
		}
	}

	return passes
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	output, _ := os.Create(os.Getenv("OUTPUT_PATH"))
	defer output.Close()

	_, _ = reader.ReadString('\n')

	data, _ := reader.ReadString('\n')
	magazine := strings.Split(strings.TrimSuffix(data, "\n"), " ")

	data, _ = reader.ReadString('\n')
	note := strings.Split(strings.TrimSuffix(data, "\n"), " ")

	passes := checkMagazine(magazine, note)
	writer := bufio.NewWriter(output)
	if passes {
		fmt.Fprint(writer, "Yes")
	} else {
		fmt.Fprint(writer, "No")
	}
	writer.Flush()
}
