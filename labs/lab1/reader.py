import os
from tokenize import Token
from typing import List
from conll06 import Conll06_Token, ConLL06_Sentence

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


def read_file(file_path_name) -> List[ConLL06_Sentence]:
    with open(file_path_name, "r", encoding="utf-8") as connl_file:
        data = connl_file.readlines()

    sentences: List[ConLL06_Sentence] = list()
    tokens: List[Conll06_Token] = list()
    for line in data:
        # keep going until "\n" or the sentence separator is encountered
        token = line.split("\t")

        _id = token[0]
        if _id == "\n":
            # sentence ends here
            sentence = ConLL06_Sentence(tokens)
            # empty list
            tokens.clear()
            sentences.append(sentence)
        else:
            _form = token[1]
            _lemma = token[2]
            _pos = token[3]
            _xpos = token[4]
            _morph = token[5]
            _head = int(token[6])
            _rel = token[7]

        conll_token = Conll06_Token(
            _id, _form, _lemma, _pos, _xpos, _morph, _head, _rel)  # type: ignore
        tokens.append(conll_token)

    return sentences


if __name__ == "__main__":
    check_file_pathnames()

    file_path_name = os.path.join(
        file_paths["english"]["dev"], "wsj_dev.conll06.pred")

    sentences = read_file(file_path_name)
    print(sentences)
