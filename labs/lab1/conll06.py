from typing import List


class Conll06_Token(object):
    def __init__(self,
                 token_id: int,
                 form: str,
                 lemma: str,
                 pos: str,
                 xpos: str,
                 morph: str,
                 head: int,
                 rel: str) -> None:

        self.token_id = token_id
        self.form = form
        self.lemma = lemma
        self.pos = pos
        self.xpos = xpos
        self.morph = morph
        self.head = head
        self.rel = rel


class ConLL06_Sentence(object):
    def __init__(self, tokens: List[Conll06_Token], *args, **kwargs) -> None:
        pass
