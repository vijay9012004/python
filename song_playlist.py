class node:
    def __init__(self):
        value = None
        next = None

class SLL:
    def __init__(self):
        self.head = node()
        self.size = 0

    def InsertAt(self, value, pos):
        t = node()
        t.value = value

        if (self.size == 0 and pos == 0):
            self.head = t
            self.size += 1
            return True

        elif (pos == 0):
            t.next = self.head
            self.head = t
            self.size += 1
            return True

        elif (pos <= self.size and self.size != 0):
            temp = self.head
            for i in range (pos - 1):
                temp = temp.next
            t.next = temp
            temp.next = t
            self.size += 1
            return True

        else:
            print("Invalid insertion")

    def DeleteAt(self, pos):

        if (pos == 0):
            temp = self.head
            self.head = self.head.next
            temp.next = None

        elif (pos <= self.size and self.size != 0):
            temp = self.head
            for i in range (pos - 1):
                temp = temp.next
            temp.next = temp.next.next
            temp.next= None

        else:
            print("Empty list")

    def PrintAt(self, pos):
       
        if (pos <= self.size and self.size != 0):
            temp = self.head
            for i in range (pos - 1):
                temp = temp.next
            print(temp.value)

        else:
            print("Data not found")

    def Print(self):
       
        temp = self.head
        for i in range (self.size - 1):
          temp = temp.next
          print(temp.value)

Playlist_1 = SLL()

while True:
    print("1.Create playlist\n2.Insert song\n3.Delete song\n4.Select Song\n5.Display \n6.Exit")
    opt = int(input("Choose an option (1 - 6): "))

    match opt:
        case 1:
            limit = int(input("Enter no. of songs: "))
            for i in range (limit):
                song = input("Enter song name: ")
                flag = Playlist_1.InsertAt(song, i)
                if (flag):
                    print("Song added successfully")
                   
        case 2:
            pos = int(input("Enter position: "))
            song = input("Enter song name: ")
            Playlist_1.InsertAt(song, pos - 1)

        case 3:
            pos = int(input("Enter position: "))
            Playlist_1.DeleteAt(pos)

        case 4:
            pos = int(input("Enter position: "))
            Playlist_1.PrintAt(pos)

        case 5:
            pos = int(input("Enter the position"))
            Playlist_1.Print(self)

        case 6:
            break
           
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

