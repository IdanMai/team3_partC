from datetime import datetime, date
from utilities.db.db_manager import dbManager


class User:
    email = ""
    username = ""
    birthday = date.today()
    password = ""
    date_added = date.today()
    points = 0

    def __init__(self, email, username, birthday, password):
        super().__init__()
        self.email = email
        self.username = username
        self.birthday = birthday
        self.password = password
        self.date_added = date.today()
        self.points = 0
        self.cursor = None


    def add_user(self):
        query = "INSERT INTO users(email, username, birthday, password, date_added, points) VALUES ('%s', '%s', '%s', '%s','%s', '%s')" % (
            self.email, self.username, self.birthday, self.password, self.date_added, self.points)
        query_result = dbManager.commit(query)
        return query_result


    def search_user(self, email):
        query = f"select * from users where email='%s'" % self.email
        query_result = dbManager.fetch(query)
        return query_result

    def update_user(self):
        query = f"UPDATE users set username='%s', birthday='%s', password='%s',points='%s' where email='%s'" % \
                (self.username, self.birthday, self.password, self.points, self.email)
        query_result = dbManager.commit(query)
        return query_result



# Creates an instance for the User class for export.
#user = User()
