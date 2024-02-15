class Queue():
    def __init__(self):
        self.cards = []

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def push(self, card):
        self.cards.append(card)

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def pop(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            return None
        

if __name__ == '__main__':
    #REMOVE PASS AND YOUR CODE GOES HERE
    my_queue = Queue()
    my_queue.push("Card 1")
    my_queue.push("Card 2")
    my_queue.push("Card 3")
    print(my_queue.pop())
    print(my_queue.pop())
    print(my_queue.pop())