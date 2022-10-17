import json
from collections import Counter
import timeit

data_file = open('data.json')
data = json.load(data_file)

starttime = timeit.default_timer()

status_list = []
piece_list = []
start_time_list = []

for item in data:
    piece_list.append(item["piece_id"])
    status_list.append(item["status"])
    start_time_list.append(item["start_time"])

unique_p_id = []

# get only the unique piece ids
for item in piece_list:
    if item not in unique_p_id:
        unique_p_id.append(item)
print(len(unique_p_id))
# create a dictionary of just unique ids
data_dict = {key: [] for key in unique_p_id}

# store status list and start time list with the key as the piece_id
for i in range(len(piece_list)):
    data_dict[piece_list[i]].append([status_list[i], start_time_list[i]])

# get just the paths
paths = list()

# append the keys to the paths
for i, values in enumerate(data_dict.items()):
    paths.append(values[1])  # status, time


paths = sorted(paths)  # sort on the time

path_list = []

for k in paths:
    temp = []
    if not k[0]:
        del k[0]
    k.sort(key=lambda x: x[1])
    for i, vals in enumerate(k):
        if vals:
            temp.append(vals[0])

    path_list.append(tuple(temp))

    # if key in path_dict:
    #     path_dict[key] += 1
    # else:
    #     path_dict[key] = path_dict.setdefault(key, 1)

# print(path_dict)
# print(counter)
most_common_path, occurrences = Counter(path_list).most_common(1)[0][0], Counter(path_list).most_common(1)[0][1]
print(f"The most common path a piece takes is: {most_common_path}")
print(f"It occurs {occurrences} times.")
print(timeit.default_timer() - starttime)
data_file.close()
