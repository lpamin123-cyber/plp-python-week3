# Initial list of scores provided by the assignment
scores = [72, 45, 90, 61, 38]

# Initialize variables for running totals and pass/fail counts
total_score = 0
passed_count = 0
failed_count = 0

# Loop through each score to evaluate grades and update totals
for score in scores:
    # Determine the grade based on score conditions
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # Print the score and its assigned grade
    print(f"Score: {score} -> Grade: {grade}")

    # Track pass/fail statistics
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

    # Accumulate total score for average calculation
    total_score += score

# Calculate and round the average score
average = round(total_score / len(scores), 1)

# Print final summaries
print("\n--- Summary ---")
print(f"Learners Passed: {passed_count}")
print(f"Learners Failed: {failed_count}")
print(f"Average Score: {average}")
