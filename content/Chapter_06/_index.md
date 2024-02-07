+++
title = "More on Loops"
date = 2023-09-22T11:30:50-04:00
weight = 600
chapter = true
pre = "<b>6. </b>"
+++


</div>
<div class="section" id="tables">
<span id="index-7"></span><h2>6.9. Tables<a class="headerlink" href="#tables" title="Permalink to this headline">¶</a></h2>
One of the things loops are good for is generating tables.  Before
computers were readily available, people had to calculate logarithms, sines and
cosines, and other mathematical functions by hand. To make that easier,
mathematics books contained long tables listing the values of these functions.
Creating the tables was slow and boring, and they tended to be full of errors.

When computers appeared on the scene, one of the initial reactions was, *&#8220;This is
great! We can use the computers to generate the tables, so there will be no
errors.&#8221;* That turned out to be true (mostly) but shortsighted. Soon thereafter,
computers and calculators were so pervasive that the tables became obsolete.

Well, almost. For some operations, computers use tables of values to get an
approximate answer and then perform computations to improve the approximation.
In some cases, there have been errors in the underlying tables, most famously
in the table the Intel Pentium processor chip used to perform floating-point division.

Although a log table is not as useful as it once was, it still makes a good
example of iteration. The following program outputs a sequence of values in the
left column and 2 raised to the power of that value in the right column:


<div id="powersof2table" class="pywindow" >

<div id="powersof2table_code_div" style="display: block">
<textarea rows="2" id="powersof2table_code" class="active_code" prefixcode="undefined">
for x in range(13):   # Generate numbers 0 to 12
    print(str(x)+"\t"+str(2**x))</textarea>
</div>
<script type="text/javascript">
pythonTool.lineNumberFlags['powersof2table_code'] = true;
pythonTool.readOnlyFlags['powersof2table_code'] = false;
</script>

<div>
<button style="float:left" type='button' class='btn btn-run' id="powersof2table_runb">Run</button>
<button style="float:left; margin-left:150px;" type='button' class='btn' id="powersof2table_popb">Pop Out</button>
<button style="float:right" type="button" class='btn btn-reset' id="powersof2table_resetb">Reset</button>
<div style='clear:both'></div>
</div>

<div id='powersof2table_error'></div>

<div style="text-align: center">
<canvas id="powersof2table_canvas" class="ac-canvas" height="400" width="400" style="border-style: solid; display: none; text-align: center"></canvas>
</div>
<pre id="powersof2table_suffix" style="display:none">
</pre>
<pre id="powersof2table_pre" class="active_out">

</pre>

<div id="powersof2table_files" class="ac-files ac-files-hidden"></div>

</div>

The string ```"\t"``` represents a **tab character**. The backslash character in
```"\t"``` indicates the beginning of an **escape sequence**.  Escape sequences
are used to represent invisible characters like tabs and newlines. The sequence
```\n``` represents a **newline**.

An escape sequence can appear anywhere in a string; in this example, the tab
escape sequence is the only thing in the string. How do you think you represent
a backslash in a string?

As characters and strings are displayed on the screen, an invisible marker
called the **cursor** keeps track of where the next character will go. After a
```print``` function, the cursor normally goes to the beginning of the next
line.

The tab character shifts the cursor to the right until it reaches one of the
tab stops. Tabs are useful for making columns of text line up, as in the output
of the previous program. Because of the tab characters between the columns, the position of the second
column does not depend on the number of digits in the first column.

</div>
<div class="section" id="two-dimensional-tables">
<span id="index-8"></span><h2>6.10. Two-dimensional tables<a class="headerlink" href="#two-dimensional-tables" title="Permalink to this headline">¶</a></h2>
A two-dimensional table is a table where you read the value at the intersection
of a row and a column. A multiplication table is a good example. Let&#8217;s say you
want to print a multiplication table for the values from 1 to 6.

A good way to start is to write a loop that prints the multiples of 2, all on
one line:


<div id="multtablestep1" class="pywindow" >

<div id="multtablestep1_code_div" style="display: block">
<textarea rows="3" id="multtablestep1_code" class="active_code" prefixcode="undefined">
for i in range(1, 7):
    print(2 * i, end="   ")
print()</textarea>
</div>
<script type="text/javascript">
pythonTool.lineNumberFlags['multtablestep1_code'] = true;
pythonTool.readOnlyFlags['multtablestep1_code'] = false;
</script>

<div>
<button style="float:left" type='button' class='btn btn-run' id="multtablestep1_runb">Run</button>
<button style="float:left; margin-left:150px;" type='button' class='btn' id="multtablestep1_popb">Pop Out</button>
<button style="float:right" type="button" class='btn btn-reset' id="multtablestep1_resetb">Reset</button>
<div style='clear:both'></div>
</div>

<div id='multtablestep1_error'></div>

<div style="text-align: center">
<canvas id="multtablestep1_canvas" class="ac-canvas" height="400" width="400" style="border-style: solid; display: none; text-align: center"></canvas>
</div>
<pre id="multtablestep1_suffix" style="display:none">
</pre>
<pre id="multtablestep1_pre" class="active_out">

</pre>

<div id="multtablestep1_files" class="ac-files ac-files-hidden"></div>

</div>

Here we&#8217;ve used the ```range``` function, but made it start its sequence at 1.
As the loop executes, the value of ```i``` changes from 1 to
6. When all the elements of the range have been assigned to ```i```, the loop terminates.
Each time through the loop, it
displays the value of ```2 * i```, followed by three spaces.

Again, the extra ```end="</span>&nbsp;&nbsp; <span class="pre">"``` argument in the ```print``` function suppresses the newline, and
uses three spaces instead.  After the
loop completes, the call to ```print``` at line 3 finishes the current line, and starts a new line.

So far, so good. The next step is to **encapsulate** and **generalize**.

</div>
<div class="section" id="encapsulation-and-generalization">
<span id="index-9"></span><h2>6.11. Encapsulation and generalization<a class="headerlink" href="#encapsulation-and-generalization" title="Permalink to this headline">¶</a></h2>
Encapsulation is the process of wrapping a piece of code in a function,
allowing you to take advantage of all the things functions are good for.

Generalization means taking something specific, such as printing the multiples
of 2, and making it more general, such as printing the multiples of any
integer.

This function encapsulates the previous loop and generalizes it to print
multiples of ```n```:


<div id="multtablestep2" class="pywindow" >

<div id="multtablestep2_code_div" style="display: block">
<textarea rows="8" id="multtablestep2_code" class="active_code" prefixcode="undefined">
def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end="   ")
    print()

print_multiples(2)
print_multiples(3)
print_multiples(4)</textarea>
</div>
<script type="text/javascript">
pythonTool.lineNumberFlags['multtablestep2_code'] = true;
pythonTool.readOnlyFlags['multtablestep2_code'] = false;
</script>

<div>
<button style="float:left" type='button' class='btn btn-run' id="multtablestep2_runb">Run</button>
<button style="float:left; margin-left:150px;" type='button' class='btn' id="multtablestep2_popb">Pop Out</button>
<button style="float:right" type="button" class='btn btn-reset' id="multtablestep2_resetb">Reset</button>
<div style='clear:both'></div>
</div>

<div id='multtablestep2_error'></div>

<div style="text-align: center">
<canvas id="multtablestep2_canvas" class="ac-canvas" height="400" width="400" style="border-style: solid; display: none; text-align: center"></canvas>
</div>
<pre id="multtablestep2_suffix" style="display:none">
</pre>
<pre id="multtablestep2_pre" class="active_out">

</pre>

<div id="multtablestep2_files" class="ac-files ac-files-hidden"></div>

</div>

To encapsulate, all we had to do was add the first line, which declares the
name of the function and the parameter list. To generalize, all we had to do
was replace the value 2 with the parameter ```n```.

By now you can probably guess how to print a multiplication table &#8212; by
calling ```print_multiples``` repeatedly with different arguments. In fact, we
can use another loop:


<div id="multtablestep3" class="pywindow" >

<div id="multtablestep3_code_div" style="display: block">
<textarea rows="7" id="multtablestep3_code" class="active_code" prefixcode="undefined">
def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end="   ")
    print()

for i in range(1, 7):
    print_multiples(i)</textarea>
</div>
<script type="text/javascript">
pythonTool.lineNumberFlags['multtablestep3_code'] = true;
pythonTool.readOnlyFlags['multtablestep3_code'] = false;
</script>

<div>
<button style="float:left" type='button' class='btn btn-run' id="multtablestep3_runb">Run</button>
<button style="float:left; margin-left:150px;" type='button' class='btn' id="multtablestep3_popb">Pop Out</button>
<button style="float:right" type="button" class='btn btn-reset' id="multtablestep3_resetb">Reset</button>
<div style='clear:both'></div>
</div>

<div id='multtablestep3_error'></div>

<div style="text-align: center">
<canvas id="multtablestep3_canvas" class="ac-canvas" height="400" width="400" style="border-style: solid; display: none; text-align: center"></canvas>
</div>
<pre id="multtablestep3_suffix" style="display:none">
</pre>
<pre id="multtablestep3_pre" class="active_out">

</pre>

<div id="multtablestep3_files" class="ac-files ac-files-hidden"></div>

</div>

Notice how similar this loop is to the one inside ```print_multiples```.  All we
did was replace the ```print``` function with a function call. The output of this program is a multiplication table.

</div>
<div class="section" id="more-encapsulation">
<span id="index-10"></span><h2>6.12. More encapsulation<a class="headerlink" href="#more-encapsulation" title="Permalink to this headline">¶</a></h2>
To demonstrate encapsulation again, let&#8217;s take the code from the last section
and wrap it up in a function:


<div id="multtablefinal" class="pywindow" >

<div id="multtablefinal_code_div" style="display: block">
<textarea rows="10" id="multtablefinal_code" class="active_code" prefixcode="undefined">
def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end="   ")
    print()

def print_mult_table():
    for i in range(1, 7):
        print_multiples(i)

print_mult_table()</textarea>
</div>
<script type="text/javascript">
pythonTool.lineNumberFlags['multtablefinal_code'] = true;
pythonTool.readOnlyFlags['multtablefinal_code'] = false;
</script>

<div>
<button style="float:left" type='button' class='btn btn-run' id="multtablefinal_runb">Run</button>
<button style="float:left; margin-left:150px;" type='button' class='btn' id="multtablefinal_popb">Pop Out</button>
<button style="float:right" type="button" class='btn btn-reset' id="multtablefinal_resetb">Reset</button>
<div style='clear:both'></div>
</div>

<div id='multtablefinal_error'></div>

<div style="text-align: center">
<canvas id="multtablefinal_canvas" class="ac-canvas" height="400" width="400" style="border-style: solid; display: none; text-align: center"></canvas>
</div>
<pre id="multtablefinal_suffix" style="display:none">
</pre>
<pre id="multtablefinal_pre" class="active_out">

</pre>

<div id="multtablefinal_files" class="ac-files ac-files-hidden"></div>

</div>

This process is a common **development plan**. We develop code by writing lines
of code outside any function, or typing them in to the interpreter. When we get
the code working, we extract it and wrap it up in a function.

This development plan is particularly useful if you don&#8217;t know how to divide
the program into functions when you start writing. This approach lets you
design as you go along.

</div>
<div class="section" id="local-variables">
<span id="index-11"></span><h2>6.13. Local variables<a class="headerlink" href="#local-variables" title="Permalink to this headline">¶</a></h2>
You might be wondering how we can use the same variable, ```i```, in both
```print_multiples``` and ```print_mult_table```. Doesn&#8217;t it cause problems when
one of the functions changes the value of the variable?

The answer is no, because the ```i``` in ```print_multiples``` and the ```i``` in
```print_mult_table``` are *not* the same variable.

Variables created inside a function definition are local; you can&#8217;t access a
local variable from outside its home function. That means you are free to have
multiple variables with the same name as long as they are not in the same
function.

Python examines all the statements in a function &#8212; if any of them assign a value
to a variable, that is the clue that Python uses to make the variable a local variable.

The stack diagram for this program shows that the two variables named ```i``` are
not the same variable. They can refer to different values, and changing one
does not affect the other.


<div><img alt="Stack 2 diagram" src="_images/stack2.png" />
</div>
The value of ```i``` in ```print_mult_table``` goes from 1 to 6. In the diagram it
happens to be 3. The next time through the loop it will be 4. Each time through
the loop, ```print_mult_table``` calls ```print_multiples``` with the current value
of ```i``` as an argument. That value gets assigned to the parameter ```n```.

Inside ```print_multiples```, the value of ```i``` goes from 1 to 6. In the
diagram, it happens to be 2. Changing this variable has no effect on the value
of ```i``` in ```print_mult_table```.

It is common and perfectly legal to have different local variables with the
same name. In particular, names like ```i``` and ```j``` are used frequently as
loop variables. If you avoid using them in one function just because you used
them somewhere else, you will probably make the program harder to read.



## Other flavors of loops<

Sometimes we&#8217;d like to have the **middle-test** loop with the exit test in the middle
of the body, rather than at the beginning or at the end.  Or a **post-test** loop that
puts its exit test as the last thing in the body. Other languages have different
syntax and keywords for these different flavours, but Python just uses
a combination of ```while``` and ```if condition: break``` to get the job done.

A typical example is a problem where the user has to input numbers to be summed.
To indicate that there are no more inputs, the user enters a special value, often
the value -1, or the empty string.  This needs a middle-exit loop pattern:
input the next number, then test whether to exit, or else process the number:


The middle-test loop flowchart

<img alt="/pythonbook/images/mid_test_loop.png" class="last" src="/pythonbook/images/mid_test_loop.png" />


```
total = 0
while True:
    response = input("Enter the next number. (Leave blank to end)")
    if response == "":
        break
    total += int(response)
print("The total of the numbers you entered is "+str(total))
```


Convince yourself that this fits the middle-exit loop flowchart: line 3
does some useful work, lines 4 and 5 can exit the loop, and if they don&#8217;t
line 6 does more useful work before the next iteration starts.

The ```while bool-expr:``` uses the Boolean expression to determine whether to iterate again.
```True``` is a trivial Boolean expression, so ```while True:```  means *always do
the loop body again*.  This is a language *idiom* &#8212; a convention that
most programmers will recognize immediately. Since the expression on line 2
will never terminate the loop, (it is a dummy test) the programmer must arrange to
break (or return) out of the loop body elsewhere, in some other way (i.e. in lines 4 and 5 in
this sample).

Similarly, by just moving the ```if condition: break``` to the end of the loop body we
create a pattern for a post-test loop.  Post-test loops are used when you want to
be sure that the loop body always executes at least once (because the first test
only happens at the end of the execution of the first loop body).
This is useful, for example, if we want to play an interactive game against
the user &#8212; we always want to play at least one game:

```
while True:
    play_the_game_once()
    response = input("Play again? (yes or no)")
    if response != "yes":
        break
print("Goodbye!")
```
Hint: Think about where you want the exit test to happen

Once you&#8217;ve recognized that you need a loop to repeat something, think
about its terminating condition &#8212; when will I want to stop iterating?
Then figure out whether you need to do the test before starting
the first (and every other) iteration, or at the end of
the first (and every other) iteration, or perhaps in
the middle of each iteration.  Interactive programs that require input
from the user or read from files often need to exit their loops in the
middle or at the end of an iteration, when it becomes clear that there is
no more data to process, or the user doesn&#8217;t want to play our game anymore.


## Functions

A few times now, we have mentioned all the things functions are good for. By
now, you might be wondering what exactly those things are.  Here are some of
them:

<ol class="arabic simple">
<li>Capturing your mental chunking. Breaking your complex tasks into sub-tasks, and
giving the sub-tasks a meaningful name is a powerful mental technique.  Look back
at the example that illustrated the post-test loop: we assumed that we had a function
called ```play_the_game_once```.  This chunking allowed us to put aside the details
of the particular game &#8212; is it a card game, or noughts and crosses, or a role playing
game &#8212; and simply focus on one isolated part of our program logic &#8212; letting the player
choose whether they want to play again.</li>
<li>Dividing a long program into functions allows you to separate parts of the
program, debug them in isolation, and then compose them into a whole.</li>
<li>Functions facilitate the use of iteration.</li>
<li>Well-designed functions are often useful for many programs. Once you write
and debug one, you can reuse it.</li>
</ol>


