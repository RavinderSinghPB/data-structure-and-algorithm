def printSequence(inputStr):
    arr = ["2", "22", "222",
           "3", "33", "333",
           "4", "44", "444",
           "5", "55", "555",
           "6", "66", "666",
           "7", "77", "777", "7777",
           "8", "88", "888",
           "9", "99", "999", "9999"]
    # length of inputStr string
    n = len(inputStr)
    output = ""

    for i in range(n):

        # checking for space
        if inputStr[i] == ' ':
            output = output + "0"
        else:
            # calculating index for each
            # character
            position = ord(inputStr[i]) - ord('A')
            output = output + arr[position]
            # output sequence
    return output


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        inputStr = input()

        print(printSequence(inputStr))
