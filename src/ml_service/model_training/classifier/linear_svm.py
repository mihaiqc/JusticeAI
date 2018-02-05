from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import precision_recall_fscore_support
from util.log import Log
from util.file import Save, Load
import numpy as np


class LinearSVM:

    def __init__(self, data_set=[]):
        """
            LinearSVM constructor
            param: data_set: entire dataset that the classifier
                             will use to train
        """
        self.data_set = data_set

    def load(self):
        """
            Loads the classifier from its binary
        """
        self.model = Load.load_binary("svm_model.bin")

    def train(self):
        """
            Trains the Linear Support Vector Machine.
        """
        (x_total, y_total) = self._reshape_dataset()
        x_train, x_test, y_train, y_test = train_test_split(
            x_total, y_total, test_size=0.20, random_state=42)
        Log.write("Sample size: {}".format(len(x_total)))
        Log.write("Train size: {}".format(len(x_train)))
        Log.write("Test size: {}".format(len(x_test)))

        Log.write("Training Classifier using SVC")
        clf = svm.SVC(kernel='linear', random_state=42)
        clf.fit(x_train, y_train)

        # Test
        Log.write("Testing Classifier")
        y_predict = clf.predict(x_test)
        num_correct = np.sum(y_predict == y_test)
        (precision, recall, f1, _) = precision_recall_fscore_support(y_test, y_predict)
        Log.write('Test accuracy: {}%'.format(
            num_correct * 100.0 / len(y_test)))
        Log.write('Precision: {}'.format(precision))
        Log.write('Recall: {}'.format(recall))
        Log.write('F1: {}'.format(f1))
        self.model = clf
        save = Save()
        save.save_binary("svm_model.bin", self.model)

    def predict(self, facts_vector):
        """
          Predicts the outcome, based on the given
          fact vector
          param: facts_vector: a vector representation of all the
                               facts
          returns: the predicted outcome vector
        """
        if hasattr(self, 'model'):
            return self.model.predict([facts_vector])
        Log.write('Please train or load the classifier first')
        return None

    def get_weights(self):
        """
            returns: the weight associated with each input fact.
                     Useful in seeing which facts the classifier
                     values more than others
        """
        if hasattr(self, 'model'):
            return self.model.coef_[0]
        Log.write('Please train or load the classifier first')
        return None

    def evaluate_best_parameters(self):
        """
            Evaluate several different parameter combinations and
            returns the best combination.
            returns: a dict containing the most optimal parameter
                     combination
        """
        (x_total, y_total) = self._reshape_dataset()
        x_train, x_test, y_train, y_test = train_test_split(
            x_total, y_total, test_size=0.20, random_state=42)

        parameters = {'kernel': ('linear', 'poly', 'sigmoid',
                                 'rbf'),
                      'C': [0.5, 0.7, 1, 1.5, 2, 3, 5]

                      }

        svc = svm.SVC()
        clf = GridSearchCV(svc, parameters)
        clf.fit(x_train, y_train)
        return clf.best_params_

    def _reshape_dataset(self):
        """
            Reshapes the given dataset to acommodate
            ML algorithm.

            x_total = m X n then y_total = x X 1

            returns: (m X n matrix, m X 1 matrix)
        """
        x_total = np.array(
            [np.reshape(precedent['facts_vector'], (len(precedent['facts_vector'],))) for precedent in self.data_set])
        y_total = np.array(
            [precedent['outcomes_vector'][0] for precedent in self.data_set])
        return x_total, y_total