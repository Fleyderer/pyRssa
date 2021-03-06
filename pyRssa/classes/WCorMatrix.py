from rpy2 import robjects
import rpy2.robjects.packages as rpackages
import numpy as np

r_ssa = rpackages.importr('Rssa')


class WCorMatrix:

    def __init__(self, ds, groups, **kwargs):
        self.groups = np.copy(groups)
        groups = np.asarray(groups) + 1
        self.matrix = robjects.r.wcor(ds, groups, **kwargs)
