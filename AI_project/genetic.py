import random

population_size=25
num_daysdays=5
exercise_per_day=5
num_generations = 100

CHEST=[('Push-ups','Beg','Num',10),
       ('Incline Push-ups','Beg','Num',15),
       ('Shoulder Stretch','Beg','Num',10),
       ('Tricep Dips','Int','Num',20),
       ('Chest Stretch','Int',5,30),
       ('Arm Circles','Int',5,30),
       ('Cobra Stretch','Adv','Num',40),
       ('Decline Push-ups','Adv','Num',40),
       ('Burpees','Adv','Num',50)]

ABS=[('Mountain Climber','Beg',3,20),
     ('Jumping Jacks','Beg',3,15),
     ('Butt Bridge','Beg','Num',10),
     ('Russian Twist','Int','Num',30),
     ('Crossover Crunch','Int','Num',40),
     ('Heel Touch','Int','Num',30),
     ('Plank','Adv',8,40),
     ('Side Bridges','Adv','Num',45),
     ('Spine Lumber Twist Stretch','Adv','Num',50)]

LEG=[('Side Hop','Beg',3,15),
     ('Wall Calf Stretch','Beg',3,10),
     ('Knee to Chest Stretch','Beg','Num',20),
     ('Lunges','Int','Num',25),
     ('Squats','Int','Num',30),
     ('Wall Sit','Int',5,25),
     ('Butterfly Stretch','Adv',8,35),
     ('Side Leg Circles','Adv','Num',45),
     ('Crusty Lunges','Adv','Num',50)]

ARM=[('Standing Bicep Stretch','Beg','Num',10),
     ('Leg Barbell Curl','Beg','Num',15),
     ('Chest Press Pulse','Beg',3,15),
     ('Skipping','Int',5,25),
     ('Diamond Push-up','Int','Num',30),
     ('Floor Tricep Dips','Int',5,30),
     ('Pull ups','Adv','Num',40),
     ('Shoulder Gator','Adv',8,40),
     ('Arm Curls Crunch','Adv','Num',50)]

BACK=[('Cat Cow Pose','Beg',3,10),
      ('Child Pose','Beg',3,10),
      ('Rhomboid Pulls','Beg',3,20),
      ('Hip Hinge','Int','Num',30),
      ('Hover Push-up','Int','Num',30),
      ('Lying Superman Pose','Int',5,20),
      ('Hyperextension','Adv','Num',35),
      ('Inchworms','Adv','Num',50),
      ('Reverse Push-up','Adv','Num',45)]


exercise_categories = {'Chest': CHEST, 'Abs': ABS, 'Legs': LEG, 'Arms': ARM, 'Back': BACK}

def generate_individual(level):
    individual = {}
    for category, exercises in exercise_categories.items():
        individual[category] = list(random.choice(exercises[a:n]))
    return individual

def calculate_fitness(individual):
    fitness=0
    for cat,exercise in individual.items():
        if exercise[-2]=='Num':
            fitness+=pushups*exercise[-1]
        else:
            fitness+=(exercise[-2]*exercise[-1])
    return fitness

def crossover(parent1, parent2):
    child = {}
    for category in exercise_categories.keys():
        if random.random() < 0.5:
            child[category] = parent1[category]
        else:
            child[category] = parent2[category]
    return child

def mutate(individual):
    mutated_category = random.choice(list(exercise_categories.keys()))
    individual[mutated_category] = random.choice(exercise_categories[mutated_category][a:n])
    return individual

def genetic_algorithm(level,pushup):

    global a,n
    if level=='Beginner':
        a=0
        n=3
    elif level=='Intermediate':
        a=3
        n=7
    else:
        a=5
        n=9

    global pushups
    pushups=pushup
    population = [generate_individual(level) for _ in range(population_size)]

    for generation in range(num_generations):
        fitness_scores = [calculate_fitness(individual) for individual in population]
        parents=[]
        for i in range(population_size):
            if random.random() < (fitness_scores[i]/sum(fitness_scores)):
                parents.append(population[i])    

        if not parents:
            best_individual_index = fitness_scores.index(max(fitness_scores))
            parents.append(population[best_individual_index])

        children = []
        while len(children) < population_size - len(parents):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = crossover(parent1, parent2)
            children.append(child)

        for i in range(len(children)):
            if random.random() < 0.1:
                children[i] = mutate(children[i])

        population = parents + children

    best_plan=max(population, key=calculate_fitness)

    return best_plan,calculate_fitness(best_plan)

if __name__ == "__main__":

    population_size = 10
    num_generations = 100
    num_days=5
    level='Beginner'
    pushup=12
    day=0
    total_plan=[]
    fit_score=[]
    print("Best Workout Plan:")
    while day<num_days:
        best_plan,fitness = genetic_algorithm(level,pushup)
        if fitness not in fit_score:
            print(f"\nDay{day+1}:")
            for category, exercise in best_plan.items():
                print(category,exercise,end=' ')
                print("fitness score:",fitness)
            total_plan.append(best_plan)
            fit_score.append(fitness)
            day+=1
        