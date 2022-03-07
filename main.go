package main

import "fmt"

func main() {
	FizzBuzz(100)
}

func FizzBuzz(n int) {
	for i := 1; i <= n; i++ {
		fmt.Println(toFizzOrToBuzz(i))
	}
}

func toFizzOrToBuzz(n int) string {
	// or perhaps to FizzBuzz
	if n%3 == 0 && n%5 == 0 {
		return "FizzBuzz"
	} else if n%3 == 0 {
		return "Fizz"
	} else if n%5 == 0 {
		return "Buzz"
	}

	return fmt.Sprintf("%d", n)
}
