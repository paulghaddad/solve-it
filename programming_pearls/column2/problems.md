## Problem 2:

- Start with unsorted sequential file
- Perform a linear scan through the file, and track which numbers have been seen
  - Seen numbers can be marked in a hash map, set or bitmap.
- Once a duplicate is encountered, return the number

Time: O(n)
Space: O(n)
where n = 4.3 billion

## Problem 6

We need to find a signature for each person's keycode, and then sort people's
name by keycode. In order to quickly find other names for a keycode combination,
we need a data storage setup as:

signature1 person1
signature1 person2
signature1 person3
signature2 person4
signature2 person5

The simplest way to generate the signature is to convert the * symbols to 0s,
and then treat the resulting number as a signature. 0 does not represent a
letter, so it's use allows us to convert the keycode to a real number.

We can use quicksort to sort this data, and then the directory provides quick
access for names when given a keycode through binary search.
