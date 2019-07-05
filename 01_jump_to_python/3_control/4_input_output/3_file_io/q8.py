
import sys

usernames = sys.argv[1:]
def greet_users (usernames):
     for usernames in sys.argv[1:]:
          print('hello,',usernames[:1].upper()+usernames[1:],"\n",end='')

greet_users(usernames)


