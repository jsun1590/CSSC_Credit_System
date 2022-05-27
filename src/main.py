from logic.account import Account
import src.auth as auth
import os
import cmd
import colorama
class CreditShell(cmd.Cmd):
    def __init__(self):
        super(CreditShell, self).__init__()
        self.account = None
        self.default_prompt = "@CSSC_Credit_System $ "
        self.prompt = "Guest" + self.default_prompt
    
    def do_clear(self, args):
        '''Clear the console of any texts.'''
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    
    # Authentication
    def do_register(self, args):
        '''Register a new account on the credit system.'''
        
        if self.account is not None:
            print("You are already logged in, please log out first.")
            return 1
        
        self.account = auth.register()
        
        if not self.account:
            return 1
        
        self.prompt = self.account.get("username") + self.default_prompt
        self.do_clear()
    
    def do_login(self, args):
        '''Login to an account on the credit system.'''
        if self.account is not None:
            print("You are already logged in, please log out first.")
            return 1
        self.account = auth.login()
        
        if not self.account:
            return 1

        self.prompt = self.account.get("username") + self.default_prompt
        self.do_clear()
        
    def do_logout(self, args):
        self.account = None
        self.prompt = "Guest" + self.default_prompt
        self.do_clear()

def main():
    CreditShell().cmdloop()

if __name__ == "__main__":
    main()