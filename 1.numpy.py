import numpy as np

# Generate random scores for 50 students
scores = np.random.randint(0, 100, size=50)

print("Student Scores:")
print(scores)

mean_score = np.mean(scores)
median_score = np.median(scores)
highest_score = np.max(scores)
lowest_score = np.min(scores)
std_deviation = np.std(scores)

print("\n----- Statistics -----")
print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Standard Deviation:", std_deviation)

p25 = np.percentile(scores, 25)
p75 = np.percentile(scores, 75)

print("25th Percentile:", p25)
print("75th Percentile:", p75)

fail_students = scores[scores < 40]
distinction_students = scores[scores > 85]

print("\n----- Failed Students (<40) -----")
print(fail_students)

print("\n----- Distinction Students (>85) -----")
print(distinction_students)

normalized_scores = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))

print("\n----- Normalized Scores -----")
print(normalized_scores)

reshaped_scores = scores.reshape(5, 10)

print("\n----- Reshaped Scores (5x10) -----")
print(reshaped_scores)

row_averages = np.mean(reshaped_scores, axis=1)

print("\n----- Subject-wise Average -----")
print(row_averages)

theory = np.random.randint(0, 100, size=50)
practical = np.random.randint(0, 100, size=50)

weighted_scores = (0.4 * theory) + (0.6 * practical)

print("\n----- Theory Scores -----")
print(theory)

print("\n----- Practical Scores -----")
print(practical)

print("\n----- Weighted Final Scores -----")
print(weighted_scores)