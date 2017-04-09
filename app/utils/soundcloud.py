from __future__ import absolute_import
import os, soundcloud, logging

def get_all_pages( client, resource ):
    """
    Generator for collecting all pages of a resource
    :param client:
    :param resource:
    :return:
    """
    logger = logging.getLogger( 'soundcloud_organizer.soundcloud.get_all_pages' )

    logger.info("Downloading [ %s ]" % resource)

    page = 1

    response = client.get( resource, limit=200, linked_partitioning=1 ).obj

    logger.info("Page 1 complete")
    page += 1

    for track in response['collection']:
        yield track

    while 'next_href' in response:
        response = client.get( response['next_href'], limit=200, linked_partitioning=1 ).obj

        logger.info("Page %s complete" % page)
        page += 1

        for track in response['collection']:
            yield track

    logger.info("Download complete")


def get_client( ):
    logger = logging.getLogger( 'soundcloud_organizer.soundcloud.get_client' )
    logger.info("Connecting to Soundcloud")
    client = soundcloud.Client(
        client_id = os.environ.get( 'SOUNDCLOUD_ID' ),
        client_secret = os.environ.get( 'SOUNDCLOUD_SECRET' ),
        username = os.environ.get( 'SOUNDCLOUD_USER' ),
        password = os.environ.get( 'SOUNDCLOUD_PASS' )
    )
    logger.info("Connected")

    return client
