guests = ["Bill", "Valenok", "Ebanat"]

name = guests[0].title()
print(f"{name}, приходи на ужин.")

name = guests[1].title()
print(f"{name}, приходи на ужин.")

name = guests[2].title()
print(f"{name}, приходи на ужин.")

name = guests[1].title()
print(f"\nИзвините, {name} не сможет придти на ужин")

del(guests[1])
guests.insert(1, "Pidor")

name = guests[0].title()
print(f"\n{name}, приходи на ужин.")

name = guests[1].title()
print(f"{name}, приходи на ужин.")

name = guests[2].title()
print(f"{name}, приходи на ужин.")

print("\nУ нас есть стол побольше!")
guests.insert(0, "koncheni")
guests.insert(2, "mamont")
guests.append("tom")

name = guests[0].title()
print(f"\n{name}, приходи на ужин.")

name = guests[1].title()
print(f"{name}, приходи на ужин.")

name = guests[2].title()
print(f"{name}, приходи на ужин.")

name = guests[3].title()
print(f"{name}, приходи на ужин.")

name = guests[4].title()
print(f"{name}, приходи на ужин.")

name = guests[5].title()
print(f"{name}, приходи на ужин.")

print("\nПланы поменялись, на обед приглашаются только 2 гостя")

name = guests.pop().title()
print(f"\n{name} тебя не ждут на ужине")

name = guests.pop().title()
print(f"{name} тебя не ждут на ужине")

name = guests.pop().title()
print(f"{name} тебя не ждут на ужине")

name = guests.pop().title()
print(f"{name} тебя не ждут на ужине")

name = guests[0].title()
print(f"\n{name} жду тебя, приглашение остается в силе")

name = guests[1].title()
print(f"{name} жду тебя, приглашение остается в силе")

del guests[0]
del guests[0]

print(guests)
