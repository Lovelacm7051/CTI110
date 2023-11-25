# CTI-110

# P4HW1 - Score List

# Lovelace, Michael

# 11/25/2023


num_of_scores = int(input("Enter the number of scores you would like to enter: "))


score_list = []


for i in range(num_of_scores):
    while True:
        try:
          
            score = float(input(f"Enter score #{i + 1}: "))

           
            if 0 <= score <= 100:

                score_list.append(score)
                break
            else:
                
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            
            print("Invalid input. Please enter a numeric score.")


lowest_score = min(score_list)
print(f"\nLowest Score: {lowest_score}")


score_list.remove(lowest_score)


print("Score List after dropping lowest score:")
for i, score in enumerate(score_list, start=1):
    print(f"Score #{i}: {score}")


average_score = sum(score_list) / len(score_list)
print(f"\nAverage Score: {average_score:.2f}")


if 90 <= average_score <= 100:
    grade = 'A'
elif 80 <= average_score < 90:
    grade = 'B'
elif 70 <= average_score < 80:
    grade = 'C'
elif 60 <= average_score < 70:
    grade = 'D'
else:
    grade = 'F'


print(f"Letter Grade: {grade}")

