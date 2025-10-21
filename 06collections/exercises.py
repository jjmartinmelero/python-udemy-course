# EX 1 ---------------------------------------------------------
print("Playlist app")

albums = []

n_songs = int(input("Number of songs to add: "))

for _ in range(n_songs):
    albums.append(input("Song: "))

# order
albums.sort(reverse=True)

# show list
print("Albums: ")

for song in albums:
    print(song)


# EX 2 ---------------------------------
print("Clasifications app")

califications = []

n_califications = int(input("Number of califications: "))

for _ in range(n_califications):
    califications.append(int(input("Calification: ")))

average = 0

# sum(list)

for calification in califications:
    average += calification

print(f"average: {average / n_califications}")


# EX 3 -------------------------------------------
print("Suscriptions app")
subscribers = set()

n_suscribers = int(input("n suscribers: "))

for _ in range(n_suscribers):
    subscribers.add(input("email suscriber: "))

print(subscribers)

new_suscriber = input("new suscriber: ")

if new_suscriber in subscribers:
    print("you can't add that suscriber :(")
else:
    subscribers.add(new_suscriber)
    print("addded !")

print(subscribers)

remove_subscriber = input("Remove suscriber: ")
subscribers.remove(remove_subscriber)

print(subscribers)


