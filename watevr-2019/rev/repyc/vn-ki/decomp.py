佤 = 0
侰 = ~佤 * ~佤
俴 = 侰 + 侰

def 䯂(䵦):
    굴 = 佤
    굿 = 佤
    괠 = [佤] * 俴 ** (俴 * 俴)
    궓 = [佤] * 100
    괣 = []
    while 䵦[굴][佤] != '듃':
        굸 = 䵦[굴][佤].lower()
        亀 = 䵦[굴][侰:]
        if 굸 == '뉃':
            괠[亀[佤]] = 괠[亀[侰]] + 괠[亀[俴]]
        elif 굸 == '렀':
            괠[亀[佤]] = 괠[亀[侰]] ^ 괠[亀[俴]]
        elif 굸 == '렳':
            괠[亀[佤]] = 괠[亀[侰]] - 괠[亀[俴]]
        elif 굸 == '냃':
            괠[亀[佤]] = 괠[亀[侰]] * 괠[亀[俴]]
        elif 굸 == '뢯':
            괠[亀[佤]] = 괠[亀[侰]] / 괠[亀[俴]]
        elif 굸 == '륇':
            괠[亀[佤]] = 괠[亀[侰]] & 괠[亀[俴]]
        elif 굸 == '맳':
            괠[亀[佤]] = 괠[亀[侰]] | 괠[亀[俴]]
        elif 굸 == '괡':
            괠[亀[佤]] = 괠[亀[佤]]
        elif 굸 == '뫇':
            괠[亀[佤]] = 괠[亀[侰]]
        elif 굸 == '꼖':
            괠[亀[佤]] = 亀[侰]
        elif 굸 == '뫻':
            궓[亀[佤]] = 괠[亀[侰]]
        elif 굸 == '딓':
            괠[亀[佤]] = 궓[亀[侰]]
        elif 굸 == '댒':
            괠[亀[佤]] = 佤
        elif 굸 == '묇':
            궓[亀[佤]] = 佤
        elif 굸 == '묟':
            괠[亀[佤]] = input(괠[亀[侰]])
        elif 굸 == '꽺':
            궓[亀[佤]] = input(괠[亀[侰]])
        elif 굸 == '돯':
            print(괠[亀[佤]])
        elif 굸 == '뭗':
            print(궓[亀[佤]])
        elif 굸 == '뭿':
            굴 = 괠[亀[佤]]
        elif 굸 == '뮓':
            굴 = 궓[亀[佤]]
        elif 굸 == '뮳':
            굴 = 괣.pop()
        elif 굸 == '믃':
            if 괠[亀[侰]] > 괠[亀[俴]]:
                굴 = 亀[佤]
                괣.append(굴)
                continue
            elif 굸 == '꽲':
                괠[7] = 佤
                for i in range(len(괠[亀[佤]])):
                    if 괠[亀[佤]] != 괠[亀[侰]]:
                        괠[7] = 侰
                        굴 = 괠[亀[俴]]
                        괣.append(굴)

            elif 굸 == '꾮':
                괢 = ''
                for i in range(len(괠[亀[佤]])):
                    괢 += chr(ord(괠[亀[佤]][i]) ^ 괠[亀[侰]])

                괠[亀[佤]] = 괢
            elif 굸 == '꿚':
                괢 = ''
                for i in range(len(괠[亀[佤]])):
                    괢 += chr(ord(괠[亀[佤]][i]) - 괠[亀[侰]])

                괠[亀[佤]] = 괢
            elif 굸 == '떇':
                if 괠[亀[侰]] > 괠[亀[俴]]:
                    굴 = 괠[亀[佤]]
                    괣.append(굴)
                    continue
                elif 굸 == '뗋':
                    if 괠[亀[侰]] > 괠[亀[俴]]:
                        굴 = 궓[亀[佤]]
                        괣.append(굴)
                        continue
                    elif 굸 == '똷':
                        if 괠[亀[侰]] == 괠[亀[俴]]:
                            굴 = 亀[佤]
                            괣.append(굴)
                            continue
                        elif 굸 == '뚫':
                            if 괠[亀[侰]] == 괠[亀[俴]]:
                                굴 = 괠[亀[佤]]
                                괣.append(굴)
                                continue
                            elif 굸 == '띇':
                                if 괠[亀[侰]] == 괠[亀[俴]]:
                                    굴 = 궓[亀[佤]]
                                    괣.append(굴)
                                    continue
        굴 += 侰



䯂([['꼖', 0, 'Authentication token: '],
 ['꽺', 0, 0],
 ['꼖',
  6,
  'á×äÓâæíäàßåÉÛãåäÉÖÓÉäàÓÉÖÓåäÉÓÚÕæïèäßÙÚÉÛÓäàÙÔÉÓâæÉàÓÚÕÓÒÙæäàÉäàßåÉßåÉäàÓÉÚÓáÉ·Ôâ×ÚÕÓÔÉ³ÚÕæïèäßÙÚÉÅä×ÚÔ×æÔÉ×Úïá×ïåÉßÉÔÙÚäÉæÓ×ÜÜïÉà×âÓÉ×ÉÑÙÙÔÉâßÔÉÖãäÉßÉæÓ×ÜÜïÉÓÚÞÙïÉäàßåÉåÙÚÑÉßÉàÙèÓÉïÙãÉáßÜÜÉÓÚÞÙïÉßäÉ×åáÓÜÜ\x97ÉïÙãäãÖÓ\x9aÕÙÛ\x99á×äÕà©â«³£ï²ÕÔÈ·±â¨ë'],
 ['꼖', 2, 120],
 ['꼖', 4, 15],
 ['꼖', 3, 1],
 ['냃', 2, 2, 3],
 ['뉃', 2, 2, 4],
 ['괡', 0, 2],
 ['댒', 3],
 ['꾮', 6, 3],
 ['꼖', 0, 'Thanks.'],
 ['꼖', 1, 'Authorizing access...'],
 ['돯', 0],
 ['딓', 0, 0],
 ['꾮', 0, 2],
 ['꿚', 0, 4],
 ['꼖', 5, 19],
 ['꽲', 0, 6, 5],
 ['돯', 1],
 ['듃'],
 ['꼖', 1, 'Access denied!'],
 ['돯', 1],
 ['듃']]

)