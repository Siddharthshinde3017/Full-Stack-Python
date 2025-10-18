class employee:
    def work(self):
        print("working emplayee")
class manager(employee):
    def manage(self):
        print("manages all clients")
class developer(employee):
    def develops(self):
        print("develop new thhings")
class techlead(manager,developer):
    def guide(self):
            print("guid the teams")

tl = techlead()
tl.work()
tl.manage()
tl.develops()
tl.guide()
