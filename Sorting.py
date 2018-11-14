def list_sort(listx):

   even = [] #[] stands for list
   odd = []
   characters = []
   mydict = dict()
   if not isinstance(listx, list):
       return 'Invalid Input'

   if not listx:
       mydict['evens'] = even
       mydict['odds'] = odd
       mydict['chars'] = characters
       return mydict

   for i in listx: # i is variable

       if isinstance(i, int):
           if i % 2 == 0:
               even.append(i)

           else:
               odd.append(i)

       elif isinstance(i, str): #elif elseif
           characters.append(i)

   mydict['evens'] = sorted(even)
   mydict['odds'] = sorted(odd)
   mydict['chars'] = sorted(characters)
   return mydict


print(list_sort([1, 3, 5, 2, 8, 'a', 'b']))