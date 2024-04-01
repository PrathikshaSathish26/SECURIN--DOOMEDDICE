# Define the faces of the dice
die_faces = [1, 2, 3, 4, 5, 6]

# Initialize a 6x6 matrix with zeros to represent the distribution
distribution = [[0] * 6 for _ in range(6)]

# Total combinations counter
total_combinations = 0

# Calculate the distribution and total combinations
for roll_a in die_faces:
    for roll_b in die_faces:
        # Update the distribution matrix
        distribution[roll_a - 1][roll_b - 1] += 1
        # Increment total combinations counter
        total_combinations += 1

# Display the total combinations
print("Total combinations possible:", total_combinations)

# Display the distribution as a 6x6 matrix
print("Distribution of all possible combinations:")
print("0 1  2  3  4  5  6")
for i in range(6):
    print(i + 1, end=" ")
    for j in range(6):
        print("{:2}".format(distribution[i][j]), end=" ")
    print()
