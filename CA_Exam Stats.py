grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print(grade)

def grades_sum(scores):
    # compute teh sum of all test grades
    score = 0
    for g in scores:
        score += g
    return score

print(grades_sum(grades))


def grades_average(grades):
    # compute average
    return grades_sum(grades) / float(len(grades))

print(grades_average(grades))


def grades_variance(scores):
    # compute variance
    average = grades_average(scores)
    variance = 0
    for s in scores:
        variance += (average - s) ** 2
    return variance / len(scores)

print(grades_variance(grades))


def grades_std_deviation(variance):
    # compute standard deviation
    return variance ** 0.5

variance = grades_variance(grades)

print(grades_std_deviation(variance))

# ====== Print all

print(print_grades(grades))

print(grades_sum(grades))

print(grades_average(grades))

print(grades_variance(grades))

print(grades_std_deviation(variance))
