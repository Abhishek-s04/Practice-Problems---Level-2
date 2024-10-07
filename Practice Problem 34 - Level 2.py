'''Write a recursive python function which returns True if the input is well-formatted with respect to the list labels. Else it should return False.

We say that an input is well-formatted with respect to the labels if:
(a) input item is a list 
(b) input item has length at least two 
(c) input’s first item is in the list labels 
(d) each of the remaining items in input is either a string or a well-formatted list '''
def check_well_formatted(input_item, list_label):
    # Check if input_item is a list and has at least two elements
    if not isinstance(input_item, list) or len(input_item) < 2:
        return False
    
    # Check if the first item is in the list_label
    if input_item[0] not in list_label:
        return False
    
    # Check the remaining items
    for item in input_item[1:]:
        if isinstance(item, list):
            # If the item is a list, it must also be well-formatted
            if not check_well_formatted(item, list_label):
                return False
        elif not isinstance(item, str):
            # If the item is not a list, it must be a string
            return False

    # If all conditions are met, return True
    return True

# Test case
input_list1 = ['VP', ['V', 'eat']]
list_label1 = ['VP', 'V']
result = check_well_formatted(input_list1, list_label1)

if result:
    print("Well formatted")
else:
    print("Not Well formatted")
