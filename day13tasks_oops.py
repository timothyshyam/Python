class laptop():
    def __init__(self,bn,colour,model):
        self.bn = bn
        self.colour  = colour
        self.model = model
    def watch(self,):
            print(f"you are watching from {self.bn} {self.model}.")
    def browsing(self,feed):
            print(f"you are browsing {feed} from {self.bn}.")
    def course(self,course,institute):
            print(f"you've enrolled {course} from {institute} through {self.bn} {self.model}.")
apple = laptop("apple","white","mac3")
apple.watch()
apple.browsing("wikipedia")
apple.course("adv python course","pythonlife")


