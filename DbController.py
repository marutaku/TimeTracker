import mysql.connector


class DbController:
    conn = mysql.connector.connect(user='root', password='marutaku19970131', host='localhost', database='timetracker')
    cur = conn.cursor()

    def getAllCommand(self):
        self.cur.execute('SELECT command FROM command_info;')
        return self.cur.fetchall()

    def getCommandInfo(self, command):
        self.cur.execute('SELECT info FROM command_info WHERE command ="' + command + '";')
        return self.cur.fetchall()

    def getCategoly(self):
        self.cur.execute('SELECT categoly FROM categoly;')
        return self.cur.fetchall()

    def get_continue_task(self, categoly='*'):
        self.cur.execute('SELECT id, start_time FROM tracking_tbl WHERE is_continue = 1 AND categoly = "' + categoly + '";')
        return self.cur.fetchall()

    def start_task(self, categoly, start_time):
        self.cur.execute('INSERT  INTO tracking_tbl(start_time, categoly) VALUES("' + start_time + '", "' + categoly + '");')
        self.conn.commit()

    def finish_task(self, task_id, time):
        self.cur.execute('UPDATE tracking_tbl SET is_continue = 0, end_time = "' + time + '" WHERE id = ' + task_id + ';')
        self.conn.commit()






