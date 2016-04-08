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
            formatted_dict[formatted_time] += (int(cur_times[1]) - int(pre_times[1])) * time_dict[time_dict.keys()[i]]
        else:
            formatted_dict[formatted_time] = time_dict[time_dict.keys()[i]] * (int(cur_times[1]) - formatted_min)
        # time = datetime.time(int(cur_times[0]), cur_times(cur_times[1]), int(cur_times[2]))
        # print(time)

    return formatted_dict


