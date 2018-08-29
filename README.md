# AtCoderSubmitter.vim

This is BETAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

## Dependencies
[nvim-yarp](https://github.com/roxma/nvim-yarp)

BeautifulSoup(python3)

requests(python3)

neovim(python3) --> `pip3 install neovim`

## Setting

Set environment variables `$ATCODER_USERNAME` and `$ATCODER_PASSWORD`

Set `g:AtCoderSubmitter#LanguageID`

```html
<option value="3003" data-mime="text/x-c++src">C++14 (GCC 5.4.1)</option>
<option value="3001" data-mime="text/x-sh">Bash (GNU bash v4.3.11)</option>
<option value="3002" data-mime="text/x-csrc">C (GCC 5.4.1)</option>
<option value="3004" data-mime="text/x-csrc">C (Clang 3.8.0)</option>
<option value="3005" data-mime="text/x-c++src">C++14 (Clang 3.8.0)</option>
<option value="3006" data-mime="text/x-csharp">C# (Mono 4.6.2.0)</option>
<option value="3007" data-mime="text/x-clojure">Clojure (1.8.0)</option>
<option value="3008" data-mime="text/x-common-lisp">Common Lisp (SBCL 1.1.14)</option>
<option value="3009" data-mime="text/x-d">D (DMD64 v2.070.1)</option>
<option value="3010" data-mime="text/x-d">D (LDC 0.17.0)</option>
<option value="3011" data-mime="text/x-d">D (GDC 4.9.4)</option>
<option value="3012" data-mime="text/x-fortran">Fortran (gfortran v4.8.4)</option>
<option value="3013" data-mime="text/x-go">Go (1.6)</option>
<option value="3014" data-mime="text/x-haskell">Haskell (GHC 7.10.3)</option>
<option value="3015" data-mime="text/x-java">Java7 (OpenJDK 1.7.0)</option>
<option value="3016" data-mime="text/x-java">Java8 (OpenJDK 1.8.0)</option>
<option value="3017" data-mime="text/javascript">JavaScript (node.js v5.12)</option>
<option value="3018" data-mime="text/x-ocaml">OCaml (4.02.3)</option>
<option value="3019" data-mime="text/x-pascal">Pascal (FPC 2.6.2)</option>
<option value="3020" data-mime="text/x-perl">Perl (v5.18.2)</option>
<option value="3021" data-mime="text/x-php">PHP (5.6.30)</option>
<option value="3022" data-mime="text/x-python">Python2 (2.7.6)</option>
<option value="3023" data-mime="text/x-python">Python3 (3.4.3)</option>
<option value="3024" data-mime="text/x-ruby">Ruby (2.3.3)</option>
<option value="3025" data-mime="text/x-scala">Scala (2.11.7)</option>
<option value="3026" data-mime="text/x-scheme">Scheme (Gauche 0.9.3.3)</option>
<option value="3027" data-mime="text/plain">Text (cat)</option>
<option value="3028" data-mime="text/x-vb">Visual Basic (Mono 4.0.1)</option>
<option value="3029" data-mime="text/x-c++src">C++ (GCC 5.4.1)</option>
<option value="3030" data-mime="text/x-c++src">C++ (Clang 3.8.0)</option>
<option value="3501" data-mime="text/x-objectivec">Objective-C (GCC 5.3.0)</option>
<option value="3502" data-mime="text/x-objectivec">Objective-C (Clang3.8.0)</option>
<option value="3503" data-mime="text/x-swift">Swift (swift-2.2-RELEASE)</option>
<option value="3504" data-mime="text/x-rust">Rust (1.15.1)</option>
<option value="3505" data-mime="text/x-sh">Sed (GNU sed 4.2.2)</option>
<option value="3506" data-mime="text/x-sh">Awk (mawk 1.3.3)</option>
<option value="3507" data-mime="text/x-brainfuck">Brainfuck (bf 20041219)</option>
<option value="3508" data-mime="text/x-sml">Standard ML (MLton 20100608)</option>
<option value="3509" data-mime="text/x-python">PyPy2 (5.6.0)</option>
<option value="3510" data-mime="text/x-python">PyPy3 (2.4.0)</option>
<option value="3511" data-mime="text/x-crystal">Crystal (0.20.5)</option>
<option value="3512" data-mime="text/x-fsharp">F# (Mono 4.0)</option>
<option value="3513" data-mime="text/x-unlambda">Unlambda (0.1.3)</option>
<option value="3514" data-mime="text/x-lua">Lua (5.3.2)</option>
<option value="3515" data-mime="text/x-lua">LuaJIT (2.0.4)</option>
<option value="3516" data-mime="text/x-moonscript">MoonScript (0.5.0)</option>
<option value="3517" data-mime="text/x-ceylon">Ceylon (1.2.1)</option>
<option value="3518" data-mime="text/x-julia">Julia (0.5.0)</option>
<option value="3519" data-mime="text/x-octave">Octave (4.0.2)</option>
<option value="3520" data-mime="text/x-nim">Nim (0.13.0)</option>
<option value="3521" data-mime="text/typescript">TypeScript (2.1.6)</option>
<option value="3522" data-mime="text/x-perl">Perl6 (rakudo-star 2016.01)</option>
<option value="3523" data-mime="text/x-kotlin">Kotlin (1.0.0)</option>
<option value="3524" data-mime="text/x-php">PHP7 (7.0.15)</option>
<option value="3525" data-mime="text/x-cobol">COBOL - Fixed (OpenCOBOL 1.1.0)</option>
<option value="3526" data-mime="text/x-cobol">COBOL - Free (OpenCOBOL 1.1.0)</option>
```

## Example

```
:call AtCoderSubmitter#Login()
:call AtCoderSubmitter#Submit()
contest_id :arc101
problem_id :arc101_a
OK? [y/n] :y
Submit
```
