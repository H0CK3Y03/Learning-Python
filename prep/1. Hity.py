import random

# for i in range(1, 159):
#     with open("karaoke.txt","a") as file:
#         file.write(f"{i}. song\n")

# with open("karaoke.txt", 'r') as file:
#     print(file.read())

songs = []
for i in range(1,159):
    songs += [f"{i}. song"]

song_playlist = random.choices(songs, k=20)
print(song_playlist)
print(len(song_playlist))