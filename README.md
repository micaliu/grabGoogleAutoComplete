grabGoogleAutoComplete
=====================

Command line script to get keywords from Google AutoComplete given search term.

Modeled on https://www.youtube.com/watch?v=Z5MmeV6aeYE

Built like a UNIX command line utility.  For a file `test.txt` that contains keyword (one keyword/phrase per line):

~~~
cat test.txt | python grabGoogleAutoComplete.py
~~~

Or to get keywords individually:

~~~
echo "kitchen" | python grabGoogleAutoComplete.py
~~~

