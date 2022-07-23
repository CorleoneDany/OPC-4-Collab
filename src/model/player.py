from faker import Faker


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

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")

    @classmethod
    def createPlayer(self):
        faker = Faker()
        players = []
        for i in range(8):
            profile = faker.profile()
            first_name, last_name = profile["name"].split(" ", 1)
            params = {
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": profile["birthdate"].strftime("%d/%m/%Y"),
                "sex": profile["sex"]
            }
            player = Player(**params)
            players.append(player)
        return players


players = Player.createPlayer()
print(players)
