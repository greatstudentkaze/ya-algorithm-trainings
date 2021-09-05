MAX_MONTHS_COUNT = 12

date_or_month, month_or_date, year = map(int, input().split())

is_first_number_month = date_or_month <= MAX_MONTHS_COUNT
is_second_number_month = month_or_date <= MAX_MONTHS_COUNT

if is_first_number_month and is_second_number_month:
    if date_or_month == month_or_date:
        print(1)
    else:
        print(0)

elif is_first_number_month or is_second_number_month:
    print(1)

else:
    print(0)
