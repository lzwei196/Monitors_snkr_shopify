import fbchat
import sys
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')



class Messenger():

    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd
        self.client = fbchat.Client(email, pwd)
        print('logged in')

    def get_uid(self, name):
        friends = self.client.searchForUsers(name)
        friend_count=0
        for friend in friends:
            if friend.is_friend==True:
                friend_count+=1
        if friend_count >1:
            print("WARNING: %s is not unique name in your friend's list" % name)

        friend = friends[0]
        return friend.uid

    def send_msg(self, uid, msg):
        sent = self.client.sendMessage(msg, thread_id=uid)
        if sent:
            print("Message sent successfully!")

if __name__ == '__main__':
    if len(sys.argv) <2:
        print('please pass in pwd as param')
        exit(0)

    pwd=sys.argv[1]
    print(pwd)
    username = "dark-soul-reaper@live.com"
    messenger = Messenger(username, pwd)
    uid = messenger.get_uid('Jolin Lu')
    # print(uid)
    # messenger.send_msg(uid, "more testing msg")
