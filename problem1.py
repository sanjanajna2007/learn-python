from random import randint
class train:
    def __init__(self, trainno):
        self.trainno = trainno

    def book(self, fro, to):
        print(f"ticket is booked in trainno : {self.trainno} from{fro} to {to}")

    def checkstatus(self):
        print(f"train no: {self.trainno } is running on time")

    def getfare(self):
        print(f"ticket fare ijn train no {self.trainno} from {fro} to {to} is {randint(222, 12121)}")

t = train(12512)

t.book("hubli", "bangalore")
t.book("hubli", "mangalore")