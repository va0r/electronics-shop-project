from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
CSV_FILE = Path.joinpath(ROOT_DIR, 'items.csv')
CSV_FILE_ERROR = Path.joinpath(ROOT_DIR, 'items_error.csv')

