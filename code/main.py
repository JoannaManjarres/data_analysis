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
    tx_index, rx_index = readData.read_beams_raymobtime()
    coord = readData.read_valid_coordinates()

    analyse.plot_histogram(rx_index, 'all', 'Rx_[8X32]', 'skyblue')
    analyse.plot_histogram(tx_index, 'all', 'Tx_[8X32]', 'darkslategrey')

    data_train_LOS, data_train_NLOS, data_test_LOS, data_test_NLOS = readData.divide_beams_and_coord_in_LOS_or_NLOS_connect(rx_index, tx_index, coord)

    analyse.relation_coord_with_beams_Plot2D(data_train_LOS, 'LOS')
    analyse.relation_coord_with_beams_extend_Plot2D(data_train_LOS, 'LOS')
    analyse.plot_histogram(data_train_LOS, 'LOS', 'xxx', 'xxx')

    analyse.plot_distribution_beams(tx_index, rx_index)

    analyse.relation_coord_with_beams_Plot2D(data_train_NLOS, 'NLOS')
    analyse.relation_coord_with_beams_extend_Plot2D(data_train_NLOS, 'NLOS')
    analyse.plot_histogram(data_train_NLOS, 'NLOS', 'xxx', 'xxx')



    # tx_1X8, tx_1X16 = readData.read_beams_Ailton()
    # data_train_LOS, data_train_NLOS, data_test_LOS, data_test_NLOS = readData.divide_beams_and_coord_in_LOS_or_NLOS_connect(tx_1X8, tx_1X16, coord)
    # analyse.relation_coord_with_beams_Plot2D(data_train_LOS, 'Tx [1X16]','LOS')
    # analyse.relation_coord_with_beams_Plot2D(data_train_NLOS, 'NLOS')
    # analyse.relation_coord_with_beams_extend_Plot2D(data_train_LOS, 'LOS')
    # analyse.relation_coord_with_beams_extend_Plot2D(data_train_NLOS, 'NLOS')
    #
    #
    #
    #
    #
    # analyse.plot_histogram(tx_1X8, 'all', 'Tx [1X8]','skyblue')
    # analyse.plot_histogram(tx_1X16, 'all', 'Tx [1X16]','darkslategrey')
    # analyse.plot_histogram(data_train_LOS, 'LOS', 'xxx', 'xxx')
    # analyse.plot_histogram(data_train_NLOS, 'NLOS', 'xxx', 'xxx')
    #analyse.plot_distribution_beams(tx, rx)







    a=0


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
