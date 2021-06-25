def make_album(artist_name,album_title,number=None):
    output = f"Album title : {album_title}.\n"
    output += f"Artist name : {artist_name}.\n"
    if number:
        output += f"Number of songs : {number}. \n"
    return output
test1 = make_album('John','American',number = 3)
test2 = make_album('John','Life is Beautiful')
test3 = make_album('Leonardo','Macaroni')
print(test1)
print(test2)
print(test3)
