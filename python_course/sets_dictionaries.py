friends=["Rolf","ruth","charlie","Jen"]
guests=["Jose","Bob","Rolf","Charlie","michael"]

friends_lower={n.lower() for n in friends}
guests_lower={n.lower() for n in guests}


present_friends=friends_lower.intersection(guests_lower)
present_friends={name.title() for name in present_friends}


print(present_friends)



