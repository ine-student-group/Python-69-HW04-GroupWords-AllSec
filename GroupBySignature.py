def group_by_signature(words: list) -> list:
    def group_by_signature(words: list) -> list:
    dict_ = {}
    for i in words:
        sorted_ ="".join(sorted(i))
        if sorted_ not in dict_ and sorted_ !="":
            dict_[sorted_] = []
            
    for j in dict_.keys():
        for i in words:
            if j =="".join(sorted(i)) and j !="":
                dict_[j].append(i)
    result = []
    for i in dict_.values():
        result.append(i)
        
    return result

if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
