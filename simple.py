

a= "aeiou"
text=input("enter the string")
count=0
vowels_checker=text.lower()
for char in vowels_checker:
    if char in a:
        count+=1
print("No of counts",count)