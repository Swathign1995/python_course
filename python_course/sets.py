art_friends={"swathi","sgn"}
science_friends={"abc","xyz"}
art_friends.add("abc")
art_friends.remove("abc")
print(art_friends)



art_friends={"swathi","sgn"}
science_friends={"abc","sgn","xyz"}
art_but_not_science=art_friends.difference(science_friends)  #to check difference
science_but_not_art=science_friends.difference(art_friends)   
not_in_both=art_friends.symmetric_difference(science_friends)  
art_and_science=art_friends.intersection(science_friends)
all_friends=art_friends.union(science_friends)
print(art_but_not_science)
print(science_but_not_art)
print(not_in_both)
print(art_and_science)
print(all_friends)

