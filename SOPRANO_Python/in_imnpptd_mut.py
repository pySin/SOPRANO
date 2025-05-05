# Handle mutations inside the immunopeptidome.

class OnMutations:

    def __init__(self, mutations_file, immunopeptidome_file):
        self.mutations_file = mutations_file
        self.immunopeptidome_file = immunopeptidome_file

    def open_mutations_file(self):

        # TODO make sure the file is proper befor opening
        with open(self.mutations_file, "r") as mf:
            print(f"Mutations File: {mf}")


