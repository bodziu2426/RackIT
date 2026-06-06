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

exercises = [exercise_1, exercise_2]

#print("Ćwiczenie:", exercise_1["name"], "Ciężar startowy:", exercise_1["start_weight"])
#print("Ćwiczenie:", exercise_2["name"], "Ciężar startowy:", exercise_2["start_weight"])

for exercise in exercises:
    print("Ćwiczenie:", exercise["name"], "Ciężar startowy:", exercise["start_weight"])