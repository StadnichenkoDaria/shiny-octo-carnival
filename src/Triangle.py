from src.Figure import Figure


class Triangle(Figure):

    # вычислить площать треугольника (S = 1/2 * a * h)
    def calculate_area(self, side_a, side_h):
        self.area = round(0.5 * side_a * side_h)
        return self.area

    # вычислить периметр треугольника (P = a + b + c)
    def calculate_perimeter(self, side_a, side_b, side_c):
        self.perimeter = side_a + side_b + side_c
        return self.perimeter



