import random

NumOfFrames = 10

RollOne = random.randint(1,10)
print "RollOne is " + str(RollOne)

if RollOne ==10:
    FramePseudoScore = 10 
    RollType = "strike"
    print "FramePseudoScore is " + str(FramePseudoScore)
else:    
    RollTwo = random.randint(1,10-RollOne)
    print "RollTwo is " + str(RollTwo)
    FramePseudoScore = RollOne + RollTwo
    print "FramePseudoScore is " + str(FramePseudoScore)
    if FramePseudoScore == 10:
        RollType = "spare"
    else:
        RollType = "regular bowl"
        
print "FramePseudoScore is " + str(FramePseudoScore) + ", which is a " + RollType

FrameScore = 0

if RollType == "strike":
    FrameScore = FramePseudoScore + nextFramePseudoScore
elif RollType = "spare":
    FrameScore = FramePseudoScore + nextFrameRollOne
else:
    FrameScore += FramePseudoScore
    
daScore = 0
for frame in NumofFrames:
    daScore += FrameScore