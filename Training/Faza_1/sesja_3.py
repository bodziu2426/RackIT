exercise_1 ={
    "name": "Wyciskanie sztangi - płaska",
    "series": 4,
    "rep_range_min": 6,
    "rep_range_max": 8,
    "start_weight": 60
}

exercise_2 ={
    "name": "Wyciskanie hantlami – skośna +30°",
    "series": 3,
    "rep_range_min": 8,
    "rep_range_max": 10,
    "start_weight": "2 x 22,5"
}

exercise_3 ={
    "name": "OHP sztangą",
    "series": 4,
    "rep_range_min": 6,
    "rep_range_max": 10,
    "start_weight": 30
}

exercise_4 ={
    "name": "Odwodzenie na wyciągu jednorącz",
    "series": 3,
    "rep_range_min": 12,
    "rep_range_max": 15,
    "start_weight": 5
}

exercise_5 ={
    "name": "Dipy – nacisk na triceps",
    "series": 4,
    "rep_range_min": 8,
    "rep_range_max": 12,
    "start_weight": "BW"
}

exercises = [exercise_1, exercise_2, exercise_3, exercise_4, exercise_5]

for exercise in exercises:
    if exercise["rep_range_max"] <= 8:
        print(exercise["name"],"Zakres siłowy")
    elif exercise["rep_range_max"] <= 12:
        print(exercise["name"],"Zakres hipertrofii")
    elif exercise["rep_range_max"] > 12 and exercise["series"]>=3:
        print(exercise["name"],"Zakres wytrzymałościowy")
    