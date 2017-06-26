
class CommandController:
    def command_chk(command):
        if(!command):
            raise CommandError('Command does not selected')
        cur.execute('SELECT command FROM command_info')

        if(command not cur.fetchall()):
            raise CommandError('Command not fuond')