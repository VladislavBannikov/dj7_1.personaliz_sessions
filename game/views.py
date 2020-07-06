from django.shortcuts import render, render_to_response
import random

active_game = None

from .models import Game, Player, PlayerGameInfo
from .forms import InputForm


def get_player(request):
    player_id = request.session.get('player_id') or None
    if player_id is None:
        player = Player.objects.create()
        request.session['player_id'] = player.id
    else:
        try:
            player = Player.objects.get(id=player_id)
        except Player.DoesNotExist:
            print(f"user with id {player_id} doesn't exist. Trying to create new player")
            request.session['player_id'] = None
            player = get_player(request)
    return player


def get_game(request, player: Player):
    game_id = request.session.get('game_id') or None
    # if game is not assigned to the player
    if game_id is None:
        # find active game
        active_games = Game.objects.filter(is_completed=False)
        if active_games.count() == 1:
            game = active_games.first()
            # join active game
            PlayerGameInfo.objects.create(player=player, game=game, is_user_creator=False)

        elif active_games.count() == 0:
            # create if no active game
            #todo: что-то не получилось генерировать Number во время создания модели.
            game = Game.objects.create(min_number=22, max_number=33,
                                       number=random.randint(22,33))
            PlayerGameInfo.objects.create(player=player, game=game, is_user_creator=True)
        else:
            print("Error: Something wrong, several active games")
            exit(1)
        request.session['game_id'] = game.id
    # if game is assigned to the player
    else:
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            print(f"Game you played before doesn't exist. Trying to join active or create new game")
            del request.session['game_id']
            game = get_game(request, player)
    return game


def show_home(request):
    player = get_player(request)
    game = get_game(request, player)
    try:
        game_info = PlayerGameInfo.objects.get(player=player, game=game)
    except PlayerGameInfo.DoesNotExist or PlayerGameInfo.MultipleObjectsReturned:
        print("Database corrupted")
        exit(1)

    context = {
        "player": player,
        "game": game,
        "game_info": game_info}

    if not game_info.is_user_creator:
        context.update({"form": InputForm})

    if not game.is_completed:
        if request.method == "POST":
            guess_number = int(request.POST.get("number"))
            if guess_number == game.number:
                game.is_completed = True
                game.save()
                context.update({"message": "Вы победили"})
            else:
                game.attempts_count += 1
                game.save()
                if guess_number > game.number:
                    context.update({"message": "Загадано число меньше"})
                elif guess_number < game.number:
                    context.update({"message": "Загадано число больше"})
    else:
        del request.session['game_id']
    return render(request, 'home.html', context=context)
