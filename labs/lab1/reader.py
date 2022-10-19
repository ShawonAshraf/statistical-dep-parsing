import os
from tokenize import Token
from conll06 import Conll06_Token

DATA_ROOT = os.getenv("STATDATA")

file_paths = {
    "english": {
        "train": os.path.join(DATA_ROOT, "english", "train"),  # type: ignore
        "test": os.path.join(DATA_ROOT, "english", "test"),  # type: ignore
        "dev": os.path.join(DATA_ROOT, "english", "dev")  # type: ignore
    },
    "german": {
        "train": os.path.join(DATA_ROOT, "german", "train"),  # type: ignore
        "test": os.path.join(DATA_ROOT, "german", "test"),  # type: ignore
        "dev": os.path.join(DATA_ROOT, "german", "dev")  # type: ignore
    }
}


def check_file_pathnames():
    # just a sanity check for pathnames
    for _, info in file_paths.items():
        for split_name, pathname in info.items():
            assert os.path.exists(pathname)


def read_file(file_path_name):
    with open(file_path_name, "r", encoding="utf-8") as connl_file:
        data = connl_file.readlines()

    for sentence in data:
        tokens = sentence.split("\t")

        # ignore the new line token
        if tokens == ["\n"]:
            continue

        conll_tokens = Conll06_Token(*tokens[:8])  # type: ignore


if __name__ == "__main__":
    check_file_pathnames()

    file_path_name = os.path.join(
        file_paths["english"]["dev"], "wsj_dev.conll06.pred")

    read_file(file_path_name)
