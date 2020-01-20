# プログラム言語: python3
# コンパイル方法: スクリプト言語のため、コンパイルは不要。
# 実行方法: ターミナル上でこのファイル名で実行
# 協力者: 山田遼太、木村優孝、渡辺将任

import string
import random


def make_random():
    li = list(string.ascii_letters)
    li[len(li): len(li)] = [" ", ",", ".", "-"]
    li = random.sample(li, len(li))
    return li
# ランダムな並びの重複しない文字列を発生


def make_dictionary():
    dic = {}
    plain = make_random()
    ran_char = random.sample(make_random(), len(plain))
    for i in range(len(plain)):
        dic[plain[i]] = ran_char[i]
    return dic
# 辞書の作成


def count_char(dic, sentence):
    li = dic.keys()
    count_dic = {}
    for char in li:
        count_dic[char] = sentence.count(char)
    return count_dic


if __name__ == '__main__':

    dic = make_dictionary()
    decode_dic = {}
    encode = []
    decode = []

    print("INPUT:")
    # 文字列（教師データ）の入力
    # https://www.bustle.com/p/21-classic-books-that-you-can-read-for-free-online-8483838 http://www.englishliteratureebooks.com/classicnovelsabridged.html から抜粋。数字や改行など不要な文字は全て削除している。
    sentence = "Bustle Search Bustle... Classic Books That You Can Read For Free Online By CHARLOTTE AHLIN Mar , mybookbathInstagram The classics. Theyre the bane of many a high schoolers existence. And yet, we all have one or two or classic books that weve been meaning to read... eventually. But when you walk into the bookstore, youre instantly distracted by all those shiny new books, and it seems like up and coming YA authors probably need your money a lot more than Charles Dickens does right now. Lucky for you, though, theres this secret, hidden realm known as the public domain, where you can read all the classics books your literary heart desires. Right now. For free. Websites like Project Gutenberg have collected tens of thousands of public domain books for your reading pleasure. You can download e-books for your phone or kindle, or just read them right there in your browser. So if youre looking for a free way to read more contemporary works, allow me to direct you to your friendly local library. But if youre looking to read up on the classics, right now, from the comfort of your own phone, laptop, or sci-fi ocular implant, then here are a whole slew of incredible books that can be found and legally read for free in the wilds of the web . Pride and Prejudice by Jane Austen Pride and Prejudice is the rom-com to end all rom-coms. Just try not to fall for the awkward, rich, emotionally repressed Mr. Darcy as he goes about unintentionally ruining Lizzies life and finally, awkwardly, sweeping her off her feet. . The Count of Monte Cristo by Alexandre Dumas The ultimate revenge tale still holds up over years later. In Alexandre Dumas classic novel, a man is imprisoned for a crime he didnt commit, and decides to deal with it by becoming fabulously wealthy and then utterly destroying the men who imprisoned him. . Dracula by Bram Stoker Every sexy vampire in modern media owes a huge debt to the original Count himself. Bram Stokers Dracula is rightfully known as one of the greatest horror stories of all time, complete with bloodsucking, shape-shifting, and one very charismatic Transylvanian. . Alices Adventures in Wonderland by Lewis Carroll The trippiest of classic childrens books is still a great read for adults. Join little Alice as she falls down a rabbit hole and deals with all kinds of weird nonsense while continually eating unidentified objects and changing size all over the place. . Adventures of Sherlock Holmes by Arthur Conan Doyle Sherlock Holmes is everyones favorite irritating detective, along with his long-suffering sidekick, Dr. John Watson. Read all about their adventures in this collection of mysteries, and put your own deductive powers to the test. . Frankenstein Or, The Modern Prometheus by Mary Wollstonecraft Shelley You probably know Frankensteins monster as that big flat-top fellow with the neck bolts. But if you read Mary Shelleys original novel, you just might discover that the real Frankensteins monster is a sensitive giant baby-man who speaks French and just wants to be loved. . Incidents in the Life of a Slave Girl, Written by Herself by Harriet A. Jacobs Incidents in the Life of a Slave Girl is the collected memoirs of Harriet Jacobs, who survived slavery in North Carolina and seven years of hiding in a tiny, coffin-like room. She eventually escaped to reunite with her children in the North, and wrote this beautifully nuanced account of her life and her perilous road to freedom. . The Complete Works of William Shakespeare by William Shakespeare Look, you dont really have to read all of Shakespeare. But you do have the option to, with this free edition of The Complete Works. Here youll find every last Shakespeare play, from the classic tragedies to the forgotten comedies to the very, very long histories. . Jane Eyre An Autobiography by Charlotte Bront Jane Eyre is a great book to read if youre considering getting married to your boss, but you havent yet checked his attic for any lurking ex-wives. Its a classic coming of age tale, a Gothic romance, and a surprisingly modern take on being a young, independent woman. . The Picture of Dorian Gray by Oscar Wilde The Picture of Dorian Gray teaches us all a valuable lesson hot guys are evil and not to be trusted. Sure, theres a little more to it than that, but youll just have to read it for yourself and find out. . Anne of Green Gables by L. M. Montgomery One of the top two spunky redheaded orphans named Anne, Anne of Green Gables is that rare, delightful character who never seems dated. Shes always there to cheer you up with her various scraps and fantasies and her bucolic Canadian country life. . Ulysses by James Joyce Ulysses is famous for being long and confusing, but now you can test that reputation for yourself. Sure, Joyces writing style is a little unconventional, but if you can get past the forty page run-on sentences, you might find that Ulysses is one of the strangest, funniest, most beautifully human books out there. . Little Women by Louisa May Alcott Four sisters grow up together in Louisa May Alcotts Little Women, dealing with minor trials and devastating tragedies as they go. Its a coming-of-age story that puts sisterhood front and center, in all its joy and frustration. . Narrative of the Life of Frederick Douglass, an American Slave by Frederick Douglass This is the first of Frederick Douglass three autobiographies, and by far his most widely read. Douglass recounts his harrowing childhood under slavery and his escape to the North, where he became one of Americas greatest orators and a national leader of the abolitionist movement. . Les Misrables by Victor Hugo Victor Hugo revolutionized the idea of writing fiction for social change with his stunning and very long novel, Les Misrables. Hugo tells the stories of various French citizens, all revolving around Jean Valjean, a man who was imprisoned for nineteen years for stealing a loaf of bread. . Great Expectations by Charles Dickens One of Dickens best loved works of fiction, Great Expectations has plenty of Dickensian orphans, reversals of fortune, poverty, crime, and one terrifying spinster in a rotting wedding dress. . Twenty Thousand Leagues Under the Sea by Jules Verne Lets clear this up once and for all the twenty thousand leagues refer to distance traveled while under water, not depth. They are not twenty thousand leagues deep. Also its one of the greatest hard sci-fi novels ever written. . Poems by Emily Dickinson by Emily Dickinson Join your new best friend Emily Dickinson for a reclusive journey out into nature, where you might brush up against all manner of flowers and also probably Death itself. . The Souls of Black Folk by W. E. B. Du Bois If youve heard the phrase double consciousness tossed around recently, thats a reference to The Souls of Black Folk by W. E. B. Du Bois. One of the seminal works in the history of sociology, this book collects some of the foundational essays about race in America, still all too relevant today. . The Works of Edgar Allan Poe Volume by Edgar Allan Poe by Edgar Allan Poe The Works of Edgar Allan Poe can be found online in several disturbing volumes, complete with all of his creepy poetry, his murderous tales, and everything in between. . The Awakening, and Selected Short Stories by Kate Chopin The Awakening is often credited as one of the first modern feminist novels. Chopins heroine gradually awakens to the fact that she, and most women, are systemically oppressed by society. So Edna decides to take her life into her own hands, regardless of what her husband or anybody else wants for her. NEWS ENTERTAINMENT BEAUTY FASHION LIFESTYLE BOOKS AWARDS SEASON MONTH VIDEO About UsAdvertiseTermsPrivacyDMCAContact UsCoupons Home Novels Poetry About Classic English Novels Abridged free ebooks. This is a collection of famous novels which have been shortened and slightly simplified for the general reader. These are not summaries each is half to two-thirds of the original length. Ive selected works that people often find daunting because of their density or complexity the aim is to make them easier to read, while keeping the style intact. Its hoped they will also appeal to students of English who are not quite ready to tackle the originals. There are currently eight books in the series Emily Brontes Wuthering Heights Jane Austens Mansfield Park George Eliots Daniel Deronda Laurence Sternes Tristram Shandy W.M.Thackerays Vanity Fair Elizabeth Gaskells North and South Charlotte Brontes Shirley Anthony Trollopes The Way We Live Now Coming in early  Charles Dickenss Bleak House More books will be added in due course. You can download them below, or from the ebook stores listed. All are free. Emily Brontes Wuthering Heights Abridged Emily Brontes complex book has at its heart the famous story of lovers Cathy and Heathcliff, but also contains a great deal more. Download epub, mobi for Kindle, pdf Or go to the books webpage at Nook Books iTunes store Kobo Books Smashwords for all ebook formats, or to read online Jane Austens Mansfield Park Abridged Timid young Fanny Price finds that life is not easy in the house of her grand relations. Janes Austens most serious novel is regarded by some as her greatest. Download epub, mobi for Kindle, pdf Or go to the books webpage at Nook Books iTunes store Kobo Books Smashwords for all ebook formats, or to read online George Eliots Daniel Deronda Abridged Two very different people influence each others lives the beautiful, worldly Gwendolen Harleth, and the idealistic Daniel Deronda, whose parentage is a mystery to him. Download epub, mobi for Kindle, pdf Or go to the books webpage at Nook Books iTunes store Kobo Books Smashwords for all ebook formats, or to read online Laurence Sternes Tristram Shandy Abridged An autobiography in which the narrator seldom gets much beyond his own birth, instead producing a bewildering bundle of anecdotes, musings and entertainment. Download epub, mobi for Kindle, pdf Or go to the books webpage at Nook Books iTunes store Kobo Books Smashwords for all ebook formats, or to read online W.M.Thackerays Vanity Fair Abridged Thackerays sweeping novel follows various families through the battle of Waterloo and beyond, all described with a satirical yet compassionate eye. Download epub, mobi for Kindle, pdf Or go to the books webpage at Nook Books iTunes store Kobo Books Smashwords for all ebook formats, or to read online Elizabeth Gaskells North and South Abridged A great novel of the Industrial Revolution southerner Margaret finds herself at loggerheads with stern northern mill-owner John Thornton. Includes an appendix on the books social context. Download epub, mobi for Kindle, pdf Or go to the books webpage at Nook Books iTunes store Kobo Books Smashwords for all ebook formats, or to read online Charlotte Brontes Shirley Abridged Two young women one based on Emily Bronte question their roles in a restrictive society. Download epub, mobi for Kindle, pdf If pdf fails to download, please try here. Anthony Trollopes The Way We Live Now Abridged Trollopes longest yet highly readable novel depicts a society in which money and ambition rule. Download epub, mobi for Kindle, pdf If pdf fails to download, please try here. You can buy an omnibus version of four of these abridged novels for Kindle at Amazon UK or Amazon USA It costs .., as I have not been able to make it free on Amazon. To download the full texts of these and other classic novels for free, try these websites Project Gutenberg Feedbooks Manybooks University of Adelaide ebook library See the classic poetry ebooks. About Emma Laybourn Home Page free ebook Emily Brontes Wuthering Heights Abridged free ebook Jane Austens Mansfield Park Abridged free ebook George Eliots Daniel Deronda Abridged free ebook Sternes Tristram Shandy Abridged free ebook Thackerays Vanity Fair Abridged free ebook Elizabeth Gaskells North and South Abridged free ebook Charlotte Brontes Shirley Abridged free ebook Trollopes The Way We Live Now Abridged"

    code = "WtORtGamvZJZDZTGt.GWTFPmthtCRGJvGjGmjZJtmjhGoTvTjoFPGDmJ TovJZRGhtFjZTSGJmGAoTjZToGWtORtGfoTjBGwjYjmrGWtORtGWTFPGJvGZPTGhjoCTvZGJmvZJZDZJtmG.toGPJCPToGTSDFjZJtmGJmGwjYjmGSTSJFjZTSGZtGvFJTmFTGjmSGZTFPmthtCRBGjmSGJvGCTmTojhhRGFtmvJSToTSGZtGzTGtmTGt.GZPTGptvZGYoTvZJCJtDvGDmJ TovJZJTvGJmGwjYjmrGWtORtGWTFPvGpjJmGFjpYDvGJvGhtFjZTSGjZGUtOjRjpjGtmGZPTGztDmSjoRGt.GXTCDotGjmSGUZjBGuJZPGJZvGpjJmGTmZojmFTG.jFJmCGZPTGUtOjRjpjGqZjZJtmrGUZPToGFjpYDvTvGjoTGhtFjZTSGJmGqDgDOjOTSjJGjmSGWjpjFPJrGWtORtGWTFPGJvGtoCjmJgTSGJmZtGvJLGvFPtthvBGuJZPJmGuPJFPGZPToTGjoTGt ToG.toZRGSTYjoZpTmZvGjmSGoTvTjoFPGFTmZTovrGWtORtGWTFPGTmothhTSG.tDoGZPtDvjmSvGvT TmGPDmSoTSvGZPJoZRGZPoTTGDmSToCojSDjZTvGjmSGtmTGZPtDvjmSG.tDoGPDmSoTSvGvJLZRG.tDoGCojSDjZTGvZDSTmZvG.toGZutGZPtDvjmSvG.J.ZTTmGZtGZutGZPtDvjmSGvJLZTTmrGaZGTpYhtRvGjotDmSGtmTGZPtDvjmSGjmSGtmTGPDmSoTSG.jFDhZRGpTpzTovrGWPTGDmJ TovJZRGPjvGzTTmGojmOTSGvTFtmSGJmGZutGZPtDvjmSvGThT TmGJmGZPTG.JThSGt.G,mCJmTToJmCGzRGqFtoTmj JrGamGjmtZPToGojmOJmCBGwjYjmTvTGYoTYGvFPtthGsjujJVDODGojmOTSGWtORtGWTFPGjvGZPTG.tDoZPGzTvZBGvTFtmSGtoGZPJoSGzTvZGJmG.topToGvTpTvZToGjmSG.JovZGJmGhjZZToGvTpTvZToGDmJ TovJZRGJmGwjYjmrGfFFtoSJmCGZtGbqGItohSGKmJ TovJZRGkjmOJmCvBGWtORtGWTFPGujvGojmOTSGZPJoSGJmGwjYjmGjmSGJmZTomjZJtmjhhRGojmOTSGZuTmZJTZPGJmGZPTG.JThSGt.G,mCJmTToJmCGjmSGWTFPmthtCRBGjmSG.J.ZRG.JovZGJmGejZDojhGvFJTmFTGJmGZutGZPtDvjmSvGThT TmrGWPTGDmJ TovJZRGujvGojmOTSGZPJoZRG.JovZGutohSuJSTGjFFtoSJmCGZtGAhtzjhGKmJ TovJZRGojmOJmCGjmSG.J.ZRGvT TmZPGJmGZutGZPtDvjmSvGThT TmGjFFtoSJmCGZtGbqGItohSGKmJ TovJZRGkjmOJmCvrGaZGujvGjhvtGojmOTSGZPJoZRG.JovZGutohSuJSTGjFFtoSJmCGZtGZPTGAhtzjhGKmJ TovJZRGkjmOJmCGJmGZutGZPtDvjmSvGThT Tmr"
    print("plain:")
    print(sentence)

    # 分布数を作成
    sentence_dic = count_char(dic, sentence)
    code_dic = count_char(dic, code)
    # 要素数順に並び替え
    sentence_sorted = sorted(sentence_dic.items(), key=lambda x: x[1])
    code_sorted = sorted(code_dic.items(), key=lambda x: x[1])
    print(type(code_sorted[0]))
    for num in range(len(sentence_dic)):
        decode_dic[code_sorted[num][0]] = sentence_sorted[num][0]
    print("OUTPUT:")

    # 分布数を表示
    print("original:")
    for key in sentence_sorted:
        print(key)
    print("gaved:")
    for key in code_sorted:
        print(key)
    print("maybe dictionary:")
    print("gaved: decode?")
    for index in decode_dic.items():
        print(index)

    # 復号文の作成
    for char in range(len(code)):
        decode.append(decode_dic[code[char]])

    # 復号文の出力
    print("decode:")
    for char in decode:
        print(char, end='')
    print("")
    # 問題点は文字の発生頻度からある程度使われている文字が推測されてしまうこと。
