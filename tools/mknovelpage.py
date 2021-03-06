import platform

def mknovelpage(bookid,bookname):
    bookid = '0'* (6-len(str(bookid))) + bookid
    if platform.system() == 'Windows':
        bookd = 'books\\' + bookid + '.html'
        bookdlink = 'novels\\' + bookid + '.html'
        booklist = 'books\\novellist.html'
    else:
        bookd = 'books/' + bookid + '.html'
        booklink = 'novels/' + bookid + '.html'
        booklist = 'books/novellist.html'
    title = '<head><title>' + bookname + '</title></head>'
    with open(bookd,'w+',encoding='utf-8') as f: # 创建书籍子页面,既章节列表页面
        str1 = '<h1>' + bookname + '</h1>'
        f.write(title)
        f.write(str1)
        f.write('\n\n')
        f.close()
    with open(booklist,'a+',encoding='utf-8') as f: # 将书籍子页面地址添加到书籍列表
        strs = '\n <a href="' + booklink + '" target="_blank">' + bookname + "</a><br>\n"
        f.write(strs)
        f.close()
    return bookd
