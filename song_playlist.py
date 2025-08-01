class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def insert_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f'Song "{title}" added.')

    def delete_song(self, title):
        current = self.head
        prev = None
        while current:
            if current.title == title:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f'Song "{title}" deleted.')
                return
            prev = current
            current = current.next
        print(f'Song "{title}" not found.')

    def display_playlist(self):
        if not self.head:
            print("Playlist is empty.")
            return
        print("Playlist:")
        current = self.head
        count = 1
        while current:
            print(f"{count}. {current.title}")
            current = current.next
            count += 1

def main():
    playlist = Playlist()

    while True:
        print("\nMenu:")
        print("1. Add song")
        print("2. Delete song")
        print("3. Display playlist")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            song_title = input("Enter song title to add: ")
            playlist.insert_song(song_title)
        elif choice == '2':
            song_title = input("Enter song title to delete: ")
            playlist.delete_song(song_title)
        elif choice == '3':
            playlist.display_playlist()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
