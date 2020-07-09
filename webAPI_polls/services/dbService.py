from flask import Flask, request, json, Response
from pymongo import MongoClient
import logging as log

app = Flask(__name__)

class MongoAPI:
    def __init__(self, collection, document, data = None):
        self.client = MongoClient("mongodb+srv://ddmilgram:DPYutVu33y2ZofXI@cluster0-oa6bc.mongodb.net/<test>?retryWrites=false&w=majority")
        cursor = self.client[collection]
        self.collection = cursor[document]
        self.data = data

    def read(self):
        log.info('Read data')
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        log.info('Writing Data')
        new_document = data
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted'}
        return output

    def update(self):
        log.info('Updating Data')
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        log.info('Deleting Data')
        filt = data['Filter']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output






