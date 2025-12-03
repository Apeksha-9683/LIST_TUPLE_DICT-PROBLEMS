
w=int(input("enter the number of books to be displayed: "))
lst=[]
i=1
while i<=w:
    books={}
    title=input("Enter book title: ")
    author=input("Enter the name of the author: ")
    year=input("Enter the year of the book publishment:  ")
    books["title"]=title
    books["author"]=author
    books["year"]=year
    lst.append(books)
    i+=1
print(lst)
for i in lst:
    print(f"The book titled '{i["title"]}' is authored by {i["author"]} and was published in the year {i["year"]}")



    