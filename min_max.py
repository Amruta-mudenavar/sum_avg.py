def process_scores(scores):
    total = sum(scores)
    average = total / len(scores) if scores else 0
    minimum = min(scores) if scores else None
    maximum = max(scores) if scores else None
    
    return total, average, minimum, maximum

#Example usage:
scores_list = [85, 92, 78, 90, 88]

total, avg, min_score, max_score = process_scores(scores_list)

print("Scores: ", scores_list)
print("Sum of scores: ", total)
print("Average of scores: ", avg)
print("Minimum scores: ",min_score)
print("Maximum scores: ", max_score)