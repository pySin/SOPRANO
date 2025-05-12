# Handle mutations inside the immunopeptidome.

class OnMutations:

    def __init__(self, mutations_file, immunopeptidome_file):
        self.mutations_file = mutations_file
        self.immunopeptidome_file = immunopeptidome_file

    def on_mutations_data(self):

        on_mut_data = []

        # TO DO make sure the file is proper before opening
        # "with" closes the file after use so all data must be extracted before closing
        with open(self.mutations_file, "r", encoding="UTF8") as mf:
            # print(f"Mutations File: {mf}")

            for line in mf.readlines():
                on_mut_data.append(line.strip().split("	"))
        #         print(f"Read Line: {line}")
        # print(f"On Mutations Data: {on_mut_data}")
        # print(f"On Mutations Data: {len(on_mut_data)}")
        return on_mut_data

    def on_immunopeptidome_data(self):

        on_imnpptd_data = []

        with open(self.immunopeptidome_file, "r", encoding="UTF8") as i_file:
            for line in i_file.readlines():
                on_imnpptd_data.append(line.strip().split("	"))
        # print(f"In Immunopeptidome data: {on_imnpptd_data}")
        return on_imnpptd_data

    def mut_imnpptd_match(self):
        mut_trans_ids = [m_id[4] for m_id in self.on_mutations_data()]
        imm_trans_ids = [im[0] for im in self.on_immunopeptidome_data()]

        # print(f"Mutation IDs: {mut_trans_ids}")
        # print(f"Immunopeptidome IDs: {imm_trans_ids}")
        match_trans_ids = [match_id for match_id in mut_trans_ids if match_id in imm_trans_ids]
        # print(f"Match Trans: {match_trans_ids}")
        # print(f"Matches Length: {len(match_trans_ids)}")

    def on_dnds(self):
        on_m_data = self.on_mutations_data()
        print(f"On DnDsData: {on_m_data}")
        mutation_variants = [mut_v[6] for mut_v in on_m_data][1:]
        print(f"Mutations Variants: {mutation_variants}")
        print(f"Mutations Count: {len(mutation_variants)}")

        synonymous_mutations = mutation_variants.count("synonymous_variant")
        non_synonymous_mutations = mutation_variants.count("missense_variant")

        print(f"synonymous_mutations: {synonymous_mutations} - label 'synonymous_variant'")
        print(f"non_synonymous_mutations: {non_synonymous_mutations} - label 'missense_variant'")

        ratio = non_synonymous_mutations / len(mutation_variants)
        print(f"Ratio Non-Synonymous to Synonymous: {ratio}")



