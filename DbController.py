from mysql import connectior
class DbController:
        conn = connector.connect(user='root', password='marutaku19970131', host='localhost', database='timetracker')
        cur = conn.cursor()
    def getAllCommand(self):
        self.cur.execute('SELECT command FROM command_info;')
        return self.cur.fetchall()

    def getCommandInfo(self, command):
        self.cur.execute('SELECT info FROM command_info WHERE command ="' + command + '";')
        return self.cur.fetchall()

    def chkCommand(self, command):
        





