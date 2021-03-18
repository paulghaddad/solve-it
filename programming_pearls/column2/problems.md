## Problem 2:

- Start with unsorted sequential file
- Perform a linear scan through the file, and track which numbers have been seen
  - Seen numbers can be marked in a hash map, set or bitmap.
- Once a duplicate is encountered, return the number

Time: O(n)
Space: O(n)
where n = 4.3 billion
