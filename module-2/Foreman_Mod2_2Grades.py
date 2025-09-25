#Natasha Foreman
#Module 2.2 Assignment
#Calculate the average of a list of scores and assign a letter grade

demo_mode = True

def compute_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("Scores list cannot be empty.")
    divisor = len(scores)
    return round(sum(scores) / divisor, 2)

def letter_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def main():
    if demo_mode:
        scores = [88, 92, 79, 95]
    else:
        raw = input("Enter comma-separated scores (e.g., 88,92,79,95): ")
        try:
            scores = [float(x.strip()) for x in raw.split(",") if x.strip() != ""]
        except ValueError:
            print("Please enter numeric values separated by commas.")
            return

    avg = compute_average(scores)
    grade = letter_grade(avg)
    print(f"Scores: {scores} -> Average: {avg} -> Grade: {grade}")

if __name__ == "__main__":
    main()
