#Baye's Theorem is used to calculate probailities of events based on prior knowledge
def BayesProbability(A, B):
    FirstEvent = A
    SecondEvent = B
    MarginofError = (1-SecondEvent)
    Unaffected = (1-FirstEvent)
    Probability = ((FirstEvent*SecondEvent)/((FirstEvent*SecondEvent)+(Unaffected*MarginofError)))
    print(str(round(FirstEvent*100, 0))+ ' percent of the population have been diagnosed for Technophobia using a test with '+str(round(SecondEvent*100, 0))+' percent accuracy and a '+str(round(MarginofError*100, 0))+' percent margin of error, which means there\'s a '+str(round(Probability*100,0))+' percent probability that you may also suffer from Tehcnophobia.\n\n On a positive note, however '+str(round(Unaffected*100, 0))+' percent of our Cyber Citizens are most likely to be Source Code Fanatics!\n\n CyberNation: Code or DIY!')
    return Probability

BayesProbability(.05, .9)
