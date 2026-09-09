# Cricket Performance Calculator

runs = int(input("Enter runs scored: "))
balls = int(input("Enter balls faced: "))
runs_given = int(input("Enter runs conceded: "))
overs = float(input("Enter overs bowled: "))
catches = int(input("Enter catches: "))

# Calculate rates
strike_rate = (runs / balls) * 100
economy_rate = runs_given / overs

# Batting
if strike_rate >= 130:
    batting = "Excellent"
elif strike_rate >= 100:
    batting = "Good"
else:
    batting = "Poor"

# Bowling
if economy_rate <= 6:
    bowling = "Excellent"
elif economy_rate <= 8:
    bowling = "Good"
else:
    bowling = "Poor"

# Fielding
if catches >= 3:
    fielding = "Excellent"
elif catches >= 1:
    fielding = "Good"
else:
    fielding = "Poor"

# Overall
if batting == "Excellent" and bowling == "Excellent":
    overall = "Excellent"
elif batting == "Good" or bowling == "Good":
    overall = "Good"
else:
    overall = "Needs Improvement"

print("\nStrike Rate:", round(strike_rate, 2))
print("Economy Rate:", round(economy_rate, 2))
print("Batting:", batting)
print("Bowling:", bowling)
print("Fielding:", fielding)
print("Overall:", overall)
