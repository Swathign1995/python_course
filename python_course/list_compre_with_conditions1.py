friends=["Rolf","ruth","charlie","Jen"]
guests=["Jose","Bob","Rolf","Charlie","michael"]

friends_lower=set([f.lower() for f in friends])
guests_lower=set([g.lower() for g in guests])


print(friends_lower.intersection(guests_lower))


