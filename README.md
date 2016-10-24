# BandParse
This is a continued project worked on by Ernie Forzano and Herbert Gutierrez. The python script allows the user to enter a band name. This band name is then sent to LastFM's API in order to get a list of similar bands. This list comes as a JSON file and is converted to a python list. This list is then parsed and then sent to BandsInTown's API in order to get all of the events that the artists are playing. 

Accomplished:
* Set up the python script as the back end with flask. 
* The front end is a simple user interface using JavaScript. 
* The user can enter a band name, and will return a list of similar artists.

Future Goals: 
* Clean up the list displayed on the page. 
* Take that list of bands and create a YouTube playlist from the artists. 


