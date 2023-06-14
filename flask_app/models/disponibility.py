from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash


class Disponibility :
    def __init__(self,data):
        self.id = data['id']
        self.date = data['date']
        self.time = data['time']
        

#                                    Query


  
    @classmethod
    def get_all_disponibility(cls):
        query = """
        SELECT * FROM disponibility
        """
        result = connectToMySQL(DATABASE).query_db(query)
        print(result)
        disponibilities = []
        for row in result:
            disponibilities.append(cls(row))
        return disponibilities

