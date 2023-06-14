from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash


class Service :
    def __init__(self,data):
        self.id = data['id']
        self.service_name = data['service_name']
        self.Price = data['Price']
        self.Price = data['Price']
        self.description = data['description']
        

#                                    Query



    @classmethod
    def get_all_service(cls):
        query = """
        SELECT * FROM services
        """
        result = connectToMySQL(DATABASE).query_db(query)
        print(result)
        services = []
        for row in result:
            services.append(cls(row))
        return services

