def merge(list1, list2):
    i , j = 0 #set the index of list1 and list 2 to zero
    merged = [] #create an empty array 
    while i < len(list1) and j < len(list2): # while i and j is are less than the length of the list
        if list[i] <= list2[j]: #if element in list1 less than or equal to list2
            merged.append(list1[i]) #append the i element into the merged list
            i+=1 #increment the index to 1, mean move to the next element
        else:
            merged.append(list2[j]) #append the j element into the merged list
            j+=1 #increment the index to 1, mean move to the next element
    merged.extend(list1[i:]) #append the remainding element in list1 to merged list
    merged.extend(list2[j:]) #append the remainding element in list2 to merged list
    return merged
