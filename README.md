# BreakDown Poetry Analysis
Python script that analyzes poems and outputs information such as alliteration, rhyme scheme, and repetition.

# General info

BreakDown is a Python 3.0 script that analyzes poems for word repetition, positive/negative word connotations, line-by-line alliteration, and rhyme schemes (or stanzas that rhyme) and prints that information to the console. The ryhme schemes use the  <b>Natural Language Toolkit 3.0 (NLTK)</b> for Python, which can be downloaded from www.nltk.org. The NLTK library must be downloaded in order to run the script, however we only needed the CMUDictionary, so you can deselect everything else when installing NLTK.

This project was developed at the Swamphacks 2017 hackathon, and as such is incomplete: potential bugs may still exist, and since we only had 15 hours left, we didn't get to test <i>everything</i>...

# Usage

To use, create a .txt document in the same directory as the main.py file that contains the poem you want to analyze. Then run the Python script, type in the name of the text file (without .txt at the end) and let the magic unfold before your eyes.

It will print, in order:
<ol>
<li>Repeated words it finds in the poem</li>
<li>If a positive or negative connotation exists (checks negative/positive dictionaries to see if positive/negative words are present)</li>
<li>Line by line matches of alliteration (though not 100% accurate)</li>
<li>Debug code for rhyme scheme we didn't remove (oops)</li>
<li>Final rhyme scheme for the poem</li>
</ol>
Note that the rhyme scheme will take a few minutes to generate (due to NLTK's rhyme checking) so don't freak out if the program seems like it's not doing anything. It is.

Finally, feel free to fork our code or submit changes to it if you are interested.

<b> Developed at Swamphacks 2017 hackathon by Joseph Zilonka and Michael Lee.</b>
