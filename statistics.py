import csv
from collections import Counter


def mean(vals):
    length = len(vals)
    total = 0
    for val in vals:
        total += val
    return total/length

# n/2-1


def median(vals):
    n = len(vals)
    isEven = n % 2 == 0
    vals.sort()
    median = 0
    if(isEven):
        m1 = n//2 - 1
        m2 = n//2+1 - 1
        median = (float(vals[m1])+float(vals[m2])) / 2
    else:
        m = (n+1)//2 - 1
        median = float(vals[m])

    return median


def mode(vals):
    data = Counter(vals)
    [(val, times)] = data.most_common(1)
    return val
    # data = {"50-60": 0, "60-70": 0, "70-80": 0, "90+100": 0}
    #  ct = 0
    #   modrange, mode = 0, 0
    #    for val, occurence in vals.items():
    #         if(50 < val < 60):
    #             ct += occurence
    #         elif(60 < val < 70):
    #             ct += occurence
    #         elif(70 < val < 80):
    #             ct += occurence

    #     for i, occurence in ct.items():
    #         if occurence > mode:
    #             modrange, mode = i.split("-")[0], i.split("-")[1], occurence


with open("./height-weight.csv", newline="") as file:
    reader = csv.reader(file)
    height_weight = list(reader)
    height_weight.pop(0)
    no_of_vals = len(height_weight)
    heights = []
    weights = []
    for i in range(no_of_vals):
        heights.append(float(height_weight[i][1]))
        weights.append(float(height_weight[i][2]))
    print("Heights Data:")
    print("Mean of Heights = " + str(mean(heights)))
    print("Medians of Heights = " + str(median(heights)))
    print("Mode of Heights = " + str(mode(heights)))
    print("-------------------------------------")
    print("Weights Data:")
    print("Mean of Weights = " + str(mean(weights)))
    print("Median of Weights = " + str(median(weights)))
    print("Mode of Weights = " + str(mode(weights)))
