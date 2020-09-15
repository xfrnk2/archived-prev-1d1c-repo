#https://www.acmicpc.net/submit/2079
arr4 = 'anavolimilana'
arr2 =  'abaccbcb'
arr = "lphbehiapswjudnbcossedgioawodnwdruaaxhbkwrxyzaxygmnjgwysafuqbmtzwdkihbwkrjefrsgjbrycembzzlwhxneiijgzidhngbmxwkhphoctpilgooitqbpjxhwrekiqupmlcvawaiposqttsdgzcsjqrmlgyvkkipfigttahljdhtksrozehkzgshekeaxezrswvtinyouomqybqsrtegwwqhqivgnyehpzrhgzckpnnpvajqevbzeksvbezoqygjtdouecnhpjibmsgmcqcgxwzlzztdneahixxhwwuehfsiqghgeunpxgvavqbqrelnvhnnyqnjqfysfltclzeoaletjfzskzvcdwhlbmwbdkxnyqappjzwlowslwcbbmcxoiqkjaqqwvkybimebapkorhfdzntodhpbhgmsspgkbetmgkqlolsltpulgsmyapgjeswazvhxedqsypejwuzlvegtusjcsoenrcmypexkjxyduohlvkhwbrtzjnarusbouwamazzejhnetfqbidalfomecehfmzqkhndpkxinzkpxvhwargbwvaeqbzdhxzmmeeozxxtzpylohvdwoqocvutcelgdsnmubyeeeufdaoznxpvdiwnkjliqtgcmvhilndcdelpnilszzerdcuokyhcxjuedjielvngarsgxkemvhlzuprywlypxeezaxoqfges"
def search_area(arr, start, k, dup, c, f):

    if f:
        if len(arr) <= k:
            return dup

        if arr[k-c] == arr[k]:
            dup += arr[k]
            c += 2
            return search_area(arr, start, k + 1, dup, c, f)
        else:
            # if k < c:
            if k-c+1 == start:
                return dup
            else:
                target = dup[0]
                box = ''
                for x in dup:
                    if x == target:
                        box += x
                    else:
                        break
                if 1 < len(box):
                    return box
                else:
                    return dup[0]



    else:
        if not dup:
            return search_area(arr, start, k+1, arr[start], c, f)

        if arr[k] == dup[-1]:

            return search_area(arr, start, k+1, dup + dup[-1], c, f)

        if arr[k] not in dup:
            dup += arr[k]
            return search_area(arr, start, k+1, dup, c, f)

        elif arr[k-c] == arr[k]:
            dup += arr[k]
            c += 2
            f = not f
            return search_area(arr, start, k+1, dup, c, f)

    return dup
results = []

i = 0
while i < len(arr):
    value = search_area(arr, i, i, '', 2, False)
    if value == arr[i]:
        i += 1
    else:
        i += len(value)
    results.append(value)
print(len(results))

