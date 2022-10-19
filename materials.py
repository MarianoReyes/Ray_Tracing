from material import Material
from color import color

ivory = Material(
    diffuse=color(220, 220, 200),
    albedo=(0.6, 0.3, 0.1, 0),
    spec=50,
    refractive_index=0
)
rubber = Material(
    diffuse=color(180, 0, 0),
    albedo=(0.9, 0.1, 0, 0, 0),
    spec=10,
    refractive_index=0
)
mirror = Material(
    diffuse=color(255, 255, 255),
    albedo=(0, 10, 0.8, 0),
    spec=1425,
    refractive_index=0
)
glass = Material(
    diffuse=color(150, 180, 200),
    albedo=(0, 0.5, 0.1, 0.8),
    spec=125,
    refractive_index=1.5
)
