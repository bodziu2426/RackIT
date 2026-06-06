import openpyxl
import json

def parse_sheet(wb, sheet_name, min_row, max_row):
    ws = wb[sheet_name]
    list_name =[]

    for row in ws.iter_rows(min_row, max_row):
        exercise = {
            "name": row[1].value,
            "series": row[2].value,
            "rep_range": row[3].value,
            "start_weight": row[4].value
        }
        list_name.append(exercise) 

    return list_name

wb = openpyxl.open("Plan_PPL_Dziennik_NEW.xlsx")

push_exercises = parse_sheet(wb, "PUSH – Klatka · Barki · Triceps", 8, 12)
pull_exercises = parse_sheet(wb, "PULL – Plecy · Biceps", 8, 11)
legs_exercises = parse_sheet(wb, "NOGI – Uda · Pośladki", 8, 10)

workout_plan = {
    "push": push_exercises,
    "pull": pull_exercises,
    "legs": legs_exercises
}

with open("Training/Faza_1/workout_plan.json", "w") as f:
    json.dump(workout_plan, f)
