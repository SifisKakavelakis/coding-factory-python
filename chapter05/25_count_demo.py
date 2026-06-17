def count_with_manual_loop(my_list):
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict:
            frequency_dict[item] +=1
        else:
            frequency_dict[item] = 1
        print("Manual loop:", frequency_dict)

def count_with_get_method(my_list):
    frequency_dict = {}
    for item in my_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
        print("Counte with get method:", frequency_dict)

def count_with_dict_compr(my_list):
    frequency_dict = {item: my_list.count(item) for item in my_list}
    print("Count with dict compr:", frequency_dict)

def main():
    my_list = ["apple", "banana", "kiwi", "apple", "orange", "banana", "apple", "kiwi", "melon", "kiwi", "kiwi"]

if __name__ == "__main__":
    main()