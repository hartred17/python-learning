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
