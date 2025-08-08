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
           
