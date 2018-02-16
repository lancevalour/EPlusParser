import numpy as np
import h5py
import scipy.io as sio

ev_charging_profile_1hr = "./data/load/EV_charging_profile_1hr.mat"

ev_charging_profile_10mins = "./data/load/EV_charging_profile_10mins.mat"

f = h5py.File(ev_charging_profile_1hr, 'r')

# data = f.get()
# data = np.array(data)  # For converting to numpy array
# print(data)


def plot():
    pass


if __name__ == '__main__':
    plot()
