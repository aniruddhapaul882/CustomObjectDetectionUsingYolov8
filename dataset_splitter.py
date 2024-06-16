import splitfolders

# Paths
raw_data_dir = 'raw_data'
output_base_dir = 'dataset'

# Split with a ratio
splitfolders.ratio(raw_data_dir, output=output_base_dir, seed=42, ratio=(.7, .2, .1), group_prefix=None, move=True)
