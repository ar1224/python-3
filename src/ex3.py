def count_words(name)-> int:
   
    #Open/Modify files
    with open(name, "r") as input_file, open("large-words.txt", "w") as large, open("small-words.txt", "w") as small:
        set = set()
        for line in input_file:
            for word in line.strip().split():
                if word not in set:
                    set.add(word)
                    if len(word) >= 3: 
                        large.write(word+"\n")
                    else: 
                        small.write(word+"\n")
        return len(set)
 
 
 
def ex3():
    total_words = count_words("files/words.txt")
    print(f"Total words: {total_words}.")
 
ex3()
 
 