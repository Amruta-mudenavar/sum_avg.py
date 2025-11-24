def process_scores(scores):
    total = sum(scores)
    average = total / len(scores) if scores else 0
    return total, average

#Example usage:
scores_list = [80, 90, 75, 88, 92]

total, avg = process_scores(scores_list)

print("Scores: ",scores_list)
print("Sum of scores: ",total)
print("Average of scores: ",avg)