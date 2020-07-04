import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from hr import HR_Config


def extract_HR_data_by_tag(rel_path_to_data='data/', tag='*'):
    """Extract HR data. Suggested tags:
    '*workout*', '*easy*', '*long*', '*warmup*', '*cooldown*', '*run*', '*ride*'
    """

    HRs = []
    num_files = 0
    for filename in glob.glob(os.path.join(rel_path_to_data, f"{tag}.gpx")):
        print(f"Opening file {filename}")
        num_files += 1
        f = open(filename, 'r')
        data = f.readlines()
        for l in data:
           if l.strip().startswith("<gpxtpx:hr>"):
               HRs.append(int(l.strip()[11:-12]))
        f.close()
    return HRs, num_files


def plot_hr_config_x(hrc, HRmin=100, HRmax=190):
    """Plot HR_config data where HR is along the x-axis."""
    # Set ticks on x-axis
    num_ticks = 7
    x = list(np.linspace(HRmin, HRmax, num_ticks).astype(int))
    xticks = list(np.linspace(HRmin, HRmax, num_ticks).astype(int))
    plt.xticks(x, xticks)

    # Mark HR zones
    plt.axvspan(HRmin, hrc.Z1_h, facecolor='c', alpha=0.3)
    plt.axvspan(hrc.Z2_l, hrc.Z2_h, facecolor='b', alpha=0.3)
    plt.axvspan(hrc.Z3_l, hrc.Z3_h, facecolor='g', alpha=0.3)
    plt.axvspan(hrc.Z4_l, hrc.Z4_h, facecolor='y', alpha=0.3)
    plt.axvspan(hrc.Z5_l, HRmax, facecolor='r', alpha=0.3)
    colors = [mpatches.Patch(color='c', label='Z1'),
              mpatches.Patch(color='b', label='Z2'),
              mpatches.Patch(color='g', label='Z3'),
              mpatches.Patch(color='y', label='Z4'),
              mpatches.Patch(color='r', label='Z5')]

    # Mark HR thresholds
    lt = plt.axvline(x=hrc.lthr, linewidth=1.0, color='k', dashes=(5, 5), label='LT')
    vt = plt.axvline(x=hrc.vthr, linewidth=1.0, color='k', dashes=(10, 10), label='VT')
    rcp = plt.axvline(x=hrc.rcphr, linewidth=1.0, color='k', dashes=(2, 2), label="RCP")
    thresholds = [lt, vt, rcp]

    # Add legend
    plt.legend(handles=colors + thresholds, loc='upper left')

def plot_hr_config_y(hrc, HRmin=100, HRmax=190):
    """Plot HR_config data where HR is along the y-axis."""
    # Set ticks on x-axis
    num_ticks = 7
    y = list(np.linspace(HRmin, HRmax, num_ticks))
    yticks = list(np.linspace(HRmin, HRmax, num_ticks))
    plt.yticks(y, yticks)

    # Mark HR zones
    plt.axhspan(HRmin, hrc.Z1_h, facecolor='c', alpha=0.2)
    plt.axhspan(hrc.Z2_l, hrc.Z2_h, facecolor='b', alpha=0.2)
    plt.axhspan(hrc.Z3_l, hrc.Z3_h, facecolor='g', alpha=0.2)
    plt.axhspan(hrc.Z4_l, hrc.Z4_h, facecolor='y', alpha=0.2)
    plt.axhspan(hrc.Z5_l, HRmax, facecolor='r', alpha=0.2)
    colors = [mpatches.Patch(color='c', label='Z1'),
              mpatches.Patch(color='b', label='Z2'),
              mpatches.Patch(color='g', label='Z3'),
              mpatches.Patch(color='y', label='Z4'),
              mpatches.Patch(color='r', label='Z5')]

    # Mark HR thresholds
    lt = plt.axhline(y=hrc.lthr, linewidth=1.0, color='k', dashes=(5, 5), label='LT')
    vt = plt.axhline(y=hrc.vthr, linewidth=1.0, color='k', dashes=(10, 10), label='VT')
    rcp = plt.axhline(y=hrc.rcphr, linewidth=1.0, color='k', dashes=(2, 2), label="RCP")
    thresholds = [lt, vt, rcp]

    # Add legend
    plt.legend(handles=colors + thresholds, loc='upper left')


def cumulative_HR_data(HRs, HRmin=100, HRmax=190, num_files='', tag='*'):
    """Histogram of total time spent at different heart rates"""

    # Histogram of HR data
    plt.hist(x=np.asarray(HRs), bins=list(range(HRmin, HRmax)), rwidth=1.0, color='k', alpha=0.5)

    # Graph labels
    plt.xlabel("Heart Rate")
    plt.ylabel("Time")
    plt.title(f"Data from {num_files} '{tag.strip('*')}' activities")

def HR_over_time(HRs, HRmin=100, HRmax=190):
    plt.plot(HRs)
    plt.ylim(HRmin, HRmax)