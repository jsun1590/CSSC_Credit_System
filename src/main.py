import src.auth as auth
import os
import cmd
import colorama
class CreditShell(cmd.Cmd):
    def __init__(self):
        super(CreditShell, self).__init__()
        self.account = None
        self.prompt = "Guest@CSSC_Credit_System $ "
    
    def do_clear(self, args):
        '''Clear the console of any texts.'''
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    
    # Authentication
    def do_register(self, args):
        '''Register a new account on the credit system.'''
        self.account = auth.register()
    
    def do_login(self, args):
        '''Login to an account on the credit system.'''
        self.account = auth.login()
        
    def do_logout(self, args):
        raise NotImplementedError

def main():
    CreditShell().cmdloop()

if __name__ == "__main__":
    main()