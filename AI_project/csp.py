domain=[
    "running", "weightlifting", "yoga", "cycling", "swimming", "jump rope", "hiking", 
    "pilates", "kickboxing", "circuit training", "rowing", "calisthenics", 
    "dumbbell curls", "dumbbell lunges", "dumbbell shoulder press", "push-ups", 
    "bodyweight squats", "plank", "jumping jacks", "burpees", "weighted squat and press", 
    "resistance band rows with dumbbells", "jump rope with medicine ball slams", 
    "circuit training with dumbbells and exercise mat", "swimming with aqua dumbbells", 
    "rowing with resistance bands", "kickboxing with dumbbells", 
    "pilates with stability ball and resistance bands", "hiking with weighted vest"
]

variables = []


# Exercise: [Min Duration (min), Max Duration (min), Min Intensity, Max Intensity, [Equipment], Min Calories Burned, Max Calories Burned]

dataset={
    "running": [10, 60, 3, 5, ["running shoes"], 150, 400, "cardio"],
    "weightlifting": [20, 90, 4, 8, ["dumbbells", "barbell"], 200, 500, "full body"],
    "yoga": [15, 60, 2, 6, ["none"], 90, 200, "flexibility"],
    "cycling": [20, 120, 3, 7, ["bicycle"], 250, 600, "legs"],
    "swimming": [30, 90, 5, 9, ["swimsuit", "goggles"], 300, 700, "full body"],
    "jump rope": [10, 30, 4, 8, ["jump rope"], 120, 300, "cardio"],
    "hiking": [30, 180, 3, 7, ["hiking boots"], 180, 400, "legs"],
    "pilates": [20, 60, 2, 6, ["yoga mat", "resistance bands"], 120, 300, "core"],
    "kickboxing": [45, 90, 6, 9, ["boxing gloves"], 400, 800, "full body"],
    "circuit training": [30, 75, 5, 8, ["dumbbells", "exercise mat"], 300, 600, "full body"],
    "rowing": [15, 45, 4, 8, ["rowing machine"], 220, 500, "back, arms"],
    "calisthenics": [20, 60, 3, 7, ["none"], 150, 350, "full body"],
    "dumbbell curls": [15, 45, 4, 8, ["dumbbells"], 100, 200, "arms"],
    "dumbbell lunges": [20, 40, 3, 7, ["dumbbells"], 150, 300, "legs"],
    "dumbbell shoulder press": [15, 50, 5, 9, ["dumbbells"], 120, 250, "shoulders"],
    "push-ups": [5, 20, 2, 6, ["none"], 50, 100, "chest"],
    "bodyweight squats": [10, 30, 3, 7, ["none"], 60, 120, "legs"],
    "plank": [1, 5, 2, 6, ["none"], 20, 50, "core"],
    "jumping jacks": [5, 15, 3, 7, ["none"], 40, 80, "full body"],
    "burpees": [10, 30, 5, 9, ["none"], 70, 150, "full body"],
    "weighted squat and press": [15, 45, 3, 8, ["dumbbells", "barbell"], 120, 250, "legs, shoulders"],
    "resistance band rows with dumbbells": [20, 60, 3, 8, ["dumbbells", "resistance bands"], 150, 300, "back, arms"],
    "jump rope with medicine ball slams": [15, 30, 4, 8, ["jump rope", "medicine ball"], 180, 400, "cardio, full body"],
    "circuit training with dumbbells and exercise mat": [30, 75, 5, 8, ["dumbbells", "exercise mat"], 300, 600, "full body"],
    "swimming with aqua dumbbells": [30, 90, 5, 9, ["swimsuit", "goggles", "aqua dumbbells"], 300, 700, "full body"],
    "rowing with resistance bands": [15, 45, 4, 8, ["rowing machine", "resistance bands"], 220, 500, "back, arms"],
    "kickboxing with dumbbells": [45, 90, 6, 9, ["boxing gloves", "dumbbells"], 400, 800, "full body"],
    "pilates with stability ball and resistance bands": [20, 60, 2, 6, ["yoga mat", "stability ball", "resistance bands"], 120, 300, "core, flexibility"],
    "hiking with weighted vest": [30, 180, 3, 7, ["hiking boots", "weighted vest"], 180, 400, "legs"]
}


i=0

def calculate_best_exercise(equipment, duration, intensity, calories, target_muscle, i, variables):
    c = 0
    if i < len(domain):
        exercise = domain[i]
        if equipment.lower() in dataset[exercise][4]:
            c += 1
            if duration >= dataset[exercise][0] and duration <= dataset[exercise][1]:
                c += 1
                if calories >= dataset[exercise][5] and calories <= dataset[exercise][6]:
                    c += 1
                    if intensity >= dataset[exercise][2] and intensity <= dataset[exercise][3]:
                        c += 1
                        if target_muscle.lower() in dataset[exercise][-1]:
                            variables.append([c, exercise])
                            calculate_best_exercise(
                                equipment, duration, intensity, calories, target_muscle, i + 1, variables
                            )
                            return variables
                        else:
                            variables.append([c, exercise])
                            calculate_best_exercise(
                                equipment, duration, intensity, calories, target_muscle, i + 1, variables
                            )
                            return variables
                    else:
                        variables.append([c, exercise])
                        calculate_best_exercise(
                            equipment, duration, intensity, calories, target_muscle, i + 1, variables
                        )
                        return variables
                else:
                    variables.append([c, exercise])
                    calculate_best_exercise(
                        equipment, duration, intensity, calories, target_muscle, i + 1, variables
                    )
                    return variables
            else:
                variables.append([c, exercise])
                calculate_best_exercise(equipment, duration, intensity, calories, target_muscle, i + 1, variables)
                return variables
        else:
            variables.append([c, exercise])
            calculate_best_exercise(equipment, duration, intensity, calories, target_muscle, i + 1, variables)
            return variables
    else:
        
        return variables


