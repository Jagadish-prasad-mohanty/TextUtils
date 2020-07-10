from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request,"index.html")
def about(request):
    return HttpResponse("<h2>about jagdish</h2> <a href='/' title='google'>back to home</a>")
def analyze(request):
    dtext=request.POST.get('text','default')
    print(dtext)
    dcheck=request.POST.get('removepunc','off')
    dcheck1=request.POST.get('lowercase','off')
    dcheck2=request.POST.get('removenew','off')
    dcheck3=request.POST.get('rexspace','off')
    dcheck4=request.POST.get('uppercase','off')
    dcheck5=request.POST.get('charcounter','off')
    purposes=""
    if dcheck=="on":
        analyzed=""
        for i in dtext:
            if i not in string.punctuation:
                analyzed+=i
        param={'purpose':'remove punchuation','analyzing_text':analyzed}
        dtext=analyzed
        purposes+=(param['purpose'] + '|')

    if dcheck1 =="on":
        analyzed=''
        for i in dtext:
            analyzed+=(i.lower())
        param={'purpose':'convert to lowercase','analyzing_text':analyzed}
        dtext=analyzed
        purposes+=(param['purpose'] + '|')
    
    if dcheck2 =="on":
        analyzed=''
        for i in dtext:
            if i != "\n" and i !="\r":
                analyzed=analyzed+i
                print(analyzed)
        param={'purpose':'remove new line','analyzing_text':analyzed}
        dtext=analyzed
        purposes+=(param['purpose'] + '|')

    if dcheck3 =="on":
        analyzed=''
        for index,char in enumerate(dtext):
            if not(dtext[index]==" " and dtext[index+1]==" "):
                analyzed+=char
        param={'purpose':'remove extraspace','analyzing_text':analyzed}
        dtext=analyzed
        purposes+=(param['purpose'] + '|')
        
    if dcheck4 =="on":
        analyzed=''
        for i in dtext:
            analyzed+=i.upper()
        param={'purpose':'convert to uppercase','analyzing_text':analyzed}
        dtext=analyzed
        purposes+=(param['purpose'] + '|')
    
    if dcheck5 =="on":
        n=len(dtext)
        analyzed=f"{dtext}\nthe no of character in the textarea is {n}"
        param={'purpose':'character counter','analyzing_text':analyzed}
        purposes+=(param['purpose'] + '|')
    param['purpose']  =purposes 
    return render(request,"analyze.html",param)
    
def contact(request):
    return HttpResponse('''<table border='1'>
        <thead>
            <tr>
                <th>link</th>
                <th>desc</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><a href="http://www.google.com" title="Google">Google</a></td>
                <td><p>google is a great search engine</p></td>
            
            </tr>
            <tr>
                <td><a href="http://www.facebook.com" title="Facebook">Facebook</a></td>
                <td><p>facebook is a great social media</p></td>
            </tr>
        </tbody>
    </table>''')


    
