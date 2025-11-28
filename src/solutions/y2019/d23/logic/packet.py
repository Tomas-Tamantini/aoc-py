from dataclasses import dataclass


@dataclass(frozen=True)
class Packet:
    origin: int
    destination: int
    x: int
    y: int
