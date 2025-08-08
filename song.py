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
            

        elif (pos == 0):
            t.next = self.head
            self.head = t
            self.size += 1
            

        elif (pos <= self.size and self.size != 0):
            temp = self.head
            for i in range (pos - 1):
                temp = temp.next
            t.next = temp
            temp.next = t
            self.size += 1
            

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
            temp.next.next = None

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
    print("1.Create playlist\n2.Insert song\n3.Delete song\n4.Display \n5.Exit")
    opt = int(input("Choose an option (1 - 6): "))
    if opt == 1:
        
        for i in range(opt):
            song = input(f"Enter song name : ")
            if Playlist_1.InsertAt(song, i):
                print("Song added successfully")

    elif opt == 2:
        pos = int(input("Enter position to insert at (1-based): ")) - 1
        song = input("Enter song name: ")
        if Playlist_1.InsertAt(song, pos):
            print("Song inserted successfully")

    elif opt == 3:
        pos = int(input("Enter position to delete (1-based): ")) - 1
        if Playlist_1.DeleteAt(pos):
            print("Song deleted successfully")

    elif opt == 4:
        print("Playlist:")
        Playlist_1.Print()

    elif opt == 5:
        print("Exiting...")
        break

    else:
        print("Choose a valid option")
