import pymongo


class Database(object):
    URI = "mongodb://201.48.37.113:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        cliente = pymongo.MongoClient(Database.URI)
        Database.DATABASE = cliente['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].finde_one(query)
