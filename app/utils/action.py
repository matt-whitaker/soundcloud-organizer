import os, json, pymongo, logging
from soundcloud import get_all_pages, get_client

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
    logger = logging.getLogger( 'soundcloud_organizer.action.write_json' )
    logger.info("Writing data to [ %s ]" % filename)
    with open( filename , 'w' ) as file:
        file.write( json.dumps( data ) )
        logger.info("Writing complete")
