import matplotlib.pyplot as plt
from hr import *

HRmin, HRmax = 100, 185
hrc = HR_Config(lthr=172.0)

# # Plotting cumulative HR data
tag = '*easy_run*'
HRs, num_files = extract_HR_data_by_tag(rel_path_to_data='data/', tag=tag)
plot_hr_config_x(hrc, HRmin, HRmax)
cumulative_HR_data(HRs, HRmin, HRmax, num_files=num_files, tag=tag)

# # Plotting HR data from a single activity
# HRs, num_files = extract_HR_data_by_tag(rel_path_to_data='data/', tag='*y20m07d04*')
# if num_files != 1:
#     print("Warning: plotting time series for more than one file! \
#     Hopefully they are chronological, check your naming convention.")
# plot_hr_config_y(hrc, HRmin, HRmax)
# HR_over_time(HRs, HRmin, HRmax)

plt.show()