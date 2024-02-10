def caesarCipher(s, k):
    if k > 26 :
        k =  (k%26)

    alphabet_a = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alphabet_A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    
    for i in s :
        
        if i in alphabet_a :
            answer += alphabet_a[alphabet_a.find(i)+k]
            print(alphabet_a.find(i))
        elif i in alphabet_A :
            answer += alphabet_A[alphabet_A.find(i)+k]
        else :
            answer += i

    return answer






