import streamlit as st
import numpy as np

def display_latex_matrices_and_maxwell_equations():
    # Title and Subtitle
    st.title("How to Display LaTeX Matrices and Algebraic expressions")
    st.subheader("ML and AI for Financial Practitioners")

    # Text and Hyperlink
    st.markdown("I am a financial analyst writing technical documents. [More Information](https://www.google.com)")

    st.header("EXAMPLE 1 : 5x5 Matrix of Random Numbers")
    # Generate a 5x5 matrix of random numbers
    matrix = np.random.rand(5, 5)
    # Convert the matrix to a LaTeX formatted string
    matrix_latex = np.array2string(matrix, separator=' & ')
    matrix_latex = matrix_latex.replace('[', '').replace(']', '').replace(' &', ' & ').replace('\n', ' \\\\ ')
    # Display the matrix using LaTeX
    st.latex(r'\begin{bmatrix}' + matrix_latex + r'\end{bmatrix}')

    # Maxwell Equations
    st.header("EXAMPLE 2: Maxwell Equations")
    st.latex(r"""\begin{align*}
    \nabla \cdot \mathbf{E} &= \frac {\rho} {\varepsilon_0} \\
    \nabla \cdot \mathbf{B} &= 0 \\
    \nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
    \nabla \times \mathbf{B} &= \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial \mathbf{E}}{\partial t}
    \end{align*}""")

if __name__ == "__main__":
    display_latex_matrices_and_maxwell_equations()
