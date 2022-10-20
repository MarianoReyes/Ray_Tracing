from material import *
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

grass = Material(
    diffuse=color(100, 255, 100),
    albedo=(0.6, 0.3, 0.1, 0),
    spec=50,
    refractive_index=0
)

logg = Material(
    diffuse=color(101, 67, 33),
    albedo=(0.9, 0.1, 0, 0),
    spec=10,
    refractive_index=0
)

leaves = Material(
    diffuse=color(0, 143, 57),
    albedo=(0.9, 0.1, 0, 0),
    spec=50,
    refractive_index=0
)

water = Material(
    diffuse=color(0, 114, 133),
    albedo=(0.9, 0.1, 0.1, 1.333),
    spec=125,
    refractive_index=0.1
)

grass2 = Material(
    texture=Texture('grama.bmp')
)
