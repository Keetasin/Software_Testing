def funnyString(s):
    r = s[::-1]
    ascii_text_s = [ord(c) for c in s]
    ascii_text_r = [ord(c) for c in r]
    
    difference_s = [abs(ascii_text_s[i]-ascii_text_s[i+1]) for i in range(0,len(ascii_text_s)-1) ]
    difference_r = [abs(ascii_text_r[i]-ascii_text_r[i+1]) for i in range(0,len(ascii_text_r)-1) ]

    if difference_s == difference_r:
        return 'Funny'
    else:
        return 'Not Funny'