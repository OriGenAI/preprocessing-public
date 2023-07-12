import os

import pandas as pd


def preprocess(download_func, output_source, base_output_source, input_files, allow_missing_files, **files):
    output_file = os.path.join(output_source.uri, "output.h5")
    for input_file_key, input_file_name in files.items():
        download_func(input_file_name, output_source.uri)

        input_file = os.path.join(output_source.uri, input_file_name)
        df = pd.read_csv(input_file)

        df.to_hdf(output_file, key=input_file_key)
