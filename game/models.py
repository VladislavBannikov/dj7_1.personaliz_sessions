from django.db import models
import random


class Player(models.Model):
    pass


class Game(models.Model):
    min_number = models.IntegerField()
    max_number = models.IntegerField()
    number = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    player_id = models.ManyToManyField(Player, through="PlayerGameInfo", related_name="game_id")
    attempts_count = models.IntegerField(default=0)

    # @classmethod
    # def create(cls, min_number=0, max_number=10):
    #     game = cls(min_number=min_number, max_number=max_number,number=10)
    #     game.number = random.randint(cls.min_number, cls.max_number)
    #     return game

class PlayerGameInfo(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    is_user_creator = models.BooleanField(blank=False)

