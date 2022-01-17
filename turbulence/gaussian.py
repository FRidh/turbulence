import numpy as np
import numexpr as ne


def wave_parameter(wavenumber, x, l):
    """
    The wave parameter :math:`D`.

    :param wavenumber: Wavenumber

    See page 208.
    """
    return 4.0 * x / (wavenumber * l ** 2.0)


def _MD(omega, delta):
    """
    See page 210
    """
    return ne.evaluate(
        "arctan( sqrt(2.0/omega) + omega*delta/2.0 * log((1.0+delta*sqrt(2.0*omega))/(1.0-delta*sqrt(2.0*omega))) ) / (delta**2.0*(omega+1.0)*sqrt(8.0*omega))"
    )


def _ND(omega, delta):
    """
    See page 210
    """
    return ne.evaluate(
        "((omega*(omega+2.0))/(2.0*(omega+1.0)**2.0)) * (1.0 + (sqrt(2*omega)*(omega+3.0)*arctan(sqrt(2.0/omega)))/(4.0*(omega+1.0)) + (delta*sqrt(2.0*omega)*(omega-1.0)*(omega+2.0)*log((1.0+delta*sqrt(2.0*omega))/(1.0-delta*sqrt(2.0*omega))) ) / (8.0*(omega+1.0)) )"
    )


# def variances_spherical(wavenumber, l, x, sigma_T, sigma_w, soundspeed=343.0):
#     """
#     See equation 7.100 and 7.101.
#     """
#     delta = D / 4.0
#     omega = np.sqrt(1.0 + delta ** (-2.0))

#     M = _MD(omega, delta)
#     N = _ND(omega, delta)

#     logamp = ne.evaluate(
#         "sqrt(np.pi)*wavenumber**2.0*l*x/8.0 *((1.0-M)*sigma_T + (1.0-N)*4*(sigma_w/soundspeed)**2.0)"
#     )  # Equation 7.100
#     phase = ne.evaluate(
#         "sqrt(np.pi)*wavenumber**2.0*l*x/8.0 *((1.0+M)*sigma_T + (1.0+N)*4*(sigma_w/soundspeed)**2.0)"
#     )  # Equation 7.101

#     return logamp, phase
