import vim
import requests
import re
from bs4 import BeautifulSoup

session = requests.Session()

def LoginSession(payload):
    r = session.get('https://beta.atcoder.jp/login')
    soup = BeautifulSoup(r.text,"html.parser")
    csrf_token = soup.find(attrs = {'name' : 'csrf_token'}).get('value')
    payload['csrf_token'] = csrf_token

    session.post('https://beta.atcoder.jp/login' , data = payload)

def Login(username,password):
    payload = {
            'username' : username,
            'password' : password
            }
    LoginSession(payload)

def Submit(contest_id,problem_id,source):
    submit_page = session.get('https://beta.atcoder.jp/contests/%s/submit' % contest_id)
    submit_data = {
            'data.TaskScreenName': problem_id,
            'data.LanguageId' : vim.eval('g:AtCoderSubmitter#LanguageID'),
            'sourceCode' : source
            }
    soup = BeautifulSoup(submit_page.text,"lxml")
    csrf_token = soup.find(attrs = {'name' : 'csrf_token'}).get('value')
    submit_data['csrf_token'] = csrf_token
    result = session.post('https://beta.atcoder.jp/contests/%s/submit' % contest_id ,data = submit_data)

def SubmitCode(contest_id,problem_id):
    source = '\n'.join(vim.eval('getline(0,"$")'))
    Submit(contest_id,problem_id,source)

def ShowSubmissions(url,args):
    soup = BeautifulSoup(session.get(url , data = args).text,"html.parser")
    trs = soup.find("tbody").find_all("tr")
    vim.command('new ACSubmission')
    vim.command('setlocal buftype=nowrite ')
    for tr in trs:
        judge = tr.find(attrs = {'class' : re.compile('label label')}).text
        score = tr.find(attrs = {'class' : 'text-right submission-score'}).text
        problem = tr.find("a" , href = re.compile('tasks')).text
        user = tr.find("a" , href = re.compile('users')).text
        vim.current.buffer.append('{0} = [{1} - {2}] @{3}'.format(problem , judge , score , user))


def MySubmissions(contest_id):
    ShowSubmissions('https://beta.atcoder.jp/contests/%s/submissions/me' % contest_id,{})
