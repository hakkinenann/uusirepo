class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_arrays(self, array):
        if len(array) < 1: return "-"
        palautettava = ""
        indeksi = 0
        for x in array:
            if indeksi == len(array)-1:
                palautettava = palautettava + "- " + x
            else:
                palautettava = palautettava + "- " + x +"\n"
                indeksi = indeksi + 1
        return palautettava
    
    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors: \n{self._stringify_arrays(self.authors)}"
            f"\n"
            f"\nDependencies: \n{self._stringify_arrays(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: \n{self._stringify_arrays(self.dev_dependencies)}"
        )
