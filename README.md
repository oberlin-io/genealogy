# genealogy
Genealogy data collected from disconnected paper-based family sources.

Standardized in a CSV relational database, wherein each person is assigned a unique ID `P000001`. I also incorporated decimal coordinates, from which Google Maps links can programmatically be created and a Maps API page can be built out.

## CSV Data Rules
*  Absolutely no double quotes.
*  Absolutely no commas, except in the Mention field.
*  The Mention field must be the last column (otherwise columns can be reordered).
   (At least until I fix the parser concerning double quotes.)
*  Don't change field names (row one),

## JavaScript-generated web page
[oberl.info/gen/gen.html](http://oberl.info/gen/gen.html)

