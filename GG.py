from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'gg',
    'version': '1.0',
    'name': 'GG Plugin',
    'description': 'Kill me when they input !!gg',
    'author': 'Hong_SZ',
    'link': 'https://github.com/yourusername/your-repo',
    'dependencies': {
        'mcdreforged': '>=1.0.0',
    }
}

def on_load(server, old_module):
    server.register_help_message('!!gg', 'Kill yourself using !!gg.')

def on_info(server, info):
    if info.content.startswith('!!gg'):
        # Get the player's name
        player_name = info.player

        # Kill the player
        server.execute(f'kill {player_name}')

def on_user_info(server, info):
    if info.content.startswith('!!gg'):
        # Get the player's name
        player_name = info.player

        # Kill the player
        server.execute(f'kill {player_name}')
        
def on_server_startup(server, old_module):
    server.logger.info('GG Plugin is loaded.')

def on_server_stop(server, old_module):
    server.logger.info('GG Plugin is unloaded.')
