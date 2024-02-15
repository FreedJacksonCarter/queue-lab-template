class Queue():
    def __init__(self):
        self.cards = []

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def push(self, card):
        self.cards.append(0)

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def pop(self):
        if self.cards:
            return self.cards.pop(0)
        

if __name__ == '__main__':
    #REMOVE PASS AND YOUR CODE GOES HERE
    my_queue = Queue()