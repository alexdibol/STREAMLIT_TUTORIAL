import streamlit as st
import math
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    d = b ** 2 - 4 * a * c

    # Compute the two solutions
    sol1 = sol2 = None
    if d >= 0:
        sol1 = (-b + math.sqrt(d)) / (2 * a)
        sol2 = (-b - math.sqrt(d)) / (2 * a)

    return sol1, sol2
def main():
    st.title('Quadratic Equation Solver')

    # Input fields for coefficients
    a = st.number_input('Enter coefficient a', value=1.0, format='%f')
    b = st.number_input('Enter coefficient b', value=1.0, format='%f')
    c = st.number_input('Enter coefficient c', value=1.0, format='%f')

    # Button to calculate solutions
    if st.button('Solve Equation'):
        sol1, sol2 = solve_quadratic(a, b, c)
        if sol1 is not None and sol2 is not None:
            st.success(f'The solutions are {sol1} and {sol2}')
        else:
            st.error('No real solutions')


if __name__ == '__main__':
    main()
