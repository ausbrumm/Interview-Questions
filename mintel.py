import json

f = open('data.json')

data = json.load(f)
status_dict = {}

for item in data:
  status_dict[item["status"]] = status_dict.setdefault(item["status"], 0)

print(len(status_dict))

status_set = set()
for item in data:
  status_set.add(item["status"])
print(len(status_set))

# user id : number of operations
# "user_id" : index counting up
user_key = "user_id"
user_count_dict = {}

for item in data:
  if item[user_key] in user_count_dict:
    user_count_dict[item[user_key]] += 1
  else:
    user_count_dict[item[user_key]] = user_count_dict.setdefault(item[user_key], 1)

top_five = sorted(user_count_dict.items(), key=lambda k_v: (k_v[1], k_v[0]),  reverse=True)

for i in range(5):
  print(top_five[i])

# How long does a piece sat in status 8951?
time_list = []
# def check_avg_time(incoming_dict: dict, status_code: int) -> None
for item in data:
  if item["status"] == 8951:
    start_time = item["start_time"]
    end_time = item["end_time"] if item["end_time"] is not None else 0
    if end_time != 0:
        time_list.append(abs(end_time - start_time))

print("avg", int(sum(time_list)/len(time_list)))

# Given that a status ending in 3 represents an error status, what percentage of pieces in this data set end up in an error status at least twice?
# status ending in "3"
# looking for percentage of pieces AT LEAST twice

count = len(data)
err_3_count = 0
piece_dict = {}

user_key = "piece_id"
status_list = []

for item in data:
  if item[user_key] in piece_dict:
    if str(item["status"])[-1] == "3":
      piece_dict[item[user_key]] += 1
  else:
    piece_dict.setdefault(item[user_key], 0)

for item, data in piece_dict.items():
  if data >= 2:
    err_3_count += 1

print(100*(err_3_count/count), "%")

# question 5

# What is the most common path for a piece to follow through the system?
f.close()
