# Handle mutations inside the immunopeptidome.
import os

class OnMutations:

    def __init__(self, mutations_file, immunopeptidome_file):
        self.mutations_file = mutations_file
        self.immunopeptidome_file = immunopeptidome_file
        self.mutations_data = None
        self.immunopeptidome_data = None
        self.report_file = ""

    def report_file_folder(self, file_name):
        folder = "report_files"
        os.makedirs(folder, exist_ok=True)
        self.report_file = open(f"{folder}/{file_name}", "a")

    def mutations_data_calc(self):

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
        self.mutations_data = on_mut_data

    def immunopeptidome_data_calc(self):

        imnpptd_data = []

        with open(self.immunopeptidome_file, "r", encoding="UTF8") as i_file:
            for line in i_file.readlines():
                imnpptd_data.append(line.strip().split("	"))
        # print(f"In Immunopeptidome data: {imnpptd_data}")
        self.immunopeptidome_data = imnpptd_data

    def mut_imnpptd_match(self):
        mut_trans_ids = [m_id[4] for m_id in self.mutations_data][1:]
        imm_trans_ids = [im[0] for im in self.immunopeptidome_data]

        # print(f"Mutation IDs count: {len(mut_trans_ids)}")
        # print(f"First Mutations records: {mut_trans_ids[0:3]}")
        # print(f"Immunopeptidome IDs: {imm_trans_ids}")
        match_trans_ids = [match_id for match_id in mut_trans_ids if match_id in imm_trans_ids]
        non_match_trans_ids = [match_id for match_id in mut_trans_ids if match_id not in imm_trans_ids]
        # print(f"Match Trans: {match_trans_ids}")
        # print(f"Matches Length: {len(match_trans_ids)}")
        self.report_file.write(f"Matches Length: {len(match_trans_ids)}\n")
        # print(f"Non_Matches Length: {len(non_match_trans_ids)}")
        return match_trans_ids, non_match_trans_ids

    def all_dnds(self):
        on_m_data = self.mutations_data
        # print(f"On DnDsData: {on_m_data}")
        mutation_variants = [mut_v[6] for mut_v in on_m_data][1:]
        # print(f"Mutations Variants: {mutation_variants}")
        # print(f"Mutations Count: {len(mutation_variants)}")

        synonymous_mutations = mutation_variants.count("synonymous_variant")
        non_synonymous_mutations = mutation_variants.count("missense_variant")

        # To Do: Transfer these prints to a file.
        # print(f"synonymous_mutations count: {synonymous_mutations} -     label 'synonymous_variant'")
        # print(f"non_synonymous_mutations count: {non_synonymous_mutations} -     label 'missense_variant'")

        ratio = non_synonymous_mutations / len(mutation_variants)
        # print(f"Ratio Non-Synonymous to Synonymous: {ratio}")

    def on_dnds(self):
        on_imnpptd_mutations_ids = self.mut_imnpptd_match()[0]
        # print(f"Mutations from the Immunopeptidome: {on_imnpptd_mutations_ids}")
        # print(f"Count On-Mutations: {len(on_imnpptd_mutations_ids)}")

        mutations_all_data = self.mutations_data[1:]
        # print(f"All data: {mutations_all_data}")

        on_synonymous = 0
        on_non_synonymous = 0

        for i in range(len(mutations_all_data)):
            if mutations_all_data[i][4] in on_imnpptd_mutations_ids:
                if mutations_all_data[i][6] == "synonymous_variant":
                    on_synonymous += 1
                elif mutations_all_data[i][6] == "missense_variant":
                    on_non_synonymous += 1

        print(f"ON Immunopeptidome.")
        print(f"Synonymous and NON-Synonymous for Transcript_IDs that match in both files(.anno, .bed)")
        print(f"ON Synonymous: {on_synonymous}")
        print(f"ON NON Synonymous: {on_non_synonymous}")

    def off_dnds(self):
        on_imnpptd_mutations_ids = self.mut_imnpptd_match()[1]
        # print(f"Mutations from the Immunopeptidome: {on_imnpptd_mutations_ids}")
        # print(f"Count On-Mutations: {len(on_imnpptd_mutations_ids)}")

        mutations_all_data = self.mutations_data[1:]
        # print(f"All data: {mutations_all_data}")

        on_synonymous = 0
        on_non_synonymous = 0

        for i in range(len(mutations_all_data)):
            if mutations_all_data[i][4] in on_imnpptd_mutations_ids:
                if mutations_all_data[i][6] == "synonymous_variant":
                    on_synonymous += 1
                elif mutations_all_data[i][6] == "missense_variant":
                    on_non_synonymous += 1

        print(f"OFF Immunopeptidome.")
        print(f"Synonymous and NON-Synonymous for Transcript_IDs that match in both files(.anno, .bed)")
        print(f"OFF Synonymous: {on_synonymous}")
        print(f"OFF NON Synonymous: {on_non_synonymous}")




