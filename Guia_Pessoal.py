# Arquivo espelhado com a versão mais recente do VocêEncontra 24H
import os
import json
import webbrowser
import datetime
import re
import requests
import flet as ft
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

from main import main, SERVICOS_APP, Icons, Colors

if __name__ == "__main__":
    if hasattr(ft, "run"):
        try:
            ft.run(main)
        except TypeError:
            ft.run(target=main)
    elif hasattr(ft, "app"):
        ft.app(target=main)
