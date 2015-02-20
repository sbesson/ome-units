#!/usr/bin/env python

from sympy import symbols as symbols
from sympy import Eq

NAME = "TEMPERATURE"

k, c, f, r = symbols("k c f r")

equations = (
    Eq(c, k + 273.15),
    Eq(r, k * 5 / 9),
    Eq(f, r + 459.67),
)

units = {
    k: "KELVIN",
    c: "CELSIUS",
    f: "FAHRENHEIT",
    r: "RANKINE",
}