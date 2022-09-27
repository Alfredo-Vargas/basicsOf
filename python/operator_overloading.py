from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Vector:
    x: float
    y: float

    # Implementing donder methods
    def __truediv__(self, other: float) -> Vector:
        return Vector(self.x / other, self.y / other)
    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)





def main() -> None:
    vector = Vector(1, 2)
    print(vector / 2)
    print(vector + vector / 2)


if __name__ == "__main__":
    main()

