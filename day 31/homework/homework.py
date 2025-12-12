# parameter - ცვლადი რომელიც ფუნქციას გადაეცემა შექმნის დროს
# argument - როდესაც ფუნქციას გადაეცემა პარამაეტრის   გამოძახების დროს
List = [23,4,-3,-4,5]

def true_false(Grrr):
    negative = []
    positive = []
    for i in range(len(Grrr)):
        if Grrr[i] > 0:
            positive.append(Grrr[i])
        elif Grrr[i] < 0:
            negative.append(Grrr[i])
    return negative,positive

print(true_false(List))

        

    