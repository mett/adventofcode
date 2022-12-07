package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "sort"
)

func checkErr(err error) {
    if err != nil {
        fmt.Println(err)
    }
}

func MaxElf(v []int) (m int) {
    if len(v) > 0 {
        m = v[0]
    }
    for i := 1; i < len(v); i++ {
        if v[i] > m {
            m = v[i]
        }
    }
    return m
}

func sum(v []int) int {
    result := 0
    for _, v := range v {
        result += v
    }
    return result
}

func main() {
    readFile, err := os.Open("test-input.txt")
    checkErr(err)

    fileScanner := bufio.NewScanner(readFile)
    fileScanner.Split(bufio.ScanLines)
    elves := make([]int, 0)
    total := 0
    for fileScanner.Scan() {
        sCalorieCount := fileScanner.Text()
        if(sCalorieCount == "") {
            elves = append(elves, total)
            total = 0
            continue
        }
        calorieCount, err := strconv.Atoi(sCalorieCount)
        checkErr(err)
        total += calorieCount
        fmt.Println(total)
    }

    // max := MaxElf(elves)
    // fmt.Println("max: ", max)
    sort.Ints(elves)
    three := elves[len(elves)-3:]
    fmt.Println(sum(three))

    readFile.Close()
}
