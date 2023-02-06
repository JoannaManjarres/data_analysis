import numpy as np
import csv

def read_beams_luan():
    data_path = "../data/beams/Luan/episode.npz"
    label_cache_file = np.load(data_path)
    connection_pairs = label_cache_file[label_cache_file.files[1]]

    index_of_invalid_connections = np.isnan(connection_pairs)
    index_of_valid_connections = np.logical_not(index_of_invalid_connections)
    valid_connections = connection_pairs[index_of_valid_connections]

    beans_rx = valid_connections[::2]
    beans_tx = valid_connections[1::2]

    return beans_tx, beans_rx

def read_beams_raymobtime():
    data_path = '../data/beams/Ailton/beam_output/beams_output_8x32.npz'
    beams = np.load(data_path)['output_classification']
    num_antennas_tx = 32
    num_antennas_rx = 8

    best_beam_index = []
    for sample in range(beams.shape[0]):
        best_beam_index.append(np.argmax(beams[sample, :]))

    beam_index_rx = np.array(best_beam_index)

    tx_index = np.zeros((beams.shape[0]), dtype=int)
    rx_index = np.zeros((beams.shape[0]), dtype=int)

    for sample in range(len(beam_index_rx)):
        index_tx = best_beam_index[sample] // num_antennas_rx
        index_rx = best_beam_index[sample] % num_antennas_rx
        tx_index[sample] = index_tx
        rx_index[sample] = index_rx

    return tx_index, rx_index



def read_beams_Ailton():
    data_path = '/Users/Joanna/git/Analise_de_dados/data/beams/Ailton/beam_output/beams_output_1x8.npz'
    beams = np.load(data_path)['output_classification']

    best_beam_index = []
    for sample in range(beams.shape[0]):
        best_beam_index.append(np.argmax(beams[sample, :]))
    #target = mode(best_beam_index)
    #print(target)

    beam_index_rx = np.array(best_beam_index)

    data_path = '/Users/Joanna/git/Analise_de_dados/data/beams/Ailton/beam_output/beams_output_1x16.npz'
    beams = np.load(data_path)['output_classification']

    best_beam_index = []
    for sample in range(beams.shape[0]):
        best_beam_index.append(np.argmax(beams[sample, :]))

    beam_index_tx = np.array(best_beam_index)

    return beam_index_rx, beam_index_tx

def read_valid_coordinates():
    filename = '/Users/Joanna/git/Analise_de_dados/data/coordinates/CoordVehiclesRxPerScene_s008.csv'
    limit_ep_train = 1564

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        number_of_rows = len(list(reader))

    all_info_coord = np.zeros([11194, 5], dtype=object)

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        cont = 0
        for row in reader:
            if row['Val'] == 'V':
                all_info_coord[cont] = int(row['EpisodeID']), float(row['x']), float(row['y']), float(row['z']), row['LOS']
                cont += 1

    # all_info_coord = np.array(all_info_coord)

    coord_train = all_info_coord[(all_info_coord[:, 0] < limit_ep_train + 1)]
    coord_test = all_info_coord[(all_info_coord[:, 0] > limit_ep_train)]

    return all_info_coord

def divide_beams_and_coord_in_LOS_or_NLOS_connect(rx_beams, tx_beams, coord):

    all_data = np.column_stack((coord, rx_beams, tx_beams))
    all_info_LOS = []
    all_info_NLOS = []

    for sample in range(len(all_data)):
        if all_data[sample,4]=='LOS=1':
            all_info_LOS.append(all_data[sample])
        else:
            all_info_NLOS.append(all_data[sample])

    data_LOS = np.array(all_info_LOS)
    data_NLOS = np.array(all_info_NLOS)

    limit_ep_train = 1564

    data_train_LOS = data_LOS[(data_LOS[:, 0] < limit_ep_train + 1)]
    data_test_LOS = data_LOS[(data_LOS[:, 0] > limit_ep_train)]

    data_train_NLOS = data_NLOS[(data_NLOS[:, 0] < limit_ep_train + 1)]
    data_test_NLOS = data_NLOS[(data_NLOS[:, 0] > limit_ep_train)]

    return data_train_LOS, data_train_NLOS, data_test_LOS, data_test_NLOS