import requests,random,concurrent.futures,io
import EZProxyLib as ProxyManager

savename = ''
hits = []
fontsetting = ''
proxychoice = ''
regions = ['NA', 'OCE', 'TR', 'RU', 'LAS','LAN', 'KR', 'JP', 'EUW', 'EUNE', 'BR']
region = ''


def usergen(nameinput):
    global fontsetting
    namesplit = nameinput.split(' ')
    # Randomized Letter Lists
    al = ['a', '@', 'A', 'À', 'Á', 'Â', 'Ã', 'Ä',
          'Å', 'Æ', 'Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'ǽ']
    bl = ['b', 'B', 'ƀ', 'Ɓ', 'Ƃ', 'ƃ', 'Ƅ', 'ƅ']
    cl = ['c', 'C', 'ç', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ',
          'ċ', 'Č', 'č', 'Ɔ', 'Ƈ', 'ƈ', 'Ȼ', 'ȼ']
    dl = ['d', 'D', 'Ď', 'ď', 'Đ', 'đ', 'Ḋ', 'Ƿ']
    el = ['e', 'E', '£', 'È', 'É', 'Ë', 'è', 'é', 'ê', 'ë', 'Ê', '3']
    fl = ['f', 'F', 'ƒ', 'Ƒ']
    gl = ['g', 'G', 'Ĝ', 'ĝ', 'ğ', 'Ġ', 'ġ']
    hl = ['h', 'H', 'Ĥ', 'ĥ', 'Ħ', 'ħ', 'Ȟ']
    il = ['i', 'I', 'ɉ', 'ŀ', 'ľ', '1']
    jl = ['j', 'J', 'ǰ', 'ȷ', 'ɉ', 'Ɉ']
    kl = ['k', 'K', 'Ķ', 'ķ', 'ĸ', 'Ƙ', 'ƙ']
    ll = ['l', 'L', 'Ì', 'Í', 'Ï', 'Ĳ', 'Ĵ', 'ƪ', 'ȴ', '1']
    ml = ['m', 'M', 'Ħ']
    nl = ['n', 'N', 'ñ', 'Ń', 'ń', 'ņ', 'Ņ', 'ň', 'ŉ', 'Ŋ']
    ol = ['o', 'O', 'Ō', 'ō', 'Ŏ', 'Ő', 'Œ', 'Ɵ', 'ơ', 'Ʊ', 'Ǒ', 'Ǫ', '0']
    pl = ['p', 'P', 'þ', 'ƥ', 'ƿ']
    ql = ['q', 'Q', 'Ǫ', 'ǫ', 'Ǭ', 'ǭ']
    rl = ['r', 'R', 'Ŕ', 'Ŗ', 'Ř', 'ř', 'ŗ', 'Ʀ']
    sl = ['s', 'S', 'Ś', 'ś', 'Ŝ', 'ŝ', 'Ş', 'ş', 'Š']
    tl = ['t', 'T', 'Ţ', 'ţ', 'Ť', 'ť', 'Ŧ', 'ŧ']
    ul = ['u', 'U', 'Ù', 'Ú', 'Û', 'Ü', 'ù', 'ú', 'û', 'ü']
    vl = ['v', 'V', 'Ɣ']
    wl = ['w', 'W']
    xl = ['x', 'X']
    yl = ['y', 'Y', 'Ỳ', 'ỳ', 'ɏ', 'Ɏ', 'ȳ', 'Ȳ', 'Ƴ', 'ƴ', 'Ɣ']
    zl = ['z', 'Z', 'Ż', 'ż', 'Ż', 'ž']
    TOTALNAME = []
    plain_text_name = ""
    # Loops and creates random letters
    for x in namesplit:
        a1 = random.choice(al)
        b1 = random.choice(bl)
        c1 = random.choice(cl)
        d1 = random.choice(dl)
        e1 = random.choice(el)
        f1 = random.choice(fl)
        g1 = random.choice(gl)
        h1 = random.choice(hl)
        i1 = random.choice(il)
        j1 = random.choice(jl)
        k1 = random.choice(kl)
        l1 = random.choice(ll)
        m1 = random.choice(ml)
        n1 = random.choice(nl)
        o1 = random.choice(ol)
        p1 = random.choice(pl)
        q1 = random.choice(ql)
        r1 = random.choice(rl)
        s1 = random.choice(sl)
        t1 = random.choice(tl)
        u1 = random.choice(ul)
        v1 = random.choice(vl)
        w1 = random.choice(wl)
        x1 = random.choice(xl)
        y1 = random.choice(yl)
        z1 = random.choice(zl)
        # Parses and randomizes name
        if x in al or bl or cl or dl or el or fl or gl or hl or il or jl or kl or ll or ml or nl or ol or pl or ql or rl or sl or tl or ul or vl or wl or xl or yl or zl:
            if x == 'a':
                letter = a1
                TOTALNAME.append(letter)
            if x == 'b':
                letter = b1
                TOTALNAME.append(letter)
            if x == 'c':
                letter = c1
                TOTALNAME.append(letter)
            if x == 'd':
                letter = d1
                TOTALNAME.append(letter)
            if x == 'e':
                letter = e1
                TOTALNAME.append(letter)
            if x == 'f':
                letter = f1
                TOTALNAME.append(letter)
            if x == 'g':
                letter = g1
                TOTALNAME.append(letter)
            if x == 'h':
                letter = h1
                TOTALNAME.append(letter)
            if x == 'i':
                letter = i1
                TOTALNAME.append(letter)
            if x == 'j':
                letter = j1
                TOTALNAME.append(letter)
            if x == 'k':
                letter = k1
                TOTALNAME.append(letter)
            if x == 'l':
                letter = l1
                TOTALNAME.append(letter)
            if x == 'm':
                letter = m1
                TOTALNAME.append(letter)
            if x == 'n':
                letter = n1
                TOTALNAME.append(letter)
            if x == 'o':
                letter = o1
                TOTALNAME.append(letter)
            if x == 'p':
                letter = p1
                TOTALNAME.append(letter)
            if x == 'q':
                letter = q1
                TOTALNAME.append(letter)
            if x == 'r':
                letter = r1
                TOTALNAME.append(letter)
            if x == 's':
                letter = s1
                TOTALNAME.append(letter)
            if x == 't':
                letter = t1
                TOTALNAME.append(letter)
            if x == 'u':
                letter = u1
                TOTALNAME.append(letter)
            if x == 'v':
                letter = v1
                TOTALNAME.append(letter)
            if x == 'w':
                letter = w1
                TOTALNAME.append(letter)
            if x == 'x':
                letter = x1
                TOTALNAME.append(letter)
            if x == 'y':
                letter = y1
                TOTALNAME.append(letter)
            if x == 'z':
                letter = z1
                TOTALNAME.append(letter)
        else:
            print('Not Found')
    # This creates a string out of the split letters
    for x in TOTALNAME:
        plain_text_name += x
    # Returns the plain text name
    if fontsetting == '1':
        return plain_text_name.lower()
    elif fontsetting == '2':
        return plain_text_name.upper()
    elif fontsetting == '3':
        return plain_text_name


def SendName():
    global savename, hits, proxychoice, region
    if proxychoice == '1':
        ProxyManager.GrabProxiesHTTP('proxies.txt')
        ProxyManager.RefreshProxy()
        proxy = ProxyManager.http
    elif proxychoice == '2':
        ProxyManager.GrabProxiesSOCKS4('proxies.txt')
        ProxyManager.RefreshProxy()
        proxy = ProxyManager.socks4
    elif proxychoice == '3':
        ProxyManager.GrabProxiesSOCKS5('proxies.txt')
        ProxyManager.RefreshProxy()
        proxy = ProxyManager.socks5
    randomname = usergen(NameToSend)
    ProxyManager.RefreshProxy()
    if region == 'ALL':
        for x in regions:
            r = requests.get('https://lolnames.gg/en/'+x+'/' +randomname+'/', proxies=proxy, timeout=10)
            if ('class="text-center">'+randomname+' is available!</h4>') in r.content.decode():
                print('HIT | {}'.format(randomname))
                with io.open(savename + '_' +x+'_Hits.txt', "a", encoding="utf-8") as f:
                    f.write(randomname + '\n')
            elif ('class="text-center">'+randomname+' is available!</h4>') not in r.content.decode():
                print('FAIL | {}'.format(randomname))
    else:
        r = requests.get('https://lolnames.gg/en/'+region+'/' +randomname+'/', proxies=proxy, timeout=10)
        if ('class="text-center">'+randomname+' is available!</h4>') in r.content.decode():
            print('HIT | {}'.format(randomname))
            with io.open(savename + '_' +region+'_Hits.txt', "a", encoding="utf-8") as f:
                f.write(randomname + '\n')
        elif ('class="text-center">'+randomname+' is available!</h4>') not in r.content.decode():
            print('FAIL | {}'.format(randomname))

def init():
    global fontsetting, savename, NameToSend, proxychoice, regions, region
    choice = input(
        'Please Select What option you want\n1)Name Sniper based off input\nEnter Choice: ')
    if choice == '1':
        proxychoice = input('What Type of proxies would you like to use?\n1)HTTP\n2)Socks4\n3)Socks5\nEnter Choice: ')
        fontsetting = input('1)All lower case\n2)All cap\n3)No Preferance?\nEnter Choice: ')
        region = input('What Region would you like to check?\n1)NA\n2)OCE\n3)TR\n4)RU\n5)LAS\n6)LAN\n7)KR\n8)JP\n9)EUW\n10)EUNE\n11)BR\n12)All\nSelection: ')
        if region == '12':
            region = 'ALL'
        else:
            region = int(region) - 1
            region = regions[region]
        checkcount = input('Number of codes to check: ')
        maxthreads = input('Maximum concurrent threads: ')
        NameToSend = input('Please Enter Name with spaces (ex: t e s t): ')
        savename = NameToSend.replace(" ", "")
        with concurrent.futures.ThreadPoolExecutor(max_workers=int(maxthreads)) as executor:
            for index in range(int(checkcount)):
                executor.submit(SendName)
        input('Finished.... Press enter to exit')


init()
