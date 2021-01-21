#!/usr/bin/env python3

"""Generates README.md based on gs_list.txt."""

TXT_FILENAME = "processed/gs_list.txt"
MD_FILENAME = "processed/README.md"
GS_PREFIX = "gs://cimr-d/"

def get_md_name(gs_path):
    """Returns the filename with leading bullet list in MD format."""
    relative_path = gs_path[len(GS_PREFIX):]
    file_name = relative_path.split("/")[-1]
    bucket_url = "https://storage.googleapis.com/cimr-d"
    return f"[{file_name}]({bucket_url}/{relative_path})"


with open(TXT_FILENAME) as file_in, open(MD_FILENAME, 'w') as file_out:
    file_out.write(
        "*Note: If the list is cutoff at the bottom due to GitHub's 512KB-limit\n"
        "on the main page, click [here](README.md) to see its full content.*\n\n"
    )
    file_out.write("List of processed files (with links to Google Cloud Storage bucket):\n")
    file_out.write("----\n")

    for line_in in file_in:
        line_in = line_in.strip()
        # Ignore blank lines and the ending summary line
        if len(line_in) == 0 or line_in.startswith("TOTAL: "):
            continue

        # folder name
        if line_in.startswith(GS_PREFIX) and line_in.endswith("/:"):
            left_idx = len(GS_PREFIX)
            folder_name = line_in[left_idx:-2]  # "-2" cuts off the trailing ":/"
            file_out.write(" " * 2 + f"* {folder_name}\n")
            continue

        # file name
        tokens = line_in.strip().split()
        gs_path = " ".join(tokens[3:])
        md_name = get_md_name(gs_path)
        file_size = " ".join(tokens[0:2])
        file_date = tokens[2]
        file_out.write(f" " * 4 + f"* {md_name}: {file_size} (updated on *{file_date}*)\n")
