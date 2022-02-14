def findaverage(dictionary):
    for key in dictionary:


        sumarray = 0
        for i in dictionary[key]:
            sumarray = sumarray + i
        avg = round(sumarray / len(dictionary[key]), 2)

        print(f"The average score for {key} is {str(avg)}")

dictionary = {
    'valentine':[20,30,40],
    'Romoe':[2,2,2],
    'Juliet':[2,3,3]
}

findaverage(dictionary)