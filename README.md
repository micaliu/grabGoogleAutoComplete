grabGoogleAutoSuggest
=====================

Command line script to get keywords from Google Autosuggest given search term.

Modeled on https://www.youtube.com/watch?v=Z5MmeV6aeYE

Built like a UNIX command line utility.  For a file test.tx that contains keywor (one keyword/phrase per line):

~~~
cat test.txt | python grabGoogleAutoSuggest.py
~~~

Or to get keywords individually:

~~~
echo "kitchen" | python grabGoogleAutoSuggest.py
~~~

