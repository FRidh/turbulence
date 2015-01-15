import numpy as np
from scipy.special import gamma
from scipy.special import kv as besselk
from scipy.integrate import cumtrapz
import numexpr as ne


def logamp_spherical_variance():
    """Variance of the log-amp squared.
    
    See "Acoustics in Moving Inhomogeneous Media", page 213.
    """
    
    return np.sqrt(np.pi)*k**2.0*l*x/8.0 *((1.0-M)*sigma_eps)
    
    
    pass



def phase_spherical_variance():
    """Variance of the phase squared.
    
    See "Acoustics in Moving Inhomogeneous Media", page 213.
    """
    pass


#def covariance():
    #"""Covariance. Wind and temperature fluctuations.
    #"""
    #pass

#def covariance_temperature():
    #"""Covariance. Temperature fluctuations only.
    #"""
    #pass


def covariance_wind(f, c0, rho, distance, L, Cv, steps=10, initial=0.001):
    """Covariance. Wind fluctuations only.
    
    :param f: Frequency
    :param c0: Speed of sound
    :param rho: Spatia separation
    :param distance: Distance
    :param L: Correlation length
    :param Cv: Variance of wind speed
    :param initial: Initial value
    
    
    """
    f = np.asarray(f)
    k = 2.*np.pi*f / c0
    K0 = 2.*np.pi / L
    
    A = 5.0/(18.0*np.pi*gamma(1./3.)) # Equation 11, see text below. Approximate result is 0.033
    gamma_v = 3./10.*np.pi**2.*A*k**2.*K0**(-5./3.)*4.*(Cv/c0)**2.  # Equation 28, only wind fluctuations

    krho = k * rho
    
    t = krho[:, None] * np.linspace(0.00000000001, 1., steps) # Fine discretization for integration

    #t[t==0.0] = 1.e-20

    gamma56 = gamma(5./6.)
    bessel56 = besselk(5./6., t)
    bessel16 = besselk(1./6., t)
    
    integration = cumtrapz(ne.evaluate("2.0**(1./6.)*t**(5./6.)/gamma56 * (bessel56 - t/2.0 * bessel16 )"), initial=initial)[:,-1]
    B = ne.evaluate("2.0*gamma_v * distance / krho * integration")
    
    #B = 2.0*gamma_v * distance / krho * cumtrapz((2.0**(1./6.)*t**(5./6.)/gamma(5./6.) * (besselk(5./6., t) - t/2.0*besselk(1./6., t)) ), initial=initial)[:,-1]
    return B


