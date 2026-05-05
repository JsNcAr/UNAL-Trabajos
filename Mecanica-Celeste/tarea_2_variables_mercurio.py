"""
Mercury orbital variables calculation module.

This script calculates various orbital parameters for Mercury based on 
position and velocity vectors in astronomical units (AU).
"""

import numpy as np


def getDistance(posicion):
    """Calculate the magnitude of the position vector."""
    distancia = np.linalg.norm(posicion)
    return round(distancia, 8)


def getOrbitalVelocity(velocidad):
    """Calculate the magnitude of the orbital velocity vector."""
    velocidad_orbital = np.linalg.norm(velocidad)
    return round(velocidad_orbital, 8)


def getOrbitalVelocityKm_s(velocidad_orbital):
    """Convert orbital velocity from UA/day to km/s."""
    unidad_ua_km = 149597870.7  # km
    unidad_dia_s = 24 * 3600  # s
    velocidad_km_s = velocidad_orbital * unidad_ua_km / unidad_dia_s
    return round(velocidad_km_s, 8)


def getMomentumAngularPerUnitMass(posicion, velocidad):
    """Calculate the angular momentum per unit mass (h = r x v)."""
    h = np.cross(posicion, velocidad)
    return np.round(h, 8)


def getMagnitudeMomentumAngularPerUnitMass(h):
    """Calculate the magnitude of the angular momentum per unit mass."""
    h_magnitud = np.linalg.norm(h)
    return round(h_magnitud, 8)


def getAngleBetweenPositionAndVelocity(h_magnitud, distancia, velocidad_orbital):
    """
    Calculate the angle between position and velocity vectors.
    
    Uses the formula: h = r * v * sin(theta)
    Where:
        h = magnitude of angular momentum per unit mass
        r = distance (magnitude of position vector)
        v = orbital velocity (magnitude of velocity vector)
        theta = angle between position and velocity vectors
    
    Returns the angle in degrees, minutes, and seconds.
    """

    sin_theta = h_magnitud / (distancia * velocidad_orbital)
    # Aseguramos que el valor esté en el rango [-1, 1] para evitar errores en arcsin
    sin_theta = np.clip(sin_theta, -1, 1)

    theta_rad = np.arcsin(sin_theta)
    
    # Convertimos el ángulo a grados
    theta_deg = np.degrees(theta_rad)
    
    # Convertimos a grados minutos segundos
    grados = int(theta_deg)
    minutos = int((theta_deg - grados) * 60)
    segundos = (theta_deg - grados - minutos / 60) * 3600
    
    return grados, minutos, segundos


def getRadialVelocity(posicion, velocidad):
    """Calculate the radial component of velocity (velocity along position vector)."""
    r_magnitud = np.linalg.norm(posicion)
    radial_velocity = np.dot(posicion, velocidad) / r_magnitud
    return round(radial_velocity, 8)


def calculate_mercury_parameters(posicion, velocidad):
    """
    Calculate orbital parameters for Mercury given position and velocity vectors.
    
    Parameters:
    -----------
    posicion : np.array
        Position vector in AU
    velocidad : np.array
        Velocity vector in UA/día
    
    Returns:
    --------
    dict : Dictionary containing all calculated parameters
    """
    distancia = getDistance(posicion)
    velocidad_orbital = getOrbitalVelocity(velocidad)
    velocidad_km_s = getOrbitalVelocityKm_s(velocidad_orbital)
    h = getMomentumAngularPerUnitMass(posicion, velocidad)
    h_magnitud = getMagnitudeMomentumAngularPerUnitMass(h)
    angulo = getAngleBetweenPositionAndVelocity(h_magnitud, distancia, velocidad_orbital)
    velocidad_radial = getRadialVelocity(posicion, velocidad)
    
    return {
        'distancia': distancia,
        'velocidad_orbital': velocidad_orbital,
        'velocidad_km_s': velocidad_km_s,
        'momento_angular': h,
        'magnitud_momento_angular': h_magnitud,
        'angulo': angulo,
        'velocidad_radial': velocidad_radial
    }


def print_mercury_results(label, params):
    """Print formatted orbital parameters."""
    print(f"\n{label}")
    print(f"Distancia de Mercurio al Sol: {params['distancia']} UA")
    print(f"Velocidad orbital de Mercurio: {params['velocidad_orbital']} UA/día")
    print(f"Velocidad orbital de Mercurio: {params['velocidad_km_s']} km/s")
    print(f"Vector de momento angular por unidad de masa (h): {params['momento_angular']} UA^2/día")
    print(f"Magnitud del vector de momento angular por unidad de masa (h): {params['magnitud_momento_angular']} UA^2/día")
    grados, minutos, segundos = params['angulo']
    print(f"Ángulo entre el vector de posición y el vector de velocidad: {grados}° {minutos}' {round(segundos, 8)}''")
    print(f"Velocidad radial de Mercurio: {params['velocidad_radial']} UA/día")


if __name__ == "__main__":
    # Mercury Base Data (Punto 1)
    print("=" * 60)
    print("PUNTO 1: Mercurio Base")
    print("=" * 60)
    
    posicion_1 = np.array([-0.10553660, 0.29576302, 0.03385018])  # UA
    velocidad_1 = np.array([-0.03214728, -0.00841247, 0.00226123])  # UA/día
    
    params_1 = calculate_mercury_parameters(posicion_1, velocidad_1)
    print_mercury_results("", params_1)
    
    # Mercury Ephemerides Data (Punto 2)
    print("\n" + "=" * 60)
    print("PUNTO 2: Efemérides de Mercurio")
    print("=" * 60)
    
    posicion_2 = np.array([0.34862821, 0.023351436, -0.03006949])  # UA
    velocidad_2 = np.array([-0.00731419, 0.02932921, 0.00306770])  # UA/día
    
    params_2 = calculate_mercury_parameters(posicion_2, velocidad_2)
    print_mercury_results("", params_2)


