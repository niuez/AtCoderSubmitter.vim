import vim
import requests
import sys
from bs4 import BeautifulSoup

def LoginSession(payload):
    s = requests.Session()
    r = s.get('https://beta.atcoder.jp/login')
    soup = BeautifulSoup(r.text,"lxml")
    csrf_token = soup.find(attrs = {'name' : 'csrf_token'}).get('value')
    payload['csrf_token'] = csrf_token

    s.post('https://beta.atcoder.jp/login' , data = payload)
    return s

def Submit(username,password,contest_id,problem_id,source,s):
    submit_page = s.get('https://beta.atcoder.jp/contests/%s/submit' % contest_id)
    submit_data = {
            'data.TaskScreenName': problem_id,
            'data.LanguageId' : vim.eval('g:AtCoderSubmitter#LanguageID'),
            'sourceCode' : source
            }
    soup = BeautifulSoup(submit_page.text,"lxml")
    csrf_token = soup.find(attrs = {'name' : 'csrf_token'}).get('value')
    submit_data['csrf_token'] = csrf_token
    result = s.post('https://beta.atcoder.jp/contests/%s/submit' % contest_id ,data = submit_data)

def SubmitCode(username,password,contest_id,problem_id):
    payload = {
            'username' : username,
            'password' : password
            }
    s = LoginSession(payload)
    source = '\n'.join(vim.eval('getline(0,"$")'))
    Submit(username,password,contest_id,problem_id,source,s)
