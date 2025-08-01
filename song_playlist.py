class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None
class Playlist:
    def __init__(self):
        self.head = None
        self.size = 0
    def insert_song(self, title, position=None):    
        if position is None:
            position = self.size
        if position < 0 or position > self.size:
            print("Invalid position.")
            return
        new_node = SongNode(title)
        if self.size == 0: 
            self.head = new_node
        elif position == 0:  
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif position == self.size:  
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:  
            temp = self.head
            for _ in range(position):
                temp = temp.next
            prev_node = temp.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = temp
            temp.prev = new_node
        self.size += 1
        print(f'Song "{title}" inserted at position {position}.')

    def delete_song(self, title):
        if self.size == 0:
            print("Playlist is empty.")
            return
        current = self.head
        while current:
            if current.title == title:               
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                self.size -= 1
                print(f'Song "{title}" deleted.')
                return
            current = current.next
        print(f'Song "{title}" not found.')

    def display(self):
        if self.size == 0:
            print("Playlist is empty.")
            return
        temp = self.head
        pos = 0
        print("Playlist:")
        while temp:
            print(f"{pos}. {temp.title}")
            temp = temp.next
            pos += 1
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
            pos_input = input(f"Enter position to insert (0 to {playlist.size}, or leave empty for end): ")
            if pos_input.strip() == '':
                playlist.insert_song(song_title)
            else:
                try:
                    position = int(pos_input)
                    playlist.insert_song(song_title, position)
                except ValueError:
                    print("Invalid position input.")
        elif choice == '2':
            song_title = input("Enter song title to delete: ")
            playlist.delete_song(song_title)
        elif choice == '3':
            playlist.display()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
s
