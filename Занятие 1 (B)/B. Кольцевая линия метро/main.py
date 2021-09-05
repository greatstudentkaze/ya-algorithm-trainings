station_count, start_station_number, end_station_number = map(int, input().split())

if start_station_number < end_station_number:
    anticlockwise_result = end_station_number - start_station_number - 1
    clockwise_gap = start_station_number
    clockwise_result = station_count + clockwise_gap - end_station_number - 1
    print(min(clockwise_result, anticlockwise_result))
else:
    anticlockwise_gap = station_count - start_station_number
    anticlockwise_result = anticlockwise_gap + end_station_number - 1
    clockwise_result = start_station_number - end_station_number - 1
    print(min(clockwise_result, anticlockwise_result))

