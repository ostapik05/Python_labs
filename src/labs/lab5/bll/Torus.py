from shared.interfaces.ShapeInterface import Shape
from math import cos, sin

class Torus(Shape):
    def __init__(self, R1, R2, K1, K2):
        super().__init__()
        self.R1 = R1
        self.R2 = R2
        self.K1 = K1
        self.K2 = K2

    def set_parameters(self, R1, R2):
        self.R1 = R1
        self.R2 = R2

    def calculate_coordinates(self, A, B, theta, phi):
        cosA, sinA = cos(A), sin(A)
        cosB, sinB = cos(B), sin(B)
        costheta, sintheta = cos(theta), sin(theta)
        cosphi, sinphi = cos(phi), sin(phi)

        circlex = self.R2 + self.R1 * costheta
        circley = self.R1 * sintheta

        x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
        y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
        z = self.K2 + cosA * circlex * sinphi + circley * sinA

        if z == 0:
            return None

        ooz = 1 / z
        xp = self.K1 * ooz * x
        yp = self.K1 * ooz * y

        return xp, yp, ooz