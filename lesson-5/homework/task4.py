import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    """Returns two lists: student enrollments and tuition fees."""
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions

def mean(data):
    """Returns the mean of a list of numbers."""
    return sum(data) / len(data) if data else 0

def median(data):
    """Returns the median of a list of numbers."""
    return statistics.median(data)

# Get enrollment and tuition data
enrollments, tuitions = enrollment_stats(universities)

# Compute statistics
total_students = sum(enrollments)
total_tuition = sum(tuitions)
mean_students = mean(enrollments)
median_students = median(enrollments)
mean_tuition = mean(tuitions)
median_tuition = median(tuitions)

# Display results
print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,}\n")
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,}")
print("*" * 30)
