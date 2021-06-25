def make_album(artist_name,album_title,number=None):
    output = f"Album title : {album_title}\n"
    output += f"Artist name : {artist_name}\n"
    if number:
        output += f"Number of songs : {number}\n"
    return output
while True:
    print("Please tell me about this album : ")
    print("Enter 'q' to exit")
    artist_name = input("Artist name : \n")
    if artist_name == 'q':
        break
    album_title = input("Album title : \n")
    if album_title == 'q':
        break
    number = input("Number of songs :")
    if number == 'q':
        break
    formatted_album = make_album(artist_name,album_title,number)
    print(f"\n{formatted_album}")
