class Player:
    def __init__(self, first_name, last_name, date_of_birth,
                 sex, rank=0, score=0, doc_id=None, players_faced=None):
        if players_faced is None:
            players_faced = []
        self.firstName = first_name
        self.lastName = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = int(rank) or 0
        self.score = int(score) or 0
        self.doc_id = doc_id
        self.players_faced = players_faced
