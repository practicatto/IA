import porespy as ps
import numpy as np


def pore_size_distribution(porous):
    porous_porosimetry = ps.filters.porosimetry(porous)
    psd = ps.metrics.pore_size_distribution(im=porous_porosimetry)
    return {"pdf": psd.pdf,
            "cdf": psd.cdf,
            "bin_widths": psd.bin_widths}


def tortuosity(porous):
    tau = ps.simulations.tortuosity_fd(im=porous, axis=1).__dict__
    tau["value"] = tau.pop("tortuosity")
    tau.pop("concentration")
    return tau


def porosity_profile(porous):
    return {"axis_x": ps.metrics.porosity_profile(porous, axis=0),
            "axis_y": ps.metrics.porosity_profile(porous, axis=1),
            "axis_z": ps.metrics.porosity_profile(porous, axis=2)}


def metrics(porous):
    return {"psd": pore_size_distribution(porous),
            "tortuosity": tortuosity(porous),
            "porosity_profile": porosity_profile(porous)}


def compare_psd(medium_1, medium_2):
    psd_1 = pore_size_distribution(medium_1)
    psd_2 = pore_size_distribution(medium_2)
    pdf = np.mean(psd_1['pdf'] != psd_2['pdf'])
    cdf = np.mean(psd_1['cdf'] != psd_2['cdf'])
    bin_widths = np.mean(psd_1['bin_widths'] != psd_2['bin_widths'])
    return {"pdf": pdf,
            "cdf": cdf,
            "bin_widths": bin_widths}


def compare_tau(medium_1, medium_2):
    tau_1 = tortuosity(medium_1)
    tau_2 = tortuosity(medium_2)
    tortuosity_error = (
        np.abs(tau_1["value"]-tau_2["value"])/tau_1["value"])*100
    return tortuosity_error


def compare_porosity_profile(medium_1, medium_2):
    porosity_profile_1 = porosity_profile(medium_1)
    porosity_profile_2 = porosity_profile(medium_2)
    axis_x = np.mean(
        porosity_profile_1['axis_x'] != porosity_profile_2['axis_x'])
    axis_y = np.mean(
        porosity_profile_1['axis_y'] != porosity_profile_2['axis_y'])
    axis_z = np.mean(
        porosity_profile_1['axis_z'] != porosity_profile_2['axis_z'])
    return {"axis_x": axis_x,
            "axis_y": axis_y,
            "axis_z": axis_z}


def compare_metrics(medium_1, medium_2):
    return {"psd": compare_psd(medium_1, medium_2),
            "tortuosity": compare_tau(medium_1, medium_2),
            "porosity_profile": compare_porosity_profile(medium_1, medium_2)}
