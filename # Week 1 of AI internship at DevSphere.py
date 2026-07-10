# Week 1 of AI internship at DevSphere
print("Portfolio Evaluator")

age = int(input("Please enter your age: "))
horizon = input("What is your horizon for investing? (short-term, medium-term, long-term): ").lower().strip()
risk_tolerance = input("What is your risk tolerance? (low, medium, high): ").lower().strip()
portfolio_type = ""

#total score possible is 9
total_score = 0

# Scoring based on age
if age < 30:
    total_score += 3
elif age < 50:
    total_score += 2
else:
    total_score += 1

# Scoring based on horizon
if horizon == "long-term":
    total_score += 3
elif horizon == "medium-term":
    total_score += 2
else:
    total_score += 1

# Scoring based on risk tolerance
if risk_tolerance == "high":
    total_score += 3
elif risk_tolerance == "medium":
    total_score += 2
else:
    total_score += 1

# Determine portfolio recommendation based on total score
if total_score > 7:
    portfolio_type = "Aggressive Portfolio"
elif total_score > 5:
    portfolio_type = "Balanced Portfolio"
else:
    portfolio_type = "Conservative Portfolio"

print(f"Based on your responses, your portfolio type is: {portfolio_type}")

