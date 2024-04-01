from fractions import Fraction

# Define the faces of the dice
die_faces = [1, 2, 3, 4, 5, 6]

# Initialize a dictionary to store the count of occurrences for each sum
sum_occurrences = {i: 0 for i in range(2, 13)}  # Sums range from 2 to 12
sum_combinations = {i: [] for i in range(2, 13)}  # Store combinations for each sum

# Calculate the distribution and total combinations
total_combinations = 0
for roll_a in die_faces:
    for roll_b in die_faces:
        total_combinations += 1
        roll_sum = roll_a + roll_b
        sum_occurrences[roll_sum] += 1
        sum_combinations[roll_sum].append((roll_a, roll_b))

# Calculate and display the probability of each possible sum occurring
print("Probability of all possible sums:")
for sum_value, occurrences in sum_occurrences.items():
    probability = Fraction(occurrences, total_combinations)
    decimal_probability = occurrences / total_combinations
    print(f"P(Sum = {sum_value}) = {probability} = {decimal_probability:.4f}")

# Display the combinations for each sum
print("\nCombinations for each sum:")
for sum_value, combinations in sum_combinations.items():
    print(f"Sum = {sum_value}: {combinations}")