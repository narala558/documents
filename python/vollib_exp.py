from py_vollib.black_scholes.greeks import analytical
from py_vollib.black_scholes.greeks import numerical

x = 'c', 10186, 10400, 10 / 250, 7.5, 11.5
print(analytical.delta(*x))
print(numerical.delta(*x))
