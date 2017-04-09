from __future__ import absolute_import
import os, soundcloud


def get_all_pages( client, resource ):
    """
    Generator for collecting all pages of a resource
    :param client:
    :param resource:
    :return:
    """
    print "Downloading [ %s ]" % resource

    page = 1

    response = client.get( resource, limit=200, linked_partitioning=1 ).obj

    print "Page 1 complete"
    page += 1

    for track in response['collection']:
        yield track

    while 'next_href' in response:
        response = client.get( response['next_href'], limit=200, linked_partitioning=1 ).obj

        print "Page %s complete" % page
        page += 1

        for track in response['collection']:
            yield track

    print "Download complete"


def get_client( ):
    print "Connecting to Soundcloud"
    client = soundcloud.Client(
        client_id = os.environ.get( 'SOUNDCLOUD_ID' ),
        client_secret = os.environ.get( 'SOUNDCLOUD_SECRET' ),
        username = os.environ.get( 'SOUNDCLOUD_USER' ),
        password = os.environ.get( 'SOUNDCLOUD_PASS' )
    )
    print "Connected"

    return client
