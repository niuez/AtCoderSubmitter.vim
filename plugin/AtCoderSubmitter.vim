if exists('g:loaded_atcoder_submitter')
  finish
endif

let g:loaded_atcoder_submitter = 1
let g:AtCoderSubmitter#LoggedIn = 0

scriptencoding utf-8

let s:save_cpo = &cpo
set cpo&vim

let s:submitter = yarp#py3('AtCoderSubmitter')

function! s:input(...) abort
  new
  cnoremap <buffer> <Esc> __CANCELED__<CR>
  try
    let input = call('input', a:000)
    let input = input =~# '__CANCELED__$' ? 0 : input
  catch /^Vim:Interrupt$/
    let input = -1
  finally
    bwipeout!
    return input
  endtry
endfunction

let g:AtCoderSubmitter#LanguageID = 3003
let g:AtCoderSubmitter#LoggedIn = 0
let g:AtcoderSubmitter#EasySubmitMode = 0

function g:AtCoderSubmitter#Submit()
  let contest_id = ""
  let problem_id = ""

	if g:AtcoderSubmitter#EasySubmitMode == 1:
		call s:submitter.notify('EasySubmit')		
		return
	endif

  if exists('g:AtCoderSubmitter#ContestID')	
    let contest_id = g:AtCoderSubmitter#ContestID
    let problem_code = input('problem_code: ')
    let problem_id = contest_id . '_' . problem_code
  else
    let contest_id = input('contest_id: ')
    let problem_id = input('problem_id: ')
  endif
  call s:submitter.notify('SubmitCode',contest_id,problem_id)
endfunction

function g:AtCoderSubmitter#Login()
  call s:submitter.notify('Login',$ATCODER_USERNAME,$ATCODER_PASSWORD)
endfunction

function g:AtCoderSubmitter#MySubmissions()
  let contest_id = input('contest_id :')
  call s:submitter.notify('MySubmissions',contest_id)
endfunction

com ACSubmit call g:AtCoderSubmitter#Submit()
com ACLogin call g:AtCoderSubmitter#Login()
com ACMySubmissions call g:AtCoderSubmitter#MySubmissions()


let &cpo = s:save_cpo
unlet s:save_cpo
