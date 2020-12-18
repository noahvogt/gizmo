#!/bin/sh

# script to convert a .md file (specified as a commandline argument)
# into a html + pdf documentation using 'markdown' and 'pandoc'

# exit if no argument given
[ -z "$1" ] && { echo "Error: Usage: build-doc [filename]"; exit 1; }
# compiling md to html (raw)

markdown -o "precomp.html" "$1"

# get directory of script
basename="$(dirname $0)"

# add code background + correct media path (for pandoc)
# (made crossplatfarm by assuming BSD-like SED)
sed "s/<pre><code>/<div><pre><code>/g;
	s/<\/code><\/pre>/<\/code><\/pre><\/div>/g;
	s/media\//\.\.\/media\//g;" precomp.html > tmp.html &&
	mv tmp.html precomp.html

pre="<!DOCTYPE html>
<html>
<meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\">
<title>gizmo documentation</title>
<style>
body {
	padding-top: 100px;
	padding-bottom: 10px;
	max-width: 800px;
	margin: auto;
}

.over {
	border: 1px solid black;
	padding: 20px;
	border-radius: 5px;	
	background: white;
	margin-bottom: 50px;
}

div {
	padding: 1px;
	padding-left: 10px;
	background: lightgrey;
}
</style>
</head>
<body>
<div class=\"over\">"

precomp=$(cat "precomp.html")

after="</div>
</body>
<hr>
<center>
	follow this project on 
	<a href="https://github.com/noahvogt/gizmo">github</a>
</center>
</html>"

# cat together all pieces for the output
echo "$pre$precomp$after" > "$basename/documentation.html"

# correct media path (for pandoc)
# (made crossplatfarm by assuming BSD-like SED)
if [ $basename != "." ]; then
	sed "s/\"\.\.\//\"/g;" "$basename/documentation.html" > tmp.html
	mv tmp.html "$basename/pandoc.html"
else
	cp "$basename/documentation.html" "$basename/pandoc.html"
fi

pandoc "$basename/pandoc.html" -f html -t pdf -o "$basename/documentation.pdf"

# remove temporary file
	rm precomp.html "$basename/pandoc.html"
