# UNAL-Trabajos

Coursework from **Universidad Nacional de Colombia** (UNAL), currently covering
celestial mechanics.

> Course material and code comments are in **Spanish**.

## Contents

### `Mecanica-Celeste/` — Celestial Mechanics

**`VariablesMovimientoMercurioT2/`** — computing orbital motion variables for
Mercury from a state vector.

Given a position **r** and velocity **v** in heliocentric coordinates, the code
derives the quantities that describe the orbit at that instant:

| Quantity | Symbol | How it's obtained |
|---|---|---|
| Heliocentric distance | *d* | ‖**r**‖, in astronomical units |
| Orbital speed | *v* | ‖**v**‖, in AU/day and converted to km/s |
| Specific angular momentum | **h** | **r** × **v** |
| Flight path angle | *θ* | arcsin(‖**h**‖ / (*d* · *v*)), reported in degrees, arcminutes, and arcseconds |
| Radial velocity | *v<sub>r</sub>* | (**r** · **v**) / *d* |

The AU/day → km/s conversion uses the IAU astronomical unit,
149 597 870.7 km, over 86 400 s.

| File | Role |
|---|---|
| `script_simplificado.py` | Compact, dependency-light version. Run it directly to print results for both assigned Mercury state vectors. |
| `script_variables_mercurio_t2.py` | The fuller working script. |
| `notebook_variables_mercurio.ipynb` | The same analysis as a notebook, with the derivations written out. |

## Setup

The project uses [Poetry](https://python-poetry.org/) and requires **Python 3.13
or newer**.

```bash
poetry install
```

Dependencies are `pandas`, `numpy`, and `matplotlib`, plus `ipykernel` in the dev
group for running the notebooks.

## Running

```bash
poetry run python Mecanica-Celeste/VariablesMovimientoMercurioT2/script_simplificado.py
```

This prints, for each of the two assigned state vectors, a line of distance and
speed, a line of angular momentum and flight path angle, and the radial
velocity.

For the notebook:

```bash
poetry run jupyter notebook
```

## Related

[`celestian-mechanics-calculations-api`](https://github.com/JsNcAr/celestian-mechanics-calculations-api)
and
[`celestial-mechanics-calculations-frontend`](https://github.com/JsNcAr/celestial-mechanics-calculations-frontend)
turn this kind of calculation into a web service.

## License

MIT — see [`LICENSE`](LICENSE).
