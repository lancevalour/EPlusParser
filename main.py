from collections import OrderedDict
import datetime


def parse_time_dict(time_dict):
    formatted_dict = OrderedDict()
    for i in range(len(time_dict.keys())):
        times = str(time_dict.keys()[i]).split(":")
        time = datetime.time(int(times[0]), int(times[1]), int(times[2]))
        print(time)

    formatted_dict[0] = 100
    return formatted_dict


screen_size = 30

time_dict = OrderedDict()

time_dict["6:58:00"] = 100
time_dict["7:01:00"] = 100
time_dict["7:14:00"] = 200
time_dict["7:20:00"] = 300
time_dict["7:25:00"] = 50
time_dict["7:29:00"] = 30
time_dict["7:32:00"] = 150
time_dict["7:40:00"] = 100
time_dict["7:47:00"] = 500
time_dict["7:55:00"] = 200
time_dict["8:00:00"] = 100
time_dict["8:15:00"] = 240
time_dict["8:30:00"] = 40


print(parse_time_dict(time_dict))

