package main

import (
	"github.com/map34/gocurrency/cmd/package/comp"
	"github.com/map34/gocurrency/cmd/package/poly"
)

func ReturnSomeString() string {
	return "hello"
}

func main() {
	project1 := poly.FixedBilling{ProjectName: "Project 1", BiddedAmount: 5000}
	project2 := poly.FixedBilling{ProjectName: "Project 2", BiddedAmount: 10000}
	project3 := poly.TimeAndMaterial{ProjectName: "Project 3", NoOfHours: 160, HourlyRate: 25}
	incomeStreams := []poly.Income{project1, project2, project3}
	poly.CalculateNetIncome(incomeStreams)

	author1 := comp.Author{
		FirstName: "Naveen",
		LastName:  "Ramanathan",
		Bio:       "Golang Enthusiast",
	}
	blogPost1 := comp.BlogPost{
		Title:   "Inheritance in Go",
		Content: "Go supports composition instead of inheritance",
		Author:  author1,
	}
	blogPost1.Details()
}
