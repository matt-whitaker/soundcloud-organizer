import json, pprint, os
from utils.soundcloud import get_all_pages, get_client


def with_dir ( dir ):
    def wrapper_fn2 ( fn ):
        def wrapper_fn1( *args, **kwargs ):
            if not os.path.exists( dir ):
                os.makedirs( dir )

            return fn( *args, **kwargs )

        return wrapper_fn1

    return wrapper_fn2


def with_client( fn ):
    def wrapper_fn( *args, **kwargs ):
        client = get_client()

        return fn( client, *args, **kwargs )

    return wrapper_fn

def write_json( filename, data ):
    print "Writing data to [ %s ]" % filename
    with open( filename , 'w' ) as file:
        file.write( json.dumps( data ) )
        print "Writing complete"

@with_client
@with_dir( 'data/json' )
def download_favorite_tracks ( client ):
    all_favorite_tracks = list( get_all_pages( client, "/me/favorites/" ) )
    write_json( 'data/json/favorite_tracks.json', all_favorite_tracks )


@with_client
@with_dir( 'data/json' )
def download_playlists ( client ):
    all_playlists = list( get_all_pages( client, "/me/playlists" ) )
    write_json( 'data/json/playlists.json', all_playlists )


@with_client
@with_dir( 'data/json' )
def download_favorite_playlists ( client ):
    all_favorite_playlists = list( get_all_pages( client, "https://api.soundcloud.com/e1/me/playlist_likes" ) )
    write_json( 'data/json/favorite_playlists.json' , all_favorite_playlists )

