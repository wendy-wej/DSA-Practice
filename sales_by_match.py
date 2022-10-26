'''
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
def sockMerchant(n, ar):
    # Write your code here
    no_of_pairs = 0
    dict_of_colors = {}
    total_no_of_pairs = 0
    for i in range(n):
        count_color = ar.count(ar[i])
        if ar[i] not in dict_of_colors:
            dict_of_colors[ar[i]] = count_color
    print(dict_of_colors)

    for x in dict_of_colors:
        no_of_pairs = int(dict_of_colors[x] / 2)
        total_no_of_pairs += no_of_pairs 
    print(total_no_of_pairs)
   
sockMerchant(n, ar)
'''
'''
n= 100
c= [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1 ,0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1,0,1,0,0,0 ,1,0,1,0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
def jumpingOnClouds(c):
    # Write your code here
    good_clouds = []
    for i in range(n):
        if c[i]== 0:
            good_clouds.append(i)
    print(good_clouds)
    length = len(c)
    i = 0

    while i < length:
        x = good_clouds[i] + 1
        y = good_clouds[i] + 2
        if x in good_clouds and y in good_clouds: 
            good_clouds.remove(x)
            length = length
        i +=1
        print(good_clouds)
    mini = len(good_clouds)
    
    print(mini)

jumpingOnClouds(c)
'''
'''
n= 100
c= [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1 ,0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1,0,1,0,0,0 ,1,0,1,0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
def jumpingOnClouds(c):
    # Write your code here
    i = 0
    steps =0
    length = len(c) -1
    while i < length :
        if c[i] == 0 and c[i+2] == 0:
            i +=2
            steps +=1
        else:
            i +=1
            steps += 1
    print(steps)


jumpingOnClouds(c)
'''

'''
s = 'a'
n = 100000000000
def repeatedString(s, n):
    # Write your code here
    new_array = [i for i in str(s)]
    multiply = n // len(new_array)
    remainder = n % len(new_array)

    count = (new_array.count('a') * multiply ) + new_array[:remainder].count('a')
    return count

repeatedString(s, n)
'''

def isValid(s):
    # Write your code here
    # Write your code here
    string_arr = []
    string_dict ={}
    string_set = set()
  
    for i in s:
        string_set.add(i)
    print("set:",string_set)
    
    for i in string_set:
        string_arr.append(s.count(i))
    print("arr: ", string_arr)
        
    for i in string_arr:
        string_dict[i] = string_arr.count(i)
    print("dict: ",string_dict)
    
        
     
    if (len(string_dict) == 2):
        first_val = list(string_dict.values())[0]
        second_val = list(string_dict.values())[1]
        first_key = list(string_dict)[0]
        second_key = list(string_dict)[1]
        print(first_key, second_key)
        if (first_val <=1 or second_val <= 1):
            if abs(first_key - second_key) == 1:
                print("yes")
            else:
                print("no")
           
    elif (len(string_dict) < 2):
        print("yes")
        return "YES"
    elif (len(string_dict) > 2):
        print("no")
        return "NO"
            
    
    return "NO"
isValid("ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd")