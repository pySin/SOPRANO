# Soprano Pytho main caller
import in_imnpptd_mut


def caller():
    data_files = "data_files"
    mutations_file = "IP_MISSONI_clonal_intersection_complement_modified.bed"
    imnppdt_file = "MISSONI_ON_clonal_cohort_SOPRANO.anno"

    mf_path = f"{data_files}/{mutations_file}"
    if_path = f"{data_files}/{imnppdt_file}"
    print(f"Mutations path: {mf_path}")

    # in_imnpptd_mut.OnMutations.open_mutations_file(data_files + "/")


if __name__ == "__main__":
    caller()
