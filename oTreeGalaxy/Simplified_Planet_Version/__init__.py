from otree.api import *

c = Currency

doc = """
This app is supposed to guide the players through a galaxy of different planets. The participants can either choose to stay on a planet or 
they can choose to go to another planet. The game has several levels and every level has 100 rounds. In the end the score of the players
is displayed. 
"""


class Constants(BaseConstants):
    name_in_url = 'Planet'
    players_per_group = None #set number of players in group to 1, because participants will play alone
    num_rounds = 10 #for now set to 10, because only test round
    payoff_if_exploit = 10 #just for simplification, the payoff if the participant decides to stay will be 10
    cost_if_explore = -3
    
   


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
