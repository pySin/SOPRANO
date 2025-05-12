# Soprano Python main caller
import in_imnpptd_mut


def caller():
    data_files = "data_files"
    mutations_file = "MISSONI_ON_clonal_cohort_SOPRANO.anno"
    imnpptd_file = "IP_MISSONI_clonal_intersection_complement_modified.bed"
    report_file_name = f"{mutations_file}_+_{imnpptd_file}.txt"
    print(report_file_name)

    mf_path = f"{data_files}/{mutations_file}"
    if_path = f"{data_files}/{imnpptd_file}"
    print(f"Mutations path: {mf_path}")

    on_mut = in_imnpptd_mut.OnMutations(mf_path, if_path)
    on_mut.report_file_folder(report_file_name)
    on_mut.immunopeptidome_data_calc()
    on_mut.mutations_data_calc()
    on_mut.mut_imnpptd_match()
    on_mut.all_dnds()
    on_mut.on_dnds()
    on_mut.off_dnds()


if __name__ == "__main__":
    caller()
