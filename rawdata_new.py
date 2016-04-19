from collections import OrderedDict
from openpyxl import load_workbook
from collections import OrderedDict

screen_size = 15


def parse_time_dict(time_dict):
    # initialization
    formatted_dict = OrderedDict()

    for i in range(len(time_dict.keys())):  # loop dates
        daily_power = OrderedDict()
        date_index = time_dict.keys()[i]
        date_list = []
        date_list.append(date_index)

        for j in range(len(time_dict.values()[i].keys())):# time_dict.values()[0].keys() times in the dict
            if 
            cur_times = str(time_dict.values()[i].keys()[j]).split(":")
            print time_dict.values()[i].values()[j]

            # format time into categorises
            # hour
            formatted_hour = cur_times[0]
            # minute
            categorise_num = int (60 / screen_size) # how many categorises will be used, screen_size is 30, categorise is 2

            for num_categorises_loop in range (categorise_num - 1):
                print num_categorises_loop
                print categorise_num
                if int(cur_times[1]) >= (screen_size * num_categorises_loop) and int(cur_times[1]) <= (screen_size * (num_categorises_loop + 1) - 1):
                    formatted_min = (num_categorises_loop + 1) * screen_size
                    break
            try:
                formatted_min
            except NameError:
                formatted_min = 0
            else:
                pass
            # second
            # formatted_sec = cur_times[2]

            formatted_time = formatted_hour + ":" + str(formatted_min)  # str
            print formatted_time

            if formatted_time in formatted_dict:
                pre_times = str(time_dict.values()[i].keys()[j - 1]).split(":")
                print pre_times
                print time_dict.values()[i].values()[j]
                temp = ((int(cur_times[1]) - int(pre_times[1])) * time_dict.values()[i].values()[j]) / screen_size
                print temp
                formatted_dict[formatted_time] = formatted_dict[formatted_time] + ((int(cur_times[1]) - int(pre_times[1])) * time_dict.values()[i].values()[j]) / screen_size
                print formatted_dict
            else:
                formatted_dict[formatted_time] = (time_dict.values()[i].values()[j] * abs((int(cur_times[1]) / screen_size) * screen_size - int(cur_times[1]))) / screen_size
                print formatted_dict

                if formatted_dict.keys().index(formatted_time) != 0:
                    print formatted_dict.keys().index(formatted_time)
                    print time_dict.values()[i].keys()[j]
                    print time_dict.values()[i].keys()[j - 1]
                    pre_times = str(time_dict.values()[i].keys()[j - 1]).split(":")
                    upper_gap = (int(pre_times[1]) / screen_size + 1) * screen_size - int(pre_times[1])
                    print "upper gap" + str(upper_gap)

                    print formatted_dict.keys()[formatted_dict.keys().index(formatted_time) - 1]
                    formatted_dict[
                        formatted_dict.keys()[formatted_dict.keys().index(formatted_time) - 1]] += upper_gap * \
                                                                                                   time_dict.values()[
                                                                                                       i].values()[
                                                                                                       j] / screen_size
                    # formatted_dict[formatted_dict.keys().index(formatted_time) - 1] += upper_gap *
                    # time = datetime.time(int(cur_times[0]), cur_times(cur_times[1]), int(cur_times[2]))
                    # print(time)
                    print formatted_dict

        daily_power[time_dict.keys()[i]] = formatted_dict
        print daily_power

    return formatted_dict


def get_time_dict():
    # First we get the date from the original sheet

    # Load the excel file
    wb = load_workbook("D:/DoF_data_income/RealTimeDataAnalysis/test.xlsx")
    print(wb.get_sheet_names()[0])

    # Get the first sheet
    ws_raw = wb.get_sheet_by_name(wb.get_sheet_names()[0])

    # Get the first column(Date/Time)
    date_times = ws_raw.columns[0]

    # Get the second column(Value)
    values = ws_raw.columns[1]

    # Ordered dictionary that contains consumption result,
    # key is the date(yyyy-mm-dd),
    # value is also an ordered dictionary,
    # of which the key is the time(hh:mm:ss)
    # the value is the consumption value of that time
    consumption = OrderedDict()

    # Iterate through all the times
    for i in range(1, len(date_times)):
        # Get the ith cell of Date/Time
        date_time = date_times[i]
        if date_time.value is None:
            # print date_time.value
            break
        else:
            # Split the string by space into a list,
            # first element is date, second element is time

            # date_object = datetime.strptime((str)(date_time.value), '%Y-%m-%d %H:%M:%S')
            # date_string = date_object.strftime('%Y-%m-%d %H:%M:%S')
            date_time_list = str(date_time.value).split()
            # date = "yyyy-mm-dd"
            date = date_time_list[0]
            # time = "hh:mm:ss"
            time = date_time_list[1]

            # If our ordered dictionary contains
            # this date key, we get its corresponding value
            # which is an ordered dictionary
            if date in consumption:
                time_dict = consumption[date]
                # print time_dict
                # If not, we create a new ordered dictionary
            else:
                time_dict = OrderedDict()
                # print time_dict

                # Then we put the key value pair in the inner dict
            time_dict[time] = values[i].value
            # print values[i].value
            # print time_dict

            # Then put the key value pair to the consumption dict
            consumption[date] = time_dict
            # print consumption

            # print(consumption.keys())

            # print(consumption[consumption.keys()[0]])

    # print(consumption)
    return consumption


time_dict = get_time_dict()

print time_dict.values()[0].keys()  # time
print time_dict.keys()  # date

print time_dict.items()
print time_dict

# time_dict.values()[].keys() times in the dict
# time_dict.values()[].values()[] power in the dict
# time_dict.keys() dates

new_time = parse_time_dict(time_dict)
# print(parse_time_dict(time_dict).items())
