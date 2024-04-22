from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)
        tietorakenteen_eka_kerros = parsed_toml["tool"]
        tietorakenteen_toka_kerros = tietorakenteen_eka_kerros["poetry"]
        tietorakenteen_kolmas_kerros = tietorakenteen_toka_kerros["group"]
        tietorakenteen_neljas_kerros = tietorakenteen_kolmas_kerros["dev"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(tietorakenteen_toka_kerros["name"], tietorakenteen_toka_kerros["description"], tietorakenteen_toka_kerros["license"], tietorakenteen_toka_kerros["authors"], tietorakenteen_toka_kerros["dependencies"], tietorakenteen_neljas_kerros["dependencies"])
