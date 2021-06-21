from os import stat
from otree.api import *
import random
import numpy as np
np.random.seed(163)

doc = """
Your app description


"""
class Constants(BaseConstants):
    name_in_url = 'planet_game_galaxy'
    players_per_group = None
    num_rounds = 100
    current_planet = 1
    exploring_cost = 5
    
    rewards = {}
    for planet in range(1, 101): #for each planet
        rewards[planet] = {}
        current_planet_center = np.random.randint(10, 91) 
        for r in range(1, 201): #rounds
            rewards[planet][r] = np.random.randint(current_planet_center - 10, current_planet_center + 10)
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.IntegerField(
        choices = [[1, 'Extract Ressources on this planet'], [0, 'Look for another planet'], [2, 'Settle down on this planet']], #1 = exploit, 0 = explore, 2 = stay forever
        widget = widgets.RadioSelectHorizontal,
        default = 2
    )


# PAGES
class Game(Page):
    form_model = 'player'
    form_fields = ['choice']
        
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        
        all_players = player.in_all_rounds()
        current_planet = len(all_players) - sum([p.choice != 0 for p in all_players]) + 1 # same as planet number

        if player.choice == 1:
            player.payoff = Constants.rewards[current_planet][player.round_number]
        
        elif player.choice == 0:
            player.payoff = -1*Constants.exploring_cost
        
        elif player.choice == 2:
            player.payoff = player.payoff = sum([Constants.rewards[current_planet][r] for r in range(player.round_number, Constants.num_rounds +1)])    
    
    @staticmethod
    def is_displayed(player: Player):    
        if player.round_number == 1:
            return True
        else:
            return player.in_round(player.round_number - 1).choice != 2

    
    @staticmethod
    def vars_for_template(player): 
        if player.round_number == 1:
            return {
                'image'    :  "".join(['test/1.jpeg']) ,     
            }
        else:
            all_players = player.in_all_rounds()
            number_of_exploratory_choices = len(all_players) - sum([p.choice != 0 for p in all_players]) + 1 # same as current
            return {
                'planet_number': number_of_exploratory_choices ,
                'image'    :  "".join(['test/', str(number_of_exploratory_choices), '.jpeg']) ,
            }

        
    
class spaceship(Page):
    timeout_seconds = 4
    timer_text = ''

    @staticmethod
    def is_displayed(player):
      return player.round_number == 1

class spaceshipbackground(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1

class startgame(Page):
    timeout_seconds = 4
    @staticmethod
    def is_displayed(player):
          return player.round_number == 1
        
class Results(Page):
    timeout_seconds = 4
    timer_text = ''
    @staticmethod
    def is_displayed(player: Player):
        return player.choice != 2 #when player does not choose to stay forever, result page is shown 
        
        
    @staticmethod
    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        number_of_exploratory_choices = len(all_players) - sum([p.choice == 1 for p in all_players]) + 1 # same as current
        
        return {
            'planet_number': number_of_exploratory_choices
        }


class ExploreWait(Page):
    timeout_seconds = 4
    @staticmethod
    def is_displayed(player):
     return player.choice == 0
  

class ExploitWait(Page):
    timeout_seconds = 4
    @staticmethod
    def is_displayed(player):
       return player.choice == 1


class stay(Page):
    timeout_seconds = 3
    @staticmethod
    def is_displayed(player):
       return player.round_number == 100
       
class Combined_results(Page):
    
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        total_payoff = 0
        all_players = player.in_all_rounds()
        number_of_exploratory_choices = len(all_players) - sum([p.choice != 0 for p in all_players]) + 1 # same as current
        
        for p in all_players:
            total_payoff += p.payoff
        
        return {
            'total_payoff': total_payoff,
            'planet_number': number_of_exploratory_choices
        }

        
page_sequence = [spaceship, spaceshipbackground, startgame, Game, ExploreWait, ExploitWait, Results, stay, Combined_results]
