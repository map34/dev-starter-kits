package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestReturnSomeString(t *testing.T) {
	assert.Equal(t, "hello", ReturnSomeString(), "Same string")
}
