import json, pprint, os
from utils.soundcloud import get_all_pages
from utils.action import with_dir, with_client, write_json
from utils.mongo import insert_all, delete_all

@with_client
@with_dir( 'data/json' )
def download_favorite_tracks ( client ):
    all_favorite_tracks = list( get_all_pages( client, "/me/favorites/" ) )
    write_json( 'data/json/favorite_tracks.json', all_favorite_tracks )

    delete_all( 'favorite_tracks' )
    insert_all( 'favorite_tracks', all_favorite_tracks )


@with_client
@with_dir( 'data/json' )
def download_playlists ( client ):
    all_playlists = list( get_all_pages( client, "/me/playlists" ) )
    write_json( 'data/json/playlists.json', all_playlists )

    delete_all( 'playlists' )
    insert_all( 'playlists', all_playlists )

@with_client
@with_dir( 'data/json' )
def download_favorite_playlists ( client ):
    all_favorite_playlists = list( get_all_pages( client, "https://api.soundcloud.com/e1/me/playlist_likes" ) )
    write_json( 'data/json/favorite_playlists.json' , all_favorite_playlists )

    delete_all( 'favorite_playlists' )
    insert_all( 'favorite_playlists', all_favorite_playlists )


