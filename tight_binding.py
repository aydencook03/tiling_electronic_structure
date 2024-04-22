import pythtb as tb

##############################################################################################


def tb_from_tiling(tiling, onsite_en=0.0, hop_amp=-1.0):
    tb_model = tb.tb_model(
        2, 2, lat=[[vec.x, vec.y] for vec in tiling.lattice_vectors], orb=tiling.unit_coordinates)
    if isinstance(onsite_en, float):
        for i, coord in enumerate(tiling.unit_coordinates):
            tb_model.set_onsite(onsite_en, ind_i=i)
    else:
        tb_model.set_onsite(onsite_en)
    if isinstance(hop_amp, float):
        hop_amp = [hop_amp]*len(tiling.hop_pairs)
    for i, pair in enumerate(tiling.hop_pairs):
        tb_model.set_hop(hop_amp[i], pair[0], pair[1], ind_R=[0, 0])
    return tb_model

##############################################################################################


if __name__ == "__main__":
    from uniform_tilings_1 import UNITS
    from tiling import Tiling
    import matplotlib.pyplot as pyplot
    for unit in UNITS:
        tiling = Tiling().add_unit_pattern(unit)
        model = tb_from_tiling(tiling)
        tiling.render_unit(pyplot)
        model.visualize(0, dir_second=1)

##############################################################################################
