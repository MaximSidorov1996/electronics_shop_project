from pathlib import Path

USE_LOCAL_DATA = True
ROOT_PATH = Path(__file__).resolve().parent
CSV_FILE_PATH = Path.joinpath(ROOT_PATH, 'src', 'items.csv')
