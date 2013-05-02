"""
Train a random forest classifer.

"""

import os
import sys
import csv
import numpy as np
import scipy
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import StratifiedKFold
from sklearn import metrics

features = list()
labels = list()

for row in csv.reader(open('feature_matrix.csv')):
    labels.append(int(row[0]))
    features.append(map(float,row[1:]))

# convert to matrices
X = np.array(features)
y = np.array(labels)

def cross_val_roc_plot(classifier, X, y, label):
    cv = StratifiedKFold(y, k=6) # 6-fold cross-validation
    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 100)
    all_tpr = list()
    # for each k-fold
    for i, (train, test) in enumerate(cv):
        # probas is percentage of tress that returned 1
        probas_ = classifier.fit(X[train], y[train]).predict_proba(X[test]) # number of trees that return true for a data set, probability that the da
        fpr, tpr, thresholds = metrics.roc_curve(y[test], probas_[:,1]) # compute rock curve
        mean_tpr += scipy.interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0
        roc_auc = metrics.auc(fpr, tpr)
        # plotting
        plt.plot(fpr, tpr, lw=1, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))
    
    # plot the average
    plt.plot([0,1], [0,1], '--', color=(0.6, 0.6, 0.6), label='Luck')
    mean_tpr /= len(cv)
    mean_tpr[-1] = 1.0
    mean_auc = metrics.auc(mean_fpr, mean_tpr)
    plt.plot(mean_fpr, mean_tpr, 'k--', label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)

    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right', borderaxespad=0.)
    plt.savefig('figs/%s.pdf' % label.replace(' ','_'))

plt.figure()
# n_estimators = number of words per tree
# compute_importances = word frequency
# verbose = detail of returned result
clf = RandomForestClassifier(n_estimators=20, compute_importances=True, verbose=1) # intialize RFC, group of 20 datums, print out most frequent(important) words through decision trees, add extra details
cross_val_roc_plot(clf, X[:,:33], y, "Test")
