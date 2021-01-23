import logging

"""
This Model Class Product called from the Controller Class in
Method show_all_product()

Model Class Attribute and Method 
attr => product_name

methods :
    constructor : takes product_name as argument ,
    get_product_name : return product_name for the instance 
    static method get_all_product() : return list of all prouduct
"""


class Product:

    def __init__(self, product_name):
        self.product_name = product_name

    def get_product_name(self):
        return self.product_name

    """
    get_all_product method 
    create a list named all_product_list and appending or create myapp.log file
    open db.txt to read product from it  
    """
    @staticmethod
    def get_all_product():
        all_product_list = []
        format_ = "%(asctime)s =>  %(message)s"
        logging.basicConfig(filename="myapp.log", filemode="a", format=format_, level=logging.INFO,
                            datefmt="%H:%M:%S")
        logging.info("Model.py    : Open db.txt File for Reading")
        with open("db.txt", "r") as db_file:
            for _ in db_file:
                all_product_list.append(_.strip())
        return all_product_list
