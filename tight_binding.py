import pythtb as tb

##############################################################################################


class TBModel:
    def __init__(self, tiling):
        self.model = tb.tb_model(2, 2, [[vec.x, vec.y] for vec in tiling.lattice_vectors], [
                                 [vec.x, vec.y] for vec in tiling.unit_coordinates])

##############################################################################################
