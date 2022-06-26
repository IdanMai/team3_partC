from utilities.db.db_manager import  DBManager



def pizzaQuery():
    query = "SELECT * FROM pizza"
    pizza_list = fetch(query, query_type='fetch')