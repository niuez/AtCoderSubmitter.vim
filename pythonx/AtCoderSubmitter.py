import vim
import requests
import sys
from bs4 import BeautifulSoup

session = requests.Session()

def LoginSession(payload):
    r = session.get('https://beta.atcoder.jp/login')
    soup = BeautifulSoup(r.text,"lxml")
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
