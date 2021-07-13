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
    minimum_number_of_rounds_player = 21
    df_thresh = 0.01
   
    rewards = {}
    for planet in range(1, 366): #for each planet
        rewards[planet] = {}
        current_planet_center = np.random.randint(1, 10)*10 
        for r in range(1, 466): #number of exploiting choice
            rewards[planet][r] = np.random.randint(current_planet_center - 10, current_planet_center + 10)
    
    dfs_checks = []
    for i in range(500):
        if i < minimum_number_of_rounds_player:
            dfs_checks.append(False)
        else:
            current_check = np.random.rand() > df_thresh
            if True in dfs_checks:
                dfs_checks.append(True)
            else:
                dfs_checks.append(current_check)
        
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.IntegerField(
        choices = [[1, 'Extract Ressources on this planet'], [0, 'Look for another planet'], [2, 'Settle down on this planet']], #1 = exploit, 0 = explore, 2 = stay forever
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    Planet = models.IntegerField()



# PAGES
class Game(Page):
    form_model = 'player'
    form_fields = ['choice']
    
    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     return 0
        # all_players = player.in_all_rounds()
        # current_planet = len(all_players) - sum([p.choice != 0 for p in all_players]) + 1 # same as planet number
        # # discount_factor = np.random.rand()
        # # discount_factor_kicks_in = discount_factor > 0.1
        # number_of_exploratory_choices = len(all_players) - sum([p.choice != 0 for p in all_players]) + 1 # same as current
        # number_of_exploiting_choices = len(all_players) - number_of_exploratory_choices

        # # if discount_factor_kicks_in and player.round_number >= 20:
        # #     player.choice = 3
        # #     player.payoff = 0

        # if player.choice == 0:
        #     player.payoff = -1*Constants.exploring_cost
        
        # elif player.choice == 1:
            
        #     if player.round_number != Constants.num_rounds:
        #         player.payoff = Constants.rewards[current_planet][player.round_number]
        #     else:
        #         player.payoff = sum([Constants.rewards[current_planet][r] for r in range(player.round_number, Constants.num_rounds +1 + number_of_exploratory_choices)])    

        # elif player.choice == 2:
        #     player.payoff = Constants.rewards[current_planet][player.round_number]
        

    @staticmethod
    def is_displayed(player: Player):    
        is_last_round = player.round_number == Constants.num_rounds
        all_players = player.in_all_rounds()
        stayed =  sum([p.choice == 2 for p in all_players]) >= 1
        current_planet = len(all_players) - sum([p.choice != 0 for p in all_players]) + 1
        number_of_exploratory_choices = len(all_players) - sum([p.choice != 0 for p in all_players]) + 1 # same as current
        number_of_exploiting_choices = len(all_players) - number_of_exploratory_choices
        current_discount_factor = Constants.dfs_checks[player.round_number]
        
        if current_discount_factor:
            player.payoff = 0
        else:
            if player.choice == 0:
                if player.round_number == Constants.num_rounds:
                    player.payoff = sum([Constants.rewards[current_planet +1][r] for r in range(player.round_number, Constants.num_rounds + number_of_exploratory_choices)]) - Constants.exploring_cost    
                else:
                    player.payoff = -1*Constants.exploring_cost
            
            elif player.choice == 1:
                
                if player.round_number != Constants.num_rounds:
                    player.payoff = Constants.rewards[current_planet][player.round_number]
                else:
                    player.payoff = sum([Constants.rewards[current_planet][r] for r in range(player.round_number, Constants.num_rounds + number_of_exploratory_choices)])    

            elif player.choice == 2:
                player.payoff = Constants.rewards[current_planet][player.round_number]
        
        # Actual displaying part
        if player.round_number == 1:
            return True
        else:
            if (player.in_round(player.round_number - 1).choice not in [2, 3]) and stayed == False and not Constants.dfs_checks[player.round_number - 1] and not is_last_round:
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
            stayed =  sum([p.choice == 2 for p in all_players]) >= 1
            return {
                'planet_number': number_of_exploratory_choices ,
                'image'    :  "".join(['test/', str(number_of_exploratory_choices), '.jpeg']) ,
                'choice':player.choice,
                'stayed':stayed,
                'df': Constants.dfs_checks[player.round_number - 1],
            }

        
class Results(Page):
    timeout_seconds = 3
    timer_text = ''
    @staticmethod
    def is_displayed(player: Player):
        all_players = player.in_all_rounds()
        stayed =  sum([p.choice == 2 for p in all_players]) >= 1
        if player.choice == 1 and player.round_number != Constants.num_rounds and not stayed and not Constants.dfs_checks[player.round_number]:
            return True
        elif player.choice ==2:
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
    timeout_seconds = 3
    @staticmethod
    def is_displayed(player):
          return player.round_number == 1
        


class ExploreWait(Page):
    timeout_seconds = 3
    @staticmethod
    def is_displayed(player):
     return player.choice == 0
  

class ExploitWait(Page):
    timeout_seconds = 1
    @staticmethod
    def is_displayed(player):
        # all_players = player.in_all_rounds()
        # is_last_round = player.round_number == Constants.num_rounds
        # stayed =  sum([p.choice == 2 for p in all_players]) >= 1
        # if player.choice == 1 and player.round_number > 1 and stayed == False and not Constants.dfs_checks[player.round_number - 1] and not is_last_round:
        #  return True 
        # else:
        #     return False
        is_last_round = player.round_number == Constants.num_rounds
        all_players = player.in_all_rounds()
        stayed =  sum([p.choice == 2 for p in all_players]) >= 1
        if player.choice ==1 and stayed ==False and not Constants.dfs_checks[player.round_number - 1] and not is_last_round:
            return True
            
        elif player.choice == 1 and stayed == False and Constants.dfs_checks[player.round_number - 1] and player.round_number == Constants.num_rounds:
           return False
          
        # if player.choice == 1: #and player.round_number > 1:
        #     #if (player.in_round(player.round_number - 1).choice not in [2, 3]) and stayed == False and not Constants.dfs_checks[player.round_number - 1] and not is_last_round:
        #     if stayed == False and not Constants.dfs_checks[player.round_number - 1] and not is_last_round:
        #         return True
        #     else:
        #         return False
            


class stay(Page):
    timeout_seconds = 3
    @staticmethod
    def is_displayed(player):
       return player.round_number == Constants.num_rounds

class gameover(Page):
    timeout_seconds = 3
    @staticmethod
    def is_displayed(player):
    #is_last_round = player.round_number == Constants.num_rounds
     is_last_round = player.round_number == Constants.num_rounds
     all_players = player.in_all_rounds()
     stayed =  sum([p.choice == 2 for p in all_players]) >= 1
     if player.choice == 1 and stayed == False and Constants.dfs_checks[player.round_number - 1] and player.round_number == Constants.num_rounds:
        return True
     else:
        return False #show this whenever gameover
       
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
        is_last_round = player.round_number == Constants.num_rounds
        all_players = player.in_all_rounds()
        stayed =  sum([p.choice == 2 for p in all_players]) >= 1
        if player.choice == 0 and player.round_number == Constants.num_rounds-2 and stayed == False:
             return True
        else:
            return False 


        
page_sequence = [spaceship, spaceshipbackground, startgame, Game, gameover, ExploreWait, ExploitWait, Results, stay, lastround, Combined_results]
