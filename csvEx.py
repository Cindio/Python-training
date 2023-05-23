import csv

with open("/home/cindy/Downloads/exam_results.csv", newline='') as csv_file:
    read = csv.reader(csv_file, delimiter=',')

    math_count = []
    physics_count = []
    biology_count = []

    for row in read:
        if row[0] == 'Maths':
            math_count.append(row)
        if row[0] == 'Physics':
            physics_count.append(row)
        if row[0] == 'Biology':
            biology_count.append(row)
    cand_count = set(())
    score = []
    pass_count = 0
    fail_count = 0
    counter = 0
    for candidate in math_count:
        cand_count.add(math_count[counter][1])
        score.append(math_count[counter][2])
        if math_count[counter][3] == 'Pass':
            pass_count += 1
        if math_count[counter][3] == 'Fail':
            fail_count += 1
        counter += 1
    score.sort()
    print(f"For Math, there were ", len(cand_count),
          f"candidates, with {pass_count} passing grades and {fail_count} failures. The highest score was", score[-1],
          "and the lowest was", score[0], ".")
    cand_count = set(())
    score = []
    pass_count = 0
    fail_count = 0
    counter = 0

    for candidate in physics_count:
        cand_count.add(physics_count[counter][1])
        score.append(physics_count[counter][2])
        if physics_count[counter][3] == 'Pass':
            pass_count += 1
        if physics_count[counter][3] == 'Fail':
            fail_count += 1
        counter += 1
    score.sort()
    print(f"For Physics, there were ", len(cand_count),
          f"candidates, with {pass_count} passing grades and {fail_count} failures. The highest score was", score[-1],
          "and the lowest was", score[0], ".")
    cand_count = set(())
    score = []
    pass_count = 0
    fail_count = 0
    counter = 0
    for candidate in biology_count:
        cand_count.add(biology_count[counter][1])
        score.append(biology_count[counter][2])
        if biology_count[counter][3] == 'Pass':
            pass_count += 1
        if biology_count[counter][3] == 'Fail':
            fail_count += 1
        counter += 1
    score.sort()
    print(f"For Biology, there were ", len(cand_count), f"candidates, with {pass_count} passing grades and {fail_count} failures. The highest score was", score[-1], "and the lowest was", score[0], ".")
