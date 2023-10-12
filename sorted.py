
def reverse_sort_dictionary(input_dict):
    # Sort the dictionary by keys (names) in reverse order
    sorted_dict = sorted(input_dict.items(), key=lambda item: item[0], reverse=True)
    
    result_list = [(name, info[0]) for name, info in sorted_dict]
    
    return result_list

    
