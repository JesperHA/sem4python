import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth

filename = './iris_data.csv'

df = pd.read_csv(filename, decimal=',')

labels_unique = df['Species'].unique()
colours = ['red', 'orange', 'green']


def scatter_plot():

    for i in range(0, 3):
        value = labels_unique[i]
        species_df = df.loc[df['Species'] == value]
        plt.scatter(
            species_df['Petal length'],
            species_df['Petal width'],
            color=colours[i],
            alpha=0.5,
            label=labels_unique[i]
        )

    plt.xlabel('sepal length')
    plt.ylabel('petal length')
    plt.title('petal length vs sepal length')


    return plt

# scatter_plot()


data = df.drop(['Species'], axis=1)

def mean_shift(data, n_samples=1000):
    bandwidth = estimate_bandwidth(data, quantile=0.2, n_samples=n_samples)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    print('labels: {}'.format(labels))
    print('Number of estimated clusters : {}'.format(n_clusters))
    print('Cluster centers: {}'.format(cluster_centers))
    return labels, cluster_centers, n_clusters


ms = mean_shift(data)

def ms_plot(data):
    labels = data[0]
    cluster_centers = data[1]

    scatter_plot()

    plt.scatter(
    cluster_centers[0],
    cluster_centers[1],
    color="black",
    alpha=1,
    )

    plt.show()

        
ms_plot(ms)


