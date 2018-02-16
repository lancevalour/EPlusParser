from collections import OrderedDict
import datetime

screen_size = 30


def parse_time_dict(time_dict):
    formatted_dict = OrderedDict()
    for i in range(len(time_dict.keys())):
        cur_times = str(time_dict.keys()[i]).split(":")

        formatted_hour = cur_times[0]
        formatted_min = (int(cur_times[1]) / screen_size) * screen_size
        formatted_sec = cur_times[2]

        formatted_time = formatted_hour + ":" + str(formatted_min) + ":" + formatted_sec
        print(formatted_time)
        if formatted_time in formatted_dict:
            pre_times = str(time_dict.keys()[i - 1]).split(":")
            formatted_dict[formatted_time] += (int(cur_times[1]) - int(pre_times[1]))\
                                              * time_dict[time_dict.keys()[i - 1]]
        else:
            formatted_dict[formatted_time] = time_dict[time_dict.keys()[i]] * (int(cur_times[1]) - formatted_min)
            print(formatted_dict.keys().index(formatted_time))
            if formatted_dict.keys().index(formatted_time) != 0:
                pre_times = str(time_dict.keys()[i - 1]).split(":")
                upper_gap = (int(pre_times[1]) / screen_size + 1) * screen_size - int(pre_times[1])
                print("upper gap " + str(upper_gap))
                formatted_dict[formatted_dict.keys()[formatted_dict.keys().index(formatted_time) - 1]] += \
                    upper_gap * time_dict[time_dict.keys()[i]]
                # formatted_dict[formatted_dict.keys().index(formatted_time) - 1] += upper_gap *
            # time = datetime.time(int(cur_times[0]), cur_times(cur_times[1]), int(cur_times[2]))
            # print(time)

    return formatted_dict


time_dict = OrderedDict()

time_dict["6:58:00"] = 1
time_dict["7:01:00"] = 1
time_dict["7:14:00"] = 1
time_dict["7:20:00"] = 1
time_dict["7:25:00"] = 1
time_dict["7:29:00"] = 1
time_dict["7:32:00"] = 1
time_dict["7:40:00"] = 1
time_dict["7:47:00"] = 1
time_dict["7:55:00"] = 1
time_dict["8:00:00"] = 1
time_dict["8:15:00"] = 1
time_dict["8:30:00"] = 1
time_dict["8:33:00"] = 1

print(time_dict)

print(parse_time_dict(time_dict).items())
