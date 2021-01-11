# gizmo
**gizmo** is a simple toolbox to create some simple melodies using python. The beauty about is, that you only need *a single motive* to create a little song.

*Note:* This program uses the [music21](https://github.com/cuthbertLab/music21) library.

## Licensing

Gizmo is a free (as in “free speech” and also as in “free beer”) Software. It is distributed under the GNU General Public License v3 (or any later version) - see the accompanying LICENSE file for more details.

## Dependencies
First of all you need [python3](https://www.python.org/downloads/) including the standard librarys. Now install the only needed additional module using pip:

	pip install music21

## the 'gizmo notation'
For a simple toolkit you need a simple notation that abides to the unix philsphoy. So we made a new one that consists simply of *lines in a plain text file*.

Every line contains the information about *one note*. Seperated by commas there are different attributes specified for each note. Every attribute seperated like this is called a **'part'**:

- The first part is a four characters long float that contains the *length* of the note in quarters.
- The second part is two to three chars long. The fist character is the note value (capitalized) and the second one the octave (as an integer). The third char is optional and just the key signature in the form of either "#" or "-".

Here an example in the *gizmo notation*:

	1.00,G4
	1.00,E4
	0.50,D4
	1.00,C#4

Now the same example in *sheet music*:

![](media/readme-example.png)

## Rendering
After you fully processed your music in the gizmo notation you can run it through the script called *final-converter* to export your work as a **.musicXML** file. This file can be viewed and further edited/processed in other free software like [MuseScore](https://github.com/musescore/MuseScore).
