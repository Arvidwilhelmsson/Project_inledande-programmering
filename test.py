'''
str = "Python Programming"
text = str.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
dic = {}
for i in text:
    if i in vowels and i not in dic:
        dic.update({i:1})
    elif i in vowels and i in dic:
        dic[i] += 1
print(dic)
------------------------------------
lst1 = ["Alice", "Bob", "Charlie"]
lst2 = ["Bob", "Dan", "Alice"]
set1 = set(lst1)
set2 = set(lst2)
set3 = set1.intersection(set2)
lst3 = list(set3)
print(lst3)
-------------------------------------
tuple1 = (5, 2, 9, 2, 5, 2)
target = 2
lst = list(tuple1)
lst2 = []
ind = -1
for i in lst:
    ind += 1
    if i == target:
        lst2.append(ind)
tup = tuple(lst2)
print(tup)
-------------------------------------
'''
'''
Set = set.add()
Set = set.remove()
Dictionary = dictionary[key] – ger value från key, ger error meddelande om key ej finns
Dictionary = dictionary.get() – ger value från key, ger None om key ej finns
Dictionary = dictionary.update({key:value}); dictionary[newkey] = ‘newValue’
Dictionary = dictionary.pop() – tar bort värde för insatt nyckel
Dictionary = dictionary.popitem() – tar bort sista key-value paret du la in
Dictionary = dictionary.items() – ger en lista av tuples för key, value paren
Alla = alla.clear() – rensar allt, alla.copy() – kopierar datastrukturen
Tuple = (1, 2, 3, 4, 5, 6) – Går ej att lägga till förutom vid skapelsen
with open('filnamn.txt', 'r') as f:with open('filnamn.txt', 'w') as f:with open('filnamn.txt', 'a') as f:Exempel: with open('smilies.txt', 'w') as f:
os.path.isfile('filnamn.txt')Exempel: os.path.isfile('TheFalloftheHouseofUsher.txt')
for line in f:Exempel:with open('temps.txt', 'r') as file:for line in file:
f.readlines()Exempel: lyrics = shine.readlines()
f.write('Text\n')Exempel: pinkfloyd.write('Time\n')
'''
'''
return tupl # tuple (1, 2, 3)
def main():
    realtuple = function()
    first, middle, third = realtuple
'''
'''
lst = [ {'Atari ST': '1984'}, {'Intel i2':'1985'}]

for dic in lst:
    for key, value in dic.items():
        print(key, value)
'''
'''
lst = [1, 1, 3, -1, 4, 4]
sum = 0
for i in lst[::-1]:
    if i >= 0:
        sum += i
    else: break
print(sum)
print(lst)
'''

def word_frequency_analysis(file_name):
    file = open(file_name, 'r')
    word_counts = {}
    unique_words = set()
    word_length = []
   
    for line in file:
        words = line.strip().lower().replace('.', '').replace(',', '')
        words = words.split()
        for word in words:
            if word:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
                unique_words.add(word)
                word_length.append(len(word))
        sett = set()
        for key, value in word_counts.items():
            sett.add((value, key))
    sett = sorted(sett, reverse=True)
    sett = sett[0:10]
    return word_counts, unique_words, word_length, sett

test_fil = "Crime_and_punishment.txt"
counts, unique, lengths, settt = word_frequency_analysis(test_fil)




#print
print ("Top 10 most common words:")
counter = 0
percentage = int(0)


for number, word in settt:
    counter +=1
    #Procentuträkning för varje ord i top 10
    percentage = (number/len(lengths)) *100
    print(f'{counter}. {word:<10} {number} times ({percentage:.1f}%)')


print(f"Totalt antal unika ord: {len(unique)}")
print(f"Antal behandlade ord: {len(lengths)}")
word_frequency_analysis(test_fil)























