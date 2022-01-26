package poly

import (
	"fmt"
)

type Income interface {
	calculate() int
	source() string
}

type FixedBilling struct {
	ProjectName  string
	BiddedAmount int
}

type TimeAndMaterial struct {
	ProjectName string
	NoOfHours   int
	HourlyRate  int
}

func (fb FixedBilling) calculate() int {
	return fb.BiddedAmount
}

func (fb FixedBilling) source() string {
	return fb.ProjectName
}

func (tm TimeAndMaterial) calculate() int {
	return tm.NoOfHours * tm.HourlyRate
}

func (tm TimeAndMaterial) source() string {
	return tm.ProjectName
}

func CalculateNetIncome(ic []Income) {
	var netincome int = 0
	for _, income := range ic {
		fmt.Printf("Income From %s = $%d\n", income.source(), income.calculate())
		netincome += income.calculate()
	}
	fmt.Printf("Net income of organization = $%d", netincome)
}
