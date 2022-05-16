#
#By Rodrigo Noriega
#
#Data serialization
#
#
#

import pickle

friends1 = {"Dan": [20,"London", 55555555], "Maria":[25, "Madrid", 77777777]}
friends2 = {"Dan": [20,"London", 55555555], "Maria":[25, "Madrid", 77777777]}
friends = (friends1, friends2)

with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)

with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)

