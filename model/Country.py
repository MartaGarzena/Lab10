from dataclasses import dataclass


@dataclass
class Country:
    CCode: int
    StateAbbr: str
    StateName: str


    def __hash__(self):
        return self.CCode

    def __str__(self):
        return f"stampa country {self.StateAbbr}"

    def __eq__(self, other):
        return self.CCode == other.CCode
