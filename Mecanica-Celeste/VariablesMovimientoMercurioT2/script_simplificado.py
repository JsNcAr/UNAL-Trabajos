import numpy as np

def calc(posicion, velocidad):
    distancia = round(np.linalg.norm(posicion), 8)
    vel_orbital = round(np.linalg.norm(velocidad), 8)
    vel_km_s = round(vel_orbital * 149597870.7 / 86400, 8)
    momento = np.round(np.cross(posicion, velocidad), 8)
    mag_momento = round(np.linalg.norm(momento), 8)
    vel_radial = round(np.dot(posicion, velocidad) / distancia, 8)
    sin_theta = np.clip(mag_momento / (distancia * vel_orbital), -1, 1)
    angulo_deg = np.degrees(np.arcsin(sin_theta))
    g = int(angulo_deg)
    m = int((angulo_deg - g) * 60)
    s = round(((angulo_deg - g) * 60 % 1) * 3600, 8)
    return distancia, vel_orbital, vel_km_s, momento, mag_momento, (g, m, s), vel_radial

def print_res(posicion, velocidad):
    d, v_o, v_km, h, h_m, angle, v_r = calc(posicion, velocidad)
    print(f"d={d} UA | v={v_o} UA/d | {v_km} km/s")
    print(f"h={h} | |h|={h_m} | θ={angle[0]}°{angle[1]}'{angle[2]}''")
    print(f"vr={v_r}")

if __name__ == "__main__":
    print("PUNTO 1: Mercurio Base")
    print_res(np.array([-0.10553660, 0.29576302, 0.03385018]),
              np.array([-0.03214728, -0.00841247, 0.00226123]))
    
    print("\nPUNTO 2: Efemérides de Mercurio")
    print_res(np.array([0.34862821, 0.023351436, -0.03006949]),
              np.array([-0.00731419, 0.02932921, 0.00306770]))
