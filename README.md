# Week 3 Assignment: Grade Reporter & Bug Hunt

## Overview
This repository contains solutions for the PLP Python Week 3 assignment focusing on loops, conditional statements, running totals, and debugging techniques.

## Files Description
* `grade_reporter.py`: Processes student scores using a `for` loop and `if/elif/else` statements to assign letter grades, calculate pass/fail counts, and display the overall class average.
* `bug_hunt.py`: A debugged program that computes the sum of numbers from 1 to 5, featuring explanations for syntax, type, and logical errors.

## Reflection: Debugging Part B
The hardest bug to find in Part B was the logical error in the `while` loop condition (`count < 5`). Unlike the missing colon or string concatenation errors, this issue did not raise a runtime error message—the program executed smoothly but produced an incorrect result of `10` instead of `15`. I knew something was wrong because I manually calculated 1 + 2 + 3 + 4 + 5 = 15, and the code stopped running before adding the final number `5`. Changing the loop condition to `count <= 5` ensured that `5` was included in the total sum.
