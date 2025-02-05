from dataclasses import dataclass
from zipfile import ZipFile

@dataclass
class FastAndTheFurious:
    name: str
    description: str

movies = [
    FastAndTheFurious(
        name="The Fast and the Furious",
        description="Street racer Brian O'Conner is recruited by the police to infiltrate a criminal gang."),
    FastAndTheFurious(
        name="2 Fast 2 Furious",
        description="Brian O'Conner teams up with an ex-con to bring down a Miami drug lord."),
    FastAndTheFurious(
        name="The Fast and the Furious: Tokyo Drift",
        description="A high school student gets involved in the Tokyo drift racing scene."),
    FastAndTheFurious(
        name="Fast & Furious",
        description="Dominic Toretto and Brian O'Conner join forces to take down a heroin importer."),
    FastAndTheFurious(
        name="Fast Five",
        description="Dominic Toretto and his crew plan a massive heist to buy their freedom."),
    FastAndTheFurious(
        name="Fast & Furious 6",
        description="Dominic Toretto and his team help the government take down a skilled mercenary group."),
    FastAndTheFurious(
        name="Furious 7",
        description="Dominic Toretto and his crew face off against a terrorist who seeks revenge."),
    FastAndTheFurious(
        name="The Fate of the Furious",
        description="Dominic Toretto turns against his team when he is blackmailed by a cyberterrorist."),
    FastAndTheFurious(
        name="F9",
        description="Dominic Toretto and his family face off against Dom's younger brother, who is working with a dangerous technology."),
]


with ZipFile('FastAndTheFurious.zip', mode='a') as arch:
    for movie in movies:
        arch.writestr(zinfo_or_arcname=f'{movie.name}.txt', data=movie.description)