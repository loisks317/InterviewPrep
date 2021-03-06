# twitterHashes.py
#
# find the hashtag items
# determine most popular
#
# LKS, July 2016, for the Insight Program

madeUpList=[' cats are the best #cats',
            ' tacos are the best #tacos',
            ' I wish I were a #cat pleaseeee',
            ' do #cats like #burritoes',
            ' who am I #twitter']

collectedHashes=[]

for i in range(len(madeUpList)):
    # find the hash
    item=madeUpList[i].split()
    for ii in range(len(item)):
        if item[ii][0] == '#':
            # this is our hash tag
            collectedHashes.append(item[ii][1:])

# now find the most common
strCounter={}
listofStrings=[]
for j in range(len(collectedHashes)):
    try:
        strCounter[collectedHashes[j]]+=1
    except:
        strCounter[collectedHashes[j]]=1
        listofStrings.append(collectedHashes[j])

for kk in range(len(listofStrings)):
        print(listofStrings[kk]+': '+str(strCounter[listofStrings[kk]]))

# return the largest number
print('The most common hash is: ' + str( max(strCounter, key=strCounter.get)))
