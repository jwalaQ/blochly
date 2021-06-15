# Blochly

Bloch sphere using plotly.

See `bloch_plotly.mp4` for example.

The example is created by passing the statevector:

stv = [0.65328148-0.27059805j, 0.65328148+0.27059805j]

to `plot_statevector` function written in base.py.  

`stv` is obtained by the simple circuit:

q_0: ----|  H  |----|  Rz(pi/4)  |----
