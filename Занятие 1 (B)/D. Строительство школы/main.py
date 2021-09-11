students_count = int(input())
coordinates = [int(coordinate) for coordinate in input().split()]

middle_index = int(students_count / 2)
print(coordinates[middle_index])


