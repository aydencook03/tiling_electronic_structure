import pythtb as tb

##############################################################################################


def tb_from_tiling(tiling, onsite_en=0.0, hop_amp=-1.0):
    """
    Takes a tiling with associated unit cell data and generates a tight-binding model from it.
    Onsite energies can be specified as a single uniform value or as a list of values corresponding to
        each individual orbital. If you need to know which orbital has which index, use the render_unit method.
    Hopping amplitudes can be specified as a single uniform value or as a list of values corresponding to
        each individual hopping pair (edge). If you need to know the index of each edge, use the render_unit method.
    """
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
        # Set hoppings within the same unit cell
        tb_model.set_hop(hop_amp[i], pair[0], pair[1], ind_R=[0, 0])
        # Add selective inter-unit cell hoppings
        '''if tiling.is_boundary_pair(pair):
            tb_model.set_hop(hop_amp[i], pair[0], pair[1], ind_R=[1, 0])
            tb_model.set_hop(hop_amp[i], pair[0], pair[1], ind_R=[0, 1])'''
    return tb_model


def plot_band_structure(pyplot, tb_model, mesh_size=(50, 50), title="Band Structure", legend=False):
    """
    Calculate and plot the band structure of the tiling.
    """
    k_mesh = tb_model.k_uniform_mesh(mesh_size)
    eigen_vals = tb_model.solve_all(k_mesh)
    fig = pyplot.figure(title)
    ax = fig.add_subplot()
    pyplot.title(title)
    for i, band in enumerate(eigen_vals):
        ax.plot(band, label="Band {}".format(i+1))
    ax.set_xlabel("k-point index")
    ax.set_ylabel("Energy")
    pyplot.legend() if legend else None
    pyplot.show()

##############################################################################################


'''
if __name__ == "__main__":
    from uniform_tilings_1 import UNITS
    from tiling import Tiling
    import matplotlib.pyplot as pyplot
    for unit in UNITS:
        tiling = Tiling().add_unit_pattern(unit)
        model = tb_from_tiling(tiling)
        # tiling.render_unit(pyplot, title="Tiling Unit: "+unit.__name__)
        # tiling.render_full(pyplot, title="Full Tiling: "+unit.__name__)
        # model.visualize(0, dir_second=1)
        plot_band_structure(
            pyplot, model, title="Band Structure: "+unit.__name__)
'''

if __name__ == "__main__":
    from uniform_tilings_1 import hexagon_square_triangle as unit
    from tiling import Tiling
    import matplotlib.pyplot as pyplot
    tiling = Tiling().add_unit_pattern(unit, depth=2)
    model = tb_from_tiling(tiling)
    tiling.render_unit(pyplot, title="Tiling Unit: "+unit.__name__)
    tiling.render_full(pyplot, title="Full Tiling: "+unit.__name__)
    model.visualize(dir_first=0, dir_second=1, draw_hoppings=True)
    plot_band_structure(
        pyplot, model, title="Band Structure: "+unit.__name__)

##############################################################################################
