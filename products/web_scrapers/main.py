from .altex import Altex
from .emag import Emag
from .evomag import Evomag
from .flanco import Flanco
from .media_galaxy import MediaGalaxy
from .pc_garage import PcGarage

def run_scrapers():
    Altex()
    Emag()
    Evomag()
    Flanco()
    MediaGalaxy()
    PcGarage()
