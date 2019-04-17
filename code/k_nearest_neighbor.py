import numpy as np 
from .distances import euclidean_distances, manhattan_distances, cosine_distances

class KNearestNeighbor():    
    def __init__(self, n_neighbors, distance_measure='euclidean'):
        """
        K-Nearest Neighbor is a straightforward algorithm that can be highly
        effective. Training time is...well...is there any training? At test time, labels for
        new points are predicted by comparing them to the nearest neighbors in the
        training data.

        ```distance_measure``` lets you switch between which distance measure you will
        use to compare data points. The behavior is as follows:

        If 'euclideaen', use euclidean_distances, if 'manhattan', use manhattan_distances,
        if  'cosine', use cosine_distances.

        Arguments:
            n_neighbors {int} -- Number of neighbors to use for prediction.
            distance_measure {str} -- Which distance measure to use. Can be one of
                'euclidean', 'manhattan', or 'cosine'. This is the distance measure
                that will be used to compare features to produce labels. 
        """
        self.n_neighbors = n_neighbors

        raise NotImplementedError()


    def fit(self, features, targets):
        """Fit features, a numpy array of size (n_samples, n_features).
        
        Arguments:
            features {np.ndarray} -- Features of each data point, shape of (n_samples,
                n_features).
            targets {[type]} -- Target labels for each data point, shape of (n_samples,)
        """

        raise NotImplementedError()
        

    def predict(self, features):
        """Predict from features, a numpy array of size (n_samples, n_features) Use the
        training data to predict labels on the test features. For each testing sample, compare it
        to the training samples. Look at the self.n_neighbors closest samples to the 
        test sample by comparing their feature vectors. The label for the test sample
        is the most common label among the K nearest neighbors in the training data.

        Arguments:
            features {np.ndarray} -- Features of each data point, shape of (n_samples,
                n_features).

        Returns:
            labels {np.ndarray} -- Labels for each data point, of shape (n_samples,)
        """
        raise NotImplementedError()
