from rpy2 import robjects
import rpy2.robjects.packages as rpackages
import numpy as np

r_ssa = rpackages.importr('Rssa')
ssa_get = robjects.r('utils::getFromNamespace("$.ssa", "Rssa")')
ssa_contributions = robjects.r('utils::getFromNamespace("contributions", "Rssa")')


class SSA:

    def __init__(self, ds, L, kind):
        self.obj = r_ssa.ssa(ds, L=L, kind=kind)
        self.sigma = ssa_get(self.obj, "sigma")
        self.U = ssa_get(self.obj, "U").T
        self.V = ssa_get(self.obj, "V")

    def contributions(self, idx):
        idx = np.asarray(idx) + 1
        return ssa_contributions(self.obj, idx)
