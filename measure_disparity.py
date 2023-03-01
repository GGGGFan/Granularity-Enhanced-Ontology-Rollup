import numpy as np
from helpers import fairness_measurement
from sklearn.metrics import roc_auc_score, average_precision_score, precision_score, recall_score, precision_recall_curve

class Measure_disparity:
    """
    An object that collect X, y, y_pred, and sensitive attributes.
    with ability to leverage ontologies for bias detection and fairness enhancement.
    """
    def __init__(self,
                 X_train,
                 X_val,
                 y_train,
                 y_val,
                 y_pred,
                 idx_sensitive_attr,
                 dic_race_idx
                ):
        """
        Initialize the learner

        Attributes
        -----------
        X_train: training feature matrix.
        X_val: validation feature matrix.
        y_train: training labels.
        y_val: validation labels.
        idx_sensitive_attr: index of feature that record the sensitive attribute.
        dic_race_idx: mappings from sensitive attributes' text to their encoded values.
        """
        self.X_train = X_train
        self.X_val = X_val
        self.y_train = y_train
        self.y_val = y_val
        self.y_pred = y_pred
        self.idx_sensitive_attr = idx_sensitive_attr
        self.dic_race_idx = dic_race_idx
        self.X_train_new = X_train
        self.X_val_new = X_val

    def evaluate(self, beta, subgroup, lst_customized_evl=None):
        """
        Calculate performance and fairness metrics for each subgroup
        including equal opportunity, demographic parity, AUROC, and AUPR;
        Keep the scores and record the underperformed subgroup to the learner.

        Input
        ---------
        self: y_pred and y_val are needed from the learner.
        beta: f-beta score to be maximized when setting the threshold for binary output.
        subgroup: the subgroup on which the measurement is taken.
        lst_customized_evl: list of evaluation metrics in addition to included 4 metrics, if any.

        Return
        ---------
        dic_subg_evl: the AUROC, AUPR, equal opportunity, and demographic parity of each subgroup
        """
        dic_race_res = {}
        # measurement on the subgroup
        X_val_sub = self.X_val[np.where(self.X_val[:,-1]==self.dic_race_idx[subgroup])[0], :]
        y_val_sub = self.y_val[np.where(self.X_val[:,-1]==self.dic_race_idx[subgroup])[0]]
        y_pred_sub = self.y_pred[np.where(self.X_val[:,-1]==self.dic_race_idx[subgroup])[0]]
        precision, recall, thres  = precision_recall_curve(y_val_sub, y_pred_sub)
        f1_score = (1+beta^2) * (precision * recall+0.00001) / ((beta^2)*precision + recall + 0.00001)
        valid_precision = list(np.where(precision!=0)[0])
        valid_recall = list(np.where(recall!=0)[0])
        valid_idx = [v for v in valid_precision if v in valid_recall]
        f1_score = f1_score[valid_idx]
        thres = thres[valid_idx]
        best_thres = thres[np.argmax(f1_score[:-max(1,int(f1_score.shape[0]*0.2))])]
        y_pred_sub_binary = y_pred_sub >= best_thres
        # fairness measurement
        equal_oppo, demog_parity = fairness_measurement(y_val_sub, y_pred_sub, y_pred_sub_binary)
        auroc = round(roc_auc_score(y_val_sub, y_pred_sub), 3)
        aupr = round(average_precision_score(y_val_sub, y_pred_sub), 3)
        dic_race_res[subgroup] = [auroc, aupr, equal_oppo, demog_parity]
        # measurement on other subgroups
        X_val_sub = self.X_val[np.where(self.X_val[:,-1]!=self.dic_race_idx[subgroup])[0], :]
        y_val_sub = self.y_val[np.where(self.X_val[:,-1]!=self.dic_race_idx[subgroup])[0]]
        y_pred_sub = self.y_pred[np.where(self.X_val[:,-1]!=self.dic_race_idx[subgroup])[0]]
        precision, recall, thres  = precision_recall_curve(y_val_sub, y_pred_sub)
        f1_score = (1+beta^2) * (precision * recall+0.00001) / ((beta^2)*precision + recall + 0.00001)
        valid_precision = list(np.where(precision!=0)[0])
        valid_recall = list(np.where(recall!=0)[0])
        valid_idx = [v for v in valid_precision if v in valid_recall]
        f1_score = f1_score[valid_idx]
        thres = thres[valid_idx]
        best_thres = thres[np.argmax(f1_score[:-max(1,int(f1_score.shape[0]*0.2))])]
        y_pred_sub_binary = y_pred_sub >= best_thres
        # fairness measurement
        equal_oppo, demog_parity = fairness_measurement(y_val_sub, y_pred_sub, y_pred_sub_binary)
        auroc = round(roc_auc_score(y_val_sub, y_pred_sub), 3)
        aupr = round(average_precision_score(y_val_sub, y_pred_sub), 3)
        dic_race_res['Other'] = [auroc, aupr, equal_oppo, demog_parity]
        # disparity
        dic_race_res['Disparity'] = [round(abs(dic_race_res['Other'][i]-dic_race_res[subgroup][i]),3)
                                    for i in range(len(dic_race_res['Other']))]
        return dic_race_res
