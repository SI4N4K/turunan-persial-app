import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("Aplikasi Turunan Parsial")

# Definisikan simbol
x, y = sp.symbols('x y')

# Input fungsi dari pengguna
fungsi_str = st.text_input("Masukkan fungsi f(x, y):", "x**2 * y + y**3")

try:
    # Konversi string ke ekspresi sympy
    f = sp.sympify(fungsi_str)
    # Hitung turunan parsial
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    # Tampilkan fungsi dan turunannya dalam LaTeX
    st.latex(f"f(x, y) = {sp.latex(f)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")

    # Input titik evaluasi
    x0 = st.number_input("Nilai x0:", value=1.0)
    y0 = st.number_input("Nilai y0:", value=2.0)

    # Hitung nilai fungsi dan gradien di titik (x0, y0)
    f_val = f.subs({x: x0, y: y0})
    fx_val = fx.subs({x: x0, y: y0})
    fy_val = fy.subs({x: x0, y: y0})

    st.write(f"Nilai fungsi di titik ({x0}, {y0}):", f_val)
    st.write(f"Gradien di titik ({x0}, {y0}):", (fx_val, fy_val))

    st.subheader("Grafik Permukaan & Bidang Singgung")

    # Buat grid untuk plot
    x_vals = np.linspace(x0 - 2, x0 + 2, 50)
    y_vals = np.linspace(y0 - 2, y0 + 2, 50)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Fungsi numpy dari fungsi sympy
    f_np = sp.lambdify((x, y), f, 'numpy')
    Z = f_np(X, Y)

    # Hitung bidang singgung
    Z_tangent = float(f_val) + float(fx_val) * (X - x0) + float(fy_val) * (Y - y0)

    # Plot permukaan dan bidang singgung
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')
    ax.plot_surface(X, Y, Z_tangent, alpha=0.5, color='red')
    ax.set_title("Permukaan f(x, y) dan bidang singgungnya")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')

    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
