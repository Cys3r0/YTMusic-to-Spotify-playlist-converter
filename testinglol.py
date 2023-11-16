from testingytapi import dict_list_list

#Search request:

query = []
track_list = []
for dict in dict_list_list:
    for track in dict:
        track_list.append(track)
        for key, value in track.items():
            query.append(f"{key} {value}")


# for i in range(len(track_list)):
#     for key, value in track_list[i].items():
#         print(f"{key} AANNDD {value}")

def get_song(index):
    for key, value in track_list[index].items():
        return key

def get_artist(index):
    for key, value in track_list[index].items():
        return value

get_song(3)
get_artist(3)

