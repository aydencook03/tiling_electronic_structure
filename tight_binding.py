import pythtb as tb

##############################################################################################


class TBModel:
    def __init__(self, tiling, onsite_energy=0.0, hop_amp=-1.0):
        self.model = tb.tb_model(
            2, 2, [[vec.x, vec.y] for vec in tiling.lattice_vectors], tiling.unit_coordinates)
        self.set_onsite(on_site_energy)
        if isinstance(hop_amp, int):
            hop_amp = [hop_amp]*len(tilng.hop_pairs)
        for i, pair in enumerate(tiling.hop_pairs):
            self.set_hop(hop_amp[i], pair[0], pair[1])

    def set_onsite(self, onsite_energy, ind_i=None, mode="set"):
        self.model.set_onsite(onsite_energy, ind_i=ind_i, mode=mode)

    def set_hop(self, hop_amp, ind_i, ind_j, ind_R=None, mode="set", allow_conjugate_pair=False):
        selfmodel.set_hop(hop_amp, ind_i, ind_j, ind_R=ind_R,
                          mode=mode, allow_conjugate_pair=allow_conjugate_pair)


def tb_from_tiling(tiling, onsite_energy=0.0, hop_amp=-1.0):
    tb_model = tb.tb_model(
        2, 2, [[vec.x, vec.y] for vec in tiling.lattice_vectors], tiling.unit_coordinates)
    tb_model.set_onsite(on_site_energy)
    if isinstance(hop_amp, int):
        hop_amp = [hop_amp]*len(tilng.hop_pairs)
    for i, pair in enumerate(tiling.hop_pairs):
        tb_model.set_hop(hop_amp[i], pair[0], pair[1])
    return tb_model

##############################################################################################


if __name__ == "__main__":
    pass

##############################################################################################
