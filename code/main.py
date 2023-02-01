# This is a sample Python script.

# Press ⌥⇧R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import read_data as readData
import analyse_data as analyse
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌃' to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    rx, tx = readData.read_beams_Ailton()
    coord = readData.read_valid_coordinates()

    data_train_LOS, data_train_NLOS, data_test_LOS, data_test_NLOS = readData.divide_beams_and_coord_in_LOS_or_NLOS_connect(rx, tx, coord)
    analyse.relation_coord_with_beams_extend_Plot2D(data_train_LOS, 'LOS')
    analyse.relation_coord_with_beams_extend_Plot2D(data_train_NLOS, 'NLOS')
    analyse.relation_coord_with_beams_Plot2D(data_train_LOS, 'LOS')
    analyse.relation_coord_with_beams_Plot2D(data_train_NLOS, 'NLOS')




    analyse.plot_histogram(rx, 'all', 'Rx','skyblue')
    analyse.plot_histogram(tx, 'all', 'Tx','darkslategrey')
    analyse.plot_histogram(data_train_LOS, 'LOS', 'xxx', 'xxx')
    analyse.plot_histogram(data_train_NLOS, 'NLOS', 'xxx', 'xxx')
    analyse.plot_distribution_beams(tx, rx)







    a=0


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
