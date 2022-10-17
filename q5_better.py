import timeit
import json
from collections import Counter
# This solution is taking about .01 seconds on average
data_file = open('data.json')
data = json.load(data_file)

start_time = timeit.default_timer()

data_dict = {}

"""
Create a dictionary from the data with format

{
    piece_id: [(status code, start time), ....],
}

We set the default to the first instance
This way we get all the unique IDs
"""
for item in data:
    if item['piece_id'] in data_dict:
        data_dict[item['piece_id']]\
            .append((item['status'], item['start_time']))
    else:
        data_dict[item['piece_id']] = \
            data_dict.setdefault(item['piece_id'],
                                 [(item['status'], item['start_time'])])

paths = []

"""
The idea of this loop is to sort our values,

"""
for key, value in data_dict.items():
    temp = []  # Create a temporary list
    value.sort(key=lambda x: x[1]) # Sort based on time since epoch
    for vals in value:
        if vals:    # Makes sure the list isn't empty
            temp.append(vals[0])  # add value to list

    # The temp list is necessary to use because we needed to convert
    # to a tuple
    paths.append(tuple(temp))


# collect most common path and count the occurrences
most_common_path, occurrences = \
    Counter(paths).most_common(1)[0][0], \
    Counter(paths).most_common(1)[0][1]

print(f"The most common path a piece takes is: {most_common_path}")
print(f"It occurs {occurrences} times.")

print(timeit.default_timer() - start_time)
data_file.close()
