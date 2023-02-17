import sqlite3



# db = sqlite3.connect('allsave.db')
# sql = db.cursor()
# # Раскоментировать и запустить файл чтобы создать таблицы в базе, не забыть прописать commit
# sql.execute("create table anydd_user (user_id)")
# db.commit()

class User:
	def __init__(self, user_id):
		self.user_id = user_id

	def add_or_check_user(self):
		db = sqlite3.connect('allsave.db')
		sql = db.cursor()
		sql.execute('select user_id from anydd_user where user_id = ?', (self.user_id,))
		

		if sql.fetchone() is None:
			sql.execute('insert into anydd_user values(?)', (self.user_id,))
			db.commit()

	def get_users(self, user_id):
		db = sqlite3.connect('allsave.db')
		sql = db.cursor()
		if user_id in [583411442, 295612129]:
			sql.execute('select user_id from anydd_user')
			Lusers = sql.fetchall()
			users = []
			for i in Lusers:
				users.append(i)

			return users
		pass

# sql.close()
# db.close()

