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
    exploring_cost = 15
    prob_survive = 0.99
    rewards = {}
    for planet in range(1, 366): #for each planet
        rewards[planet] = {}
        current_planet_center = np.random.randint(10, 91) 
        for r in range(1, 466): #rounds
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
    Planet = models.IntegerField()

#def creating_session(subsession):
    # randomize to treatments
    #for player in subsession.get_players():
       #if player.round_number == 1:
           #calculate maximum rounds
           #r = 1
           #s = True
           #while s: 
               #r += 1 
               #s = Constants.prob_survive >= np.random.rand()
       #player.participant.max_round = r


# PAGES
class Game(Page):
    form_model = 'player'
    form_fields = ['choice']
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        
        all_players = player.in_all_rounds()
        current_planet = len(all_players) - sum([p.choice != 0 for p in all_players]) + 1 # same as planet number
        discount_factor = np.random.rand()
        number_of_exploratory_choices = len(all_players) - sum([p.choice != 0 for p in all_players]) + 1 # same as current

        if player.round_number == Constants.num_rounds:
         player.choice = 3

        if player.choice == 1:
            if player.round_number != Constants.num_rounds:
                player.payoff = Constants.rewards[current_planet][player.round_number]
            else:
                player.payoff = sum([Constants.rewards[current_planet][r] for r in range(player.round_number, Constants.num_rounds +1 + number_of_exploratory_choices)])    
        
        elif player.choice == 0:
            player.payoff = -1*Constants.exploring_cost
        
        elif player.choice == 2:
            
            player.payoff = sum([Constants.rewards[current_planet][r] for r in range(player.round_number, Constants.num_rounds +1 + number_of_exploratory_choices)])    
            
        elif player.choice == 3:
            player.payoff = sum([Constants.rewards[current_planet][r] for r in range(player.round_number, Constants.num_rounds +1 + number_of_exploratory_choices)])    
        
        
    
    @staticmethod
    def is_displayed(player: Player):    
        if player.round_number == 1:
            return True
        elif player.participant.max_round >= player.round_number: 
            return True
        else:
            if player.in_round(player.round_number - 1).choice not in [2, 3]:
                return True
            else:
                return False
        

    
    @staticmethod
    def vars_for_template(player): 
        if player.round_number == 1:
            return {
                'planet_number':1 ,
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
        if player.choice == 1 and player.round_number != 100:
             return True
        elif player.choice ==2:
             return False
        elif player.choice ==3:
             return False
        elif player.choice ==0:
            return True
        
        
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
       if player.choice == 1 and player.round_number != 100:
          return True
       else:
        return False


class stay(Page):
    timeout_seconds = 3
    @staticmethod
    def is_displayed(player):
       return player.round_number == 100

class gameover(Page):
    @staticmethod
    def is_displayed(player):
        return player.participant.max_round == player.round_number #show this whenever gameover
       
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
class Discount(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.choice == 3

class lastround(Page):
    @staticmethod
    def is_displayed(player: Player):
        if player.choice == 1 and player.round_number == 99:
             return True
        else:
            return False


        
page_sequence = [spaceship, spaceshipbackground, startgame, Game, ExploreWait, ExploitWait, Results, Discount, stay, lastround, gameover, Combined_results]
