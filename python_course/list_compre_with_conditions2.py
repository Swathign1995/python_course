friends=["Rolf","ruth","charlie","Jen"]
guests=["Jose","Bob","Rolf","Charlie","michael"]

friends_lower=set([f.lower() for f in friends])


present_friends=[
        name.title() for name in guests if name.lower() in friends_lower

        ]
print(present_friends)
