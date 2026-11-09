class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _stringify_dependencies(self, dependencies):
        # output:
        #Dependencies:
        #- python
        #- Flask
        #- editdistance
        for dependency in dependencies:
            return "\n".join([f"- {dependency.split(">=")[0]}" for dependency in dependencies])
        
    def _stringfy_authorDict(self):
        # esimerkki: [{'name': 'Matti Luukkainen'}, {'name': 'Kalle Ilves'}]
        # output: 
        # Author:
        # - Matti Luukkainen
        # - Kalle Ilves
        for author in self.authors:
            return "\n".join([f"- {author['name']}" for author in self.authors])



    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description}"
            f"\nLicense: {self.license}"
            "\n"
            f"\nAuthors: \n{self._stringfy_authorDict()}"
            "\n"
            f"\nDependencies: \n{self._stringify_dependencies(self.dependencies)}"
            "\n"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
