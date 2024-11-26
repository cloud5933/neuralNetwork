import polars as pl

splits = {'train': 'mnist/train-00000-of-00001.parquet', 'test': 'mnist/test-00000-of-00001.parquet'}
df = pl.read_parquet('hf://datasets/ylecun/mnist/' + splits['train'])