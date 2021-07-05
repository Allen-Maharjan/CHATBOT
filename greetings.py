import random
def greetings(name):
    greetings_reply = ['Hello', 'Hi', 'Namaste']
    greetings_random = random.SystemRandom()
    #joining_tuple = ' '.join(args,)
    result=str((greetings_random.choice(greetings_reply)))
    return(result)