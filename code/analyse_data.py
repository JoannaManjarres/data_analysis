import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
import statsmodels.api as sm
import matplotlib.pyplot as plt



#def plot_histogram(beam, title, x_label, color):
def plot_histogram(all_data, connection, user, color):

    # n = len(beam)
    # number_of_intervals = int(np.sqrt(n))
    #
    # q25, q75 = np.percentile(beam, [25, 75])
    # bin_width = 2 * (q75 - q25) * len(beam) ** (-1 / 3)
    # bins = round((beam.max() - beam.min()) / bin_width)

    path = '/Users/Joanna/git/Analise_de_dados/results/analyzes/histogram/'

    if connection == 'all':
        data = pd.DataFrame(all_data, columns=['beams'])
        sns.set(style='darkgrid')
        sns.set(rc={'figure.figsize': (8, 4)})
        plot = sns.histplot(data=data,
                     x='beams',
                     bins=15,
                     stat='frequency',
                     color=color,
                     legend=False)
        plt.title('Distribuição de TODOS os indices dos Beams no ' + user, fontweight='bold')
        plt.xlabel('Indices no ' + user)
        plt.ylabel('Frequência')
        plt.legend(bbox_to_anchor=(1.05, 1),
                   borderaxespad=0,
                   loc='upper left',
                   title='Amostras',
                    labels=[str(all_data.shape[0])])
        # plot.fig.set_figwidth(4)
        # plot.fig.set_figheight(8)
        plt.subplots_adjust(right=0.786, bottom=0.155)

        name = 'Histogram_all_Dataset_Beams_' + user + '.png'
        #plt.figure(figsize=(10,6))
        plt.savefig(path + name, transparent=True, dpi=300)

        plt.show()

    else:
        data = pd.DataFrame(all_data, columns=['EpisodeID', 'x', 'y', 'z', 'LOS', 'rxBeams', 'txBeams'])

        n = len(data['rxBeams'])
        number_of_intervals = int(np.sqrt(n))

        q25, q75 = np.percentile(data['rxBeams'], [25, 75])
        bin_width = 2 * (q75 - q25) * len(data['rxBeams']) ** (-1 / 3)
        bins = round((data['rxBeams'].max() - data['rxBeams'].min()) / bin_width)

        sns.set(style='darkgrid')
        sns.set(rc={'figure.figsize': (8, 4)})
        plot = sns.histplot(data=data, x='rxBeams', bins=15, stat='frequency', color='skyblue' )
        plt.title('Distribuição dos indices dos Beams no Rx \n para conexoes ' + connection, fontweight='bold')
        plt.xlabel('Indices no Rx')
        plt.ylabel('Frequência')
        plt.legend(bbox_to_anchor=(1.05, 1),
                   borderaxespad=0,
                   loc='upper left',
                   title='Amostras',
                   labels=[str(all_data.shape[0])])
        plt.subplots_adjust(right=0.786, bottom=0.155)
        #plot.fig.set_figwidth(6)
        #plot.fig.set_figheight(8)
        name = 'Histogram_of_Rx_Beams_' + connection + '.png'
        plt.savefig(path + name, transparent=True, dpi=300)
        plt.show()



        sns.set(style='darkgrid')
        sns.set(rc={'figure.figsize': (8, 4)})
        plot = sns.histplot(data=data, x='txBeams', bins=15, stat='frequency', color='darkslategrey')
        plt.title('Distribuição dos indices dos Beams no Tx \n para conexoes ' +connection, fontweight='bold')
        plt.xlabel('Indices no Tx')
        plt.ylabel('Frequência')
        plt.legend(bbox_to_anchor=(1.05, 1),
                   borderaxespad=0,
                   loc='upper left',
                   title='Amostras',
                   labels=[str(all_data.shape[0])])
        plt.subplots_adjust(right=0.786, bottom=0.155)
        #plot.fig.set_figwidth(6)
        #plot.fig.set_figheight(8)
        name = 'Histogram_of_Tx_Beams_' + connection + '.png'
        plt.savefig(path + name, transparent=True, dpi=300)
        plt.show()




def plot_distribution_beams(beams_tx, beams_rx):
    path = '/Users/Joanna/git/Analise_de_dados/results/analyzes/histogram/'
    plt.Figure(figsize=(32, 8))
    plot = sns.displot(x=beams_tx,
                y=beams_rx,
                row_order=range(8),
                col_order=range(32),
                binwidth=(1, 1),
                aspect=10.67,
                height=3,
                cbar=True)

    plt.title("Distribuicao dos Beams (Tx-Rx)")
    plt.xlabel("beams_tx_index")
    plt.ylabel("beams_rx_index")

    plt.subplots_adjust(left=0.05)
    plt.subplots_adjust(bottom=0.179)
    plt.subplots_adjust(top=0.879)
    #plot.fig.set_figwidth(10)
    #plot.fig.set_figheight(6)
    name = 'Beams_distribution.png'
    plt.savefig(path + name, transparent=True, dpi=300)
    plt.show()


def relation_coord_with_beams_Plot2D(all_data, title):

    data = pd.DataFrame(all_data, columns=['EpisodeID','x','y','z','LOS','rxBeams','txBeams'])
    print(data.head())
    path = '/Users/Joanna/git/Analise_de_dados/results/analyzes/'

    sns.set(style='darkgrid')

    plot = sns.relplot(data=data,
                       x='x',
                       y='y',
                       kind='scatter',
                       # hue='txBeams',
                       # size='txBeams',
                       # sizes=(200, 20),
                       # alpha=0.3,
                       # palette='Spectral',
                       style='txBeams'
                       )
    sns.set(rc={'figure.figsize': (60, 5)})

    plot.fig.suptitle('Distribuicao dos indices dos Beams do Tx \n relativo à posicao usando dados ' + title,
                      fontweight='bold')
    plot.fig.subplots_adjust(top=0.90)
    plot.fig.set_figwidth(6)
    plot.fig.set_figheight(8)

    leg = plot._legend
    leg.set_bbox_to_anchor([1, 0.75])
    name = 'relation_coord_with_Tx_beams_'+title+'.png'
    plt.savefig(path + name, transparent=True, dpi=300)
    plt.show()


    plot = sns.relplot(data=data,
                x='x',
                y='y',
                kind='scatter',
                hue='rxBeams',
                size='rxBeams',
                sizes=(200,20),
                alpha=0.5,
                palette='Spectral')
    sns.set(rc={'figure.figsize':(60,5)})

    plot.fig.suptitle('Distribuicao dos indices dos Beams do Rx \n relativo à posicao usando dados '+title, fontweight='bold')
    plot.fig.subplots_adjust(top=0.90)
    plot.fig.set_figwidth(6)
    plot.fig.set_figheight(8)

    leg = plot._legend
    leg.set_bbox_to_anchor([1, 0.75])
    name = 'relation_coord_with_Rx_beams_' + title + '.png'
    plt.savefig(path + name, transparent=True, dpi=300)
    plt.show()


def relation_coord_with_beams_extend_Plot2D(all_data,title):
    data = pd.DataFrame(all_data, columns=['EpisodeID', 'x', 'y', 'z', 'LOS', 'rxBeams', 'txBeams'])
    print(data.head())
    path = '/Users/Joanna/git/Analise_de_dados/results/analyzes/'


    name = 'relation_coord_with_Rx_beams_extend_'+title+'.png'
    print(name)

    sns.set(style='darkgrid')
    plot = sns.relplot(data=data,
                       x='x',
                       y='y',
                       kind='scatter',
                       hue='rxBeams',
                       palette='dark',
                       style='rxBeams',
                       col='rxBeams',
                       legend=False)
    plot.fig.suptitle('Distribuição dos indices dos Beams do Rx \n relativo à posição usando dados ' + title,
                     fontweight='bold')
    plot.fig.subplots_adjust(top=0.825, left=0.048)
    plot.fig.set_figwidth(15)
    plot.fig.set_figheight(6)
    plt.savefig(path+name, transparent=True, dpi=300)
    plt.show()

    #print(path+name+'.png')

    name = 'relation_coord_with_Tx_beams_extend_' + title + '.png'
    plot = sns.relplot(data=data,
                       x='x',
                       y='y',
                       kind='scatter',
                       hue='txBeams',
                       palette='dark',
                       style='txBeams',
                       col='txBeams',
                       legend=False,
                       col_wrap=8)
    #plot.fig.set_size_inches(20, 6)
    plot.fig.set_figheight(6)
    plot.fig.set_figwidth(40)
    plot.fig.suptitle('Distribuição dos indices dos Beams do Tx \n relativo à posição usando dados ' + title,
                      fontweight='bold')
    plot.fig.subplots_adjust(top=0.825, left=0.048)
    plot.fig.set_figwidth(15)
    plot.fig.set_figheight(6)
    plt.savefig(path + name, transparent=True, dpi=300)
    plt.show()



    # pairplot explore the pairwise relationships between variables.
    #sns.pairplot(data[['x', 'y', 'z', 'rxBeams']], hue='rxBeams', height=3)
    #plt.show()

def plot_variables_correlation(data1, data2, title, x_label, y_label, color):
        # custom = []
        plt.scatter(data1, data2, c=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        # pyplot.legend('test', 'test1')
        plt.show()