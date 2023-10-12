def reverse_sort_dictionary(dic): # create a function called sort_directory which dic is the arugument
    sorted_list = [] # create an empty list
    for name,(phone_number, age) in sorted(dic.items(), key = lambda x: x[1][1]): #Iterate the rough the dictionary using sorted function, that sort based onn age of the dictionary
        sorted_list.append((name,phone_number)) #append the name and phone number to the sorted_list
        return sorted_list
    