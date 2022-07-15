from datetime import datetime, date
from utilities.db.db_manager import dbManager


class User:

    def __init__(self):
        super().__init__()
        self.cursor = None


    def add_user(self,email, username, birthday, password):
        query = "INSERT INTO users(email, username, birthday, password, date_added, points) VALUES ('%s', '%s', '%s', '%s','%s', '%s')" % (
            email, username, birthday, password, date.today(), 0)
        query_result = dbManager.commit(query)
        return query_result


    def search_user(self, email):
        query = f"select * from users where email='%s'" % email
        query_result = dbManager.fetch(query)
        return query_result

    def update_user(self):
        query = f"UPDATE users set username='%s', birthday='%s', password='%s',points='%s' where email='%s'" % \
                (self.username, self.birthday, self.password, self.points, self.email)
        query_result = dbManager.commit(query)
        return query_result



# Creates an instance for the User class for export.
#user = User()
