from dataclasses import dataclass


@dataclass
class Confini:
    state1no: int
    state2no: int
    year: int

    def __hash__(self):
        return (self.state1no, self.state2no)

    def __str__(self):
        return f"stampa confine"


