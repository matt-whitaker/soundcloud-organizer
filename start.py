import argparse, pyramda, logging, sys, os
from dotenv import load_dotenv, find_dotenv
from app import actions

load_dotenv(find_dotenv())
logging.basicConfig( level=getattr(logging, os.environ.get( 'LOG_LEVEL' ) or 'DEBUG' ) )

def run( ):
    parser = argparse.ArgumentParser()

    parser.add_argument( 'action', type = str )
    parser.add_argument( 'resource', type = str )

    args = parser.parse_args( )

    getattr(actions, "%s_%s" % ( args.action, args.resource ) )( )

run()

# with open('db/json/favorite_playlists.json', 'r') as favorite_playlists_json:
#     playlists = json.loads(favorite_playlists_json.read())
#     # for playlist in playlists:
#     print playlists[0]['playlist']['permalink_url']