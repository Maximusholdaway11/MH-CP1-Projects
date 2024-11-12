#Max Holdaway Counting Characters

ACount = 0

BCount = 0

CCount = 0

DCount = 0

ECount = 0

grid = [

['A', 'B', 'C', 'A', 'D'],

['C', 'A', 'B', 'D', 'E'],

['A', 'D', 'C', 'E', 'A'],

['B', 'A', 'C', 'A', 'D'],

['D', 'C', 'B', 'E', 'A'] ]

for y in grid:
    if y in [["A", "B", "C", "A", "D"]]:
        for x in ["A", "B", "C", "A", "D"]:
            if x in ["A"]:
                ACount += 1
            elif x in ["B"]:
                BCount += 1
            elif x in ["C"]:
                CCount += 1
            elif x in ["D"]:
                DCount += 1
            elif x in ["E"]:
                ECount += 1
            else:
                continue

for z in grid:
    if z in [["C", "A", "B", "D", "E"]]:
        for d in ["C", "A", "B", "D", "E"]:
            if d in ["A"]:
                ACount += 1
            elif d in ["B"]:
                BCount += 1
            elif d in ["C"]:
                CCount += 1
            elif d in ["D"]:
                DCount += 1
            elif d in ["E"]:
                ECount += 1
            else:
                continue

for a in grid:
    if a in [["A", "D", "C", "E", "A"]]:
        for e in ["A", "D", "C", "E", "A"]:
            if e in ["A"]:
                ACount += 1
            elif e in ["B"]:
                BCount += 1
            elif e in ["C"]:
                CCount += 1
            elif e in ["D"]:
                DCount += 1
            elif e in ["E"]:
                ECount += 1
            else:
                continue

for b in grid:
    if b in [["B", "A", "C", "A", "D"]]:
        for f in ["B", "A", "C", "A", "D"]:
            if f in ["A"]:
                ACount += 1
            elif f in ["B"]:
                BCount += 1
            elif f in ["C"]:
                CCount += 1
            elif f in ["D"]:
                DCount += 1
            elif f in ["E"]:
                ECount += 1
            else:
                continue

for c in grid:
    if c in [["D", "C", "B", "E", "A"]]:
        for g in ["D", "C", "B", "E", "A"]:
            if g in ["A"]:
                ACount += 1
            elif g in ["B"]:
                BCount += 1
            elif g in ["C"]:
                CCount += 1
            elif g in ["D"]:
                DCount += 1
            elif g in ["E"]:
                ECount += 1
            else:
                continue

print(f"This is the number of A's {ACount}. This is the number of B's {BCount}. This is the number of C's {CCount}. This is the number of D's {DCount}. This is the number of E's {ECount}.")