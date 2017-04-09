import logging
from pymongo import MongoClient

def get_connection( ):
    return MongoClient().soundcloud_origanizer

def insert( collection, obj ):
    logger = logging.getLogger( 'soundcloud_organizer.mongo.insert' )
    db = get_connection()

    logger.info("Inserting one into %s" % collection)
    logger.info("One document inserted" % len(getattr( db, collection ).insert_one( obj ).inserted_ids))
    logger.info("Insert complete")

def insert_all( collection, objs ):
    logger = logging.getLogger( 'soundcloud_organizer.mongo.insert_all' )
    db = get_connection()

    logger.info("Inserting many into %s" % collection)
    logger.info("%s documents inserted " % len(getattr(db, collection).insert_many( objs ).inserted_ids))
    logger.info("Insert complete")

def delete_all( collection ):
    logger = logging.getLogger( 'soundcloud_organizer.mongo.delete_all' )
    db = get_connection( )

    logger.info("Deleting all from %s" % collection)
    logger.info("%s documents deleted" % getattr( db, collection ).delete_many( { } ).deleted_count)
    logger.info("Delete complete")
