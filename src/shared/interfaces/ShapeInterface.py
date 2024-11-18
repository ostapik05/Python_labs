from abc import ABC, abstractmethod

# Base class for shapes (Interface)
class Shape(ABC):
    @abstractmethod
    def calculate_coordinates(self, A, B, theta, phi):
        """Calculate coordinates for the shape"""
        pass
