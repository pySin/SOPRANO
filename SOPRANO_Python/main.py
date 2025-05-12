# Soprano Python main caller
import in_imnpptd_mut


def caller():
    data_files = "data_files"
    imnpptd_file = "MISSONI_ON_clonal_cohort_SOPRANO.anno"
    mutations_file = "IP_MISSONI_clonal_intersection_complement_modified.bed"

    mf_path = f"{data_files}/{imnpptd_file}"
    if_path = f"{data_files}/{mutations_file}"
    print(f"Mutations path: {mf_path}")

    on_mut = in_imnpptd_mut.OnMutations(mf_path, if_path)
    # on_mut.on_immunopeptidome_data()
    # on_mut.on_mutations_data()
    on_mut.mut_imnpptd_match()
    on_mut.on_dnds()


if __name__ == "__main__":
    caller()
