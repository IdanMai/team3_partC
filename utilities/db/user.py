from datetime import datetime, date

from utilities.db.db_manager import dbManager


class User:
    def _init_(self, email, username, birthday, password, date_added, points):
        super()._init_()
        self.email = email
        self.username = username
        self.birthday = birthday
        self.password = password
        self.date_added = date_added
        self.points = points


    def add_user(self):
        query = "INSERT INTO users(email, username, birthday, password, date_added) VALUES ('%s', '%s', '%s', %s, %s)" % (
            self.email, self.username, self.birthday, self.password, date.today())
        query_result = dbManager.commit(query)
        print(query_result)

    def search_user(self):
        query = f"select * from users where email='%s'" % self.email
        query_result = dbManager.fetch(query)
        return query_result

    def update_user(self):
        query = f"UPDATE users set username='%s', birthday='%s', password='%s',points='%s' where email='%s'" % \
                (self.username, self.birthday, self.password, self.points, self.email)
        query_result = dbManager.commit(query)
        return query_result