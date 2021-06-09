from plotly import graph_objects as go
import numpy as np
from cmath import polar


def draw_bloch_sphere():
    rho = 1
    theta, phi = np.mgrid[0 : 2 * np.pi : 360j, 0 : np.pi : 180j]
    x = rho * np.cos(-phi) * np.sin(theta)
    y = rho * np.sin(-phi) * np.sin(theta)
    z = rho * np.cos(theta)

    fig = go.Figure(
        go.Surface(
            x=x,
            y=y,
            z=z,
            opacity=0.2,
            surfacecolor=x ** 2 + y ** 2 + z ** 2,
            contours={
                "z": {
                    "show": True,
                    "start": -1,
                    "end": 1,
                    "size": 0.25,
                    "color": "azure",
                }
            },
            colorscale="bluered",
            showscale=False,
        )
    )
    fig.add_trace(
        go.Scatter3d(
            x=[-1, 1],
            y=[0, 0],
            z=[0, 0],
            mode="lines+markers",
            marker={"size": 1},
            line={"color": "black"},
        )
    )

    fig.add_trace(
        go.Scatter3d(
            x=[0, 0],
            y=[-1, 1],
            z=[0, 0],
            mode="lines+markers",
            marker={"size": 1},
            line={"color": "black"},
        )
    )
    fig.add_trace(
        go.Scatter3d(
            x=[0, 0],
            y=[0, 0],
            z=[-1, 1],
            mode="lines+markers",
            marker={"size": 1},
            line={"color": "black"},
        )
    )
    fontsize = 16
    fig.update_layout(
        scene=dict(
            annotations=[
                dict(
                    text="qubit0",
                    font={"size": fontsize},
                    x=0,
                    y=0,
                    z=1.5,
                    showarrow=False,
                ),
                dict(
                    text="|0>",
                    font={"size": fontsize},
                    x=0,
                    y=0,
                    z=1.2,
                    showarrow=False,
                ),
                dict(
                    text="|1>",
                    font={"size": fontsize},
                    x=0,
                    y=0,
                    z=-1.2,
                    showarrow=False,
                ),
                dict(
                    text="|+>",
                    font={"size": fontsize},
                    x=0,
                    y=1.2,
                    z=0,
                    showarrow=False,
                ),
                dict(
                    text="|->",
                    font={"size": fontsize},
                    x=0,
                    y=-1.2,
                    z=0,
                    showarrow=False,
                ),
            ],
            camera_eye={"x": -1, "y": 1.32, "z": 0.6},
        ),
        showlegend=False,
    )
    return fig


def plot_statevector(st, use_fig=None):
    st_copy = st.copy()
    phi0 = polar(st_copy[0])[1]
    phi1 = polar(st_copy[1])[1]
    req_phi = phi0 - phi1

    st_copy[0] = st_copy[0] / np.exp(1.0j * phi0)
    st_copy[1] = st_copy[1] / np.exp(1.0j * phi1)
    req_theta = 2 * np.arccos(st_copy[0])

    rho = 1
    plot_y = rho * np.cos(req_phi) * np.sin(req_theta)
    plot_x = rho * np.sin(req_phi) * np.sin(req_theta)
    plot_z = rho * np.cos(req_theta)
    plot_x, plot_y, plot_z = map(lambda x: x.real, (plot_x, plot_y, plot_z))

    if use_fig is None:
        fig = draw_bloch()
    else:
        fig = use_fig

    fig.add_trace(
        go.Scatter3d(
            x=[0, plot_x],
            y=[0, plot_y],
            z=[0, plot_z],
            mode="lines",
            line=dict(color="black", width=2),
        )
    )

    fig.add_trace(
        go.Cone(
            anchor="tip",
            x=[plot_x],
            y=[plot_y],
            z=[plot_z],
            u=[plot_x],
            v=[plot_y],
            w=[plot_z],
            sizemode="absolute",
            sizeref=0.15,
            colorscale="twilight",
            showscale=False,
        )
    )

    return fig
