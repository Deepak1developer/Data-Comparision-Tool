import pandas as pd

primary_col = '<primary_col'
old_pd_df = pd.read_csv("<file_1>", error_bad_lines=False, skipinitialspace=True)
new_pd_df = pd.read_csv("<file_2>", error_bad_lines=False, skipinitialspace=True)

matched_from_old_pd_df = old_pd_df[old_pd_df[primary_col].isin(new_pd_df[primary_col])].sort_index(axis=1).sort_values(
    by=primary_col, ascending=True)
matched_from_new_pd_df = new_pd_df[new_pd_df[primary_col].isin(old_pd_df[primary_col])].sort_index(axis=1).sort_values(
    by=primary_col, ascending=True)

# unmatched data
unmatched_old_df = old_pd_df[~(old_pd_df[primary_col].isin(new_pd_df[primary_col]))].sort_index(axis=1).sort_values(
    by=primary_col, ascending=True)
unmatched_new_df = new_pd_df[~(new_pd_df[primary_col].isin(old_pd_df[primary_col]))].sort_index(axis=1).sort_values(
    by=primary_col, ascending=True)

unmatched_old_df = unmatched_old_df.set_index(primary_col)
unmatched_new_df = unmatched_new_df.set_index(primary_col)

matched_from_old_pd_df = matched_from_old_pd_df.set_index(primary_col)
matched_from_new_pd_df = matched_from_new_pd_df.set_index(primary_col)

diff = matched_from_old_pd_df.compare(matched_from_new_pd_df, align_axis=0, result_names=("old_data", "new_data"))
diff.to_csv("diff_file.csv", index=False)
unmatched_old_df.to_csv("unmatched_old_df.csv", index=False)
unmatched_new_df.to_csv("unmatched_new_df.csv", index=False)
