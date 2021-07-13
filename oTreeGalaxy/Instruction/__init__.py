from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Instruction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    pass


# PAGES

class Instruction(Page):
    pass

# class Questions(Page):
#     form_model = 'player'
#     form_fields = []

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Instruction]
