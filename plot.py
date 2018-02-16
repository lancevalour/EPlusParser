import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter, FuncFormatter
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from random import randint
import scipy.io as scio

ev_charging_profile_1hr = "./data/load/EV_charging_profile_1hr.mat"

ev_charging_profile_10mins = "./data/load/EV_charging_profile_10mins.mat"

voltage_4bus_400v_1hr = "./data/voltage/Voltage_4bus_400v_1hr.mat"

voltage_4bus_400v_10mins = "./data/voltage/Voltage_4bus_400v_10mins.mat"


def get_data():
    mat = scio.loadmat(voltage_4bus_400v_10mins)
    # print(mat.keys())
    # print(len(mat.keys()) - 1)
    # print(mat.keys())
    # print(mat.keys()[mat.keys(). - 1])

    keys = list(mat.keys())

    data = np.array(mat.get(keys[len(keys) - 1]))
    print(np.shape(data))
    avg_array = []
    max_array = []
    min_array = []
    hist_array = []
    max = np.amax(data)
    min = np.amin(data)

    for time_index in range(0, len(data)):
        # max = np.amax(data[time_index])
        # min = np.amin(data[time_index])
        # print(len(data[time_index]))
        # print(len(data[time_index]))
        # print(data[time_index])
        # np.shape(data[time_index])
        hist_per_bus = []
        for bus_index in range(0, np.shape(data[time_index])[1]):
            samples = data[time_index][:, bus_index]
            counts, values = np.histogram(samples, bins=10)
            max_count = np.amax(counts)
            max_count_index = 0
            for count_index in range(0, len(counts)):
                if counts[count_index] == max_count:
                    max_count_index = count_index
                    pass
            hist_per_bus.append(values[max_count_index])
            # print(max_count_index)
            # print(values[max_count_index])

        hist_array.append(hist_per_bus)
        avg_array.append(np.average(data[time_index], axis=0))
        max_array.append(np.amax(data[time_index], axis=0))
        min_array.append(np.amin(data[time_index], axis=0))

    avg_array = np.asarray(avg_array)
    max_array = np.asarray(max_array)
    min_array = np.asarray(min_array)
    hist_array = np.asarray(hist_array)

    return avg_array, max_array, min_array, hist_array


def get_mock_data():
    data = []
    for k in range(0, 5):
        bus = []
        for i in range(0, 1000):
            day = []
            for j in range(0, 144):
                day.append(randint(0, 10))
            day_array = np.asarray(day)
            bus.append(day_array)
        bus = np.asarray(bus)
        data.append(bus)

    data_array = np.asarray(data)
    return data_array


def plot_3d(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    ax.set_zlim(np.amin(z), np.amax(z))
    ax.zaxis.set_major_locator(LinearLocator(3))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
    ax.set_zlabel("z")

    ax.set_xlim(np.amin(x), np.amax(x))
    ax.xaxis.set_major_locator(LinearLocator(5))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.set_xlabel("x")

    ax.set_ylim(np.amin(y), np.amax(y))
    ax.yaxis.set_major_locator(LinearLocator(12))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: "%d" % (x / 12)))
    ax.set_ylabel("y")

    # cbaxes = inset_axes(ax, width="3%", height="100%", loc=2)
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # cbaxes = inset_axes(ax, width="3%", height="100%", loc=2)
    # fig.colorbar(surf, cax=cbaxes, ticks=[0., 1], orientation='vertical')

    plt.show()


def plot(data):
    # data = []
    # for k in range(0, 5):
    #     bus = []
    #     for i in range(0, 1000):
    #         day = []
    #         for j in range(0, 144):
    #             day.append(randint(0, 10))
    #         day_array = np.asarray(day)
    #         bus.append(day_array)
    #     bus = np.asarray(bus)
    #     data.append(bus)
    #
    # data_array = np.asarray(data)
    # print(data_array)
    # print(np.shape(data_array))

    zz = []

    for i in range(0, len(data)):
        print(data[i])
        print(np.average(data[i], axis=0))
        zz.append(np.average(data[i]))

    print(np.shape(np.average(data[0])))

    x = np.arange(0, len(data), 1)
    # print(x)
    y = np.arange(0, 144, 1)

    # print(y)
    # z_array = []
    # for i in range(0, len(x)):
    #     z_array.append(y * (i + 1))
    #
    # z = np.asarray(z_array)
    # z = np.transpose(z)
    # print(np.shape(z))

    z_array = []
    for i in range(0, len(x)):
        z_array.append(np.average(data[i], axis=0))

    z = np.asarray(z_array)
    z = np.transpose(z)
    print(np.shape(z))

    x, y = np.meshgrid(x, y)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    ax.set_zlim(np.amin(z), np.amax(z))
    ax.zaxis.set_major_locator(LinearLocator(3))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
    ax.set_zlabel("z")

    ax.set_xlim(np.amin(x), np.amax(x))
    ax.xaxis.set_major_locator(LinearLocator(5))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.set_xlabel("x")

    ax.set_ylim(np.amin(y), np.amax(y))
    ax.yaxis.set_major_locator(LinearLocator(12))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: "%d" % (x / 12)))
    ax.set_ylabel("y")

    # cbaxes = inset_axes(ax, width="3%", height="100%", loc=2)
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # cbaxes = inset_axes(ax, width="3%", height="100%", loc=2)
    # fig.colorbar(surf, cax=cbaxes, ticks=[0., 1], orientation='vertical')

    plt.show()


if __name__ == '__main__':
    # plot(get_mock_data())
    # plot(get_data())
    avg_array, max_array, min_array, hist_array = get_data()

    row, col = np.shape(avg_array)

    x = np.arange(0, col, 1)
    y = np.arange(0, row, 1)
    x, y = np.meshgrid(x, y)

    plot_3d(x, y, avg_array)
    plot_3d(x, y, max_array)
    plot_3d(x, y, min_array)
    plot_3d(x, y, hist_array)
