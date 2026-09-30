def group_anagrams(strs):
    anagrams_dict = {}

    for item in strs:
        word = item.lower()
        counts = [0] * 26

        for char in word:
            counts[ord(char) - ord("a")] += 1

        key = tuple(counts)

        if key in anagrams_dict:
            anagrams_dict[key].append(item)
        else:
            anagrams_dict[key] = [item]

    return list(anagrams_dict.values())


if __name__ == "__main__":
    strs = ["eat", "Tea", "tan", "ATE", "nat", "bat"]
    print(group_anagrams(strs))
