import csv
class Release():
    def __init__(self,artist,title,label,style,rating,release_date,releaseId):
        self.artist = artist.lower()
        self.title = artist.lower()
        self.label = label
        self.style = style.split(", ")
        self.rating = rating
        self.release_date = release_date
        self.releaseId = releaseId
        
    #print out the release information as a string
    def str_release(self):
        return "artist = {},title = {}, label = {}, style = {}, rating = {}, year = {}, releaseID = {}".format(self.artist,self.title,self.label,self.style,self.rating,self.year,self.releaseId)

    #get field attribute
    def getField(self,fieldName):
        if fieldName == "artist":
            return self.artist
        elif fieldName == "title":
            return self.title
        elif fieldName == "release_date":
            return self.release_date
        
class Library():
    def __init__(self):
        self.releases = []

    #read line in text file
    def openFile(self,fileName):
        with open(fileName,'r') as f:
            next(f)
            reader = csv.reader(f,delimiter = '\t')
            for line in reader:
                self.releases.append(Release(line[0],line[1],line[2],line[3],line[4],line[5],line[6]))
            return self.releases
        
    #add a release to the library
    def add_release(self,artist,title,label,style,rating,release_date,release_id):
        self.releases[release_id] = Release(artist,title,label,style,rating,release_date)

    #swap two elements
    def swap(self,alist,item1,item2):
        temp = alist[item1]
        alist[item1] = alist[item2]
        alist[item2] = temp

    #left child of parent is 2n+1
    def left_child(self,n):
        return 2*n + 1

    #right child of parent is 2n+2
    def right_child(self,n):
        return 2*n + 2

    #check if elements are greater than each other and swap
    def moveDownTree(self,alist,begin,right,sortBy):
        left = self.left_child(begin)
        #if right child is greater than left
        while left <= right:
            #right child is bigger than parent
            if left < right and alist[left].getField(sortBy)< alist[left+1].getField(sortBy):
                left += 1
            #move down to the biggest child
            if alist[left].getField(sortBy) > alist[begin].getField(sortBy):
                self.swap(alist,left,begin)
                begin = left
                left = self.left_child(begin)
            else:
                return

    def heapSort(self, lst, sortBy ):
  # convert list to heap
      length = len( lst ) - 1
      lowest_parent = length / 2
      for i in range ( lowest_parent, -1, -1 ):
        self.moveDownTree( lst, i, length , sortBy)

  # flatten heap into sorted array
      for i in range ( length, 0, -1 ):
        if lst[0].getField(sortBy) > lst[i].getField(sortBy):
          self.swap( lst, 0, i )
          self.moveDownTree( lst, 0, i - 1 , sortBy)
      return lst

    def sortRelease(self,lst,sortBy):
        return self.heapSort(lst,sortBy)
  
    def sortByArtist(self,lst):
        return self.sortRelease(lst,"artist")

    def sortByYear(self,lst):
        return self.sortRelease(lst,"release_date")

    def sortByTitle(self,lst):
        return self.sortRelease(lst,"title")

db = Library()
txt = db.openFile("Music database - test data - Sheet1.tsv")
db.sortRelease(txt,"artist")
for i in txt:
    print i.artist

    
