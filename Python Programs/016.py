#Write a function to find sequences of lowercase letters joined with an underscore.

def lowerLettersJoinedWithUnderscore(str):

    result = []
    lstr = ""
    rstr = ""
    underscore = False
    for char in str:
        if 122>=ord(char)>=97 or char == "_":
            if char == "_":
                underscore = True
                continue
            if not underscore:
                lstr = lstr + char
            elif underscore:
                rstr = rstr + char
        elif lstr and rstr and underscore:
            result.append(lstr+"_"+rstr)
            lstr = ""
            rstr = ""
            underscore = False
        else:
            lstr = ""
            rstr = ""
            underscore = False
        print(lstr, rstr)
    return result
print(lowerLettersJoinedWithUnderscore("hehe_ha tyP_ol anik_Et Nor_maL"))