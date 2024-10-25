import csv
def read_csv(file_name):
    concepts = []
    target = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            concepts.append(row[:-1])
            target.append(row[-1])  
    return concepts, target

def candidate_elimination(concepts, target):
    specific_h = concepts[0].copy() 
    general_h = [['?' for _ in range(len(specific_h))] for _ in range(len(specific_h))]

    for i, h in enumerate(concepts):
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x] = ['?']
        else:  # target[i] == "No"
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
    general_h = [g for g in general_h if g != ['?' for _ in range(len(specific_h))]]

    return specific_h, general_h
file_name = 'candidate.csv'  
concepts, target = read_csv(file_name)
s_final, g_final = candidate_elimination(concepts, target)

print("Final Specific Hypothesis:", s_final, sep="\n")
print("Final General Hypothesis:", g_final, sep="\n")
