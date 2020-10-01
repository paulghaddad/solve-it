package bob

import (
	"fmt"
	"testing"
)

func TestBob(t *testing.T) {
	var tests = []struct {
		remark string
		want   string
	}{
		{"How are you?", "Sure."},
		{"STOP DOING THAT!", "Whoa, chill out!"},
		{"WHY ARE YOU DOING THAT?", "Calm down, I know what I'm doing!"},
		{"", "Fine. Be that way!"},
		{"You are Bob.", "Whatever."},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%s,%s", tt.remark, tt.want)

		t.Run(testname, func(t *testing.T) {
			response := Hey(tt.remark)

			if response != tt.want {
				t.Errorf("Hey(%s) = %s; want: %s", tt.remark, response, tt.want)
			}
		})
	}
}
