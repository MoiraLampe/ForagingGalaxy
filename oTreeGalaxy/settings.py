from os import environ


SESSION_CONFIGS = [
    dict(
        name='Introduction',
        app_sequence=['Introduction'], #not sure what app sequence stands for?
        num_demo_participants=1,
      ),
    dict(
        name='Instruction',
        app_sequence=['Introduction', 'Instruction','Planet_Game', 'survey'], #not sure what app sequence stands for?
        num_demo_participants=1,
    ),
      
    dict(
        name='Planet_Game',
        app_sequence=['Introduction', 'Instruction','Planet_Game', 'survey'], #not sure what app sequence stands for?
        num_demo_participants=1,
    ),
      dict(
        name='galaxy_game',
        app_sequence=['Introduction','Instruction','galaxy_game','survey','EndOfGame'], #not sure what app sequence stands for?
        num_demo_participants=10,
      ),
    dict(
        name='Survey',
        app_sequence=['Planet_Game', 'survey'],
        num_demo_participants=1,
    ), #do I want to merge them together?
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '3872274287741'

INSTALLED_APPS = ['otree']
