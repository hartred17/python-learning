def make_album(artist_name, album_name, number_of_tracks=None):
    """Возвращает словарь с названием альбома и исполнителем."""
    album_dict = {'artist': artist_name, 'album': album_name, 'tracks': number_of_tracks}
    if number_of_tracks:
        album_dict['tracks'] = number_of_tracks
    return album_dict 

while True:
    print("\nПриложение для создания словаря альбома и исполнителя.")
    print(f"(Нажмите 'q' чтобы завершить приложение.)")

    artist = input("\nВведите имя исполнителя: ")
    if artist == 'q':
        break
    
    album = input("\nВведите название альбома: ")
    if album == 'q':
        break

    glossary = make_album(artist, album)
    print(glossary)
