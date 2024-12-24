class Codec:
    #encode list of str --> str --> decode --> list of str
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        #input: takes a list of strs 
        #output: one string
        #task: convert this list of str into one sring
        #steps: convert every character into their ascii separated by a space between letters and a - between words for decoding and concatenate the numbers into a string
        coded_str = ""
        encoded_words= []
        for word in strs:#every word
            # for c in word:#every character
            #     # coded_str += str(ord(c))
            #     # coded_str += " " #separate by spaces

            #     coded_str = " ".join(str(ord(c)))
            encoded_word =  " ".join(str(ord(c)) for c in word)
            encoded_words.append(encoded_word)

            coded_str = "-".join(encoded_words)
       
        return coded_str

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        #input: takes a str
        #output: converts said str into a list of strings
        #task: convert this one str into the original list of strings
        #steps: split the string at the dash into strings representing the word
                # split each word at the space then join and append the str to the result array

        ans = []
        word_split = s.split("-")#word_split is holding a list of strings of int separator
        #print(word_split)
        for word in word_split:
            value = word.split()#value is holding a list of strings of each character of the current word
            print(value)
            value = map(int, value)
            value = "".join(map(chr, value))
            print(value)
            ans.append(value)

        return ans

            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))