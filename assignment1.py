def internship_days(income,travel_costs, rent, other_expenses):
    remaining_income = income - rent - other_expenses 
    travel_days= remaining_income/(2*travel_costs)
    if travel_days < 0:
        return 0
    if travel_days > 30:
        return 30
    else:
        return int(travel_days)
