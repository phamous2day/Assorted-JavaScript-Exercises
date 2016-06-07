# Directions

## Part 1: Basics

1. get a key https://developers.google.com/maps/documentation/javascript/get-api-key#key
2. Read https://developers.google.com/maps/documentation/javascript/tutorial#The_Hello_World_of_Google_Maps_v3
3. Copy-n-paste, replace YOUR_API_KEY - you will need to do this with every example - with your API Key and run the hello world example.
4. Change the center of the map to some place else. https://developers.google.com/maps/documentation/javascript/overlays#overlay_types
5. Change the zoom level.
6. Re-type the code to better commit the Google Maps JS API to your memory. You may copy-n-paste the really tedious parts like your API key.

## Part 2: Markers

5. Read https://developers.google.com/maps/documentation/javascript/markers
6. Copy-n-paste (hint: use the "click to copy" button on the top right) the marker-simple example (use the Javascript + HTML Tab) and run it: https://developers.google.com/maps/documentation/javascript/examples/marker-simple
7. Change the location of the marker to some place else. You will also want to change the center of the map so that you can see where the marker is.
8. Bonus: animate the dropping of the marker.
9. Copy & paste the https://developers.google.com/maps/documentation/javascript/examples/marker-labels example and run it.
10. Change the center of the map to some where in the US.
11. Change the zoom so that you can see the entire US.
12. Add markers - to various places in the US - to the map. See the "Some Place Coordinates" section below.
13. Read the API documentation for https://developers.google.com/maps/documentation/javascript/3.exp/reference#Marker and https://developers.google.com/maps/documentation/javascript/3.exp/reference#MarkerOptions
14. Change some options for when you create a Marker and see what happens.
15. Re-type the previous working example from scratch to better commit the Google Maps JS API to your memory. You can copy-n-paste the really tedious bits like your API key.

## Part 3: Showing and Hiding Markers

0. Read the "Remove a Marker" section of https://developers.google.com/maps/documentation/javascript/markers
1. Add two buttons to the page ( you may use jQuery - in which case you need to include jQuery, or use native DOM event listener methods ):
  1. "show markers" - shows all markers if they are hidden
  2. "hide markers" - hides all markers if they are shown
  3. You may refer to the https://developers.google.com/maps/documentation/javascript/examples/marker-remove example

## Part 4: Info Windows

1. Read https://developers.google.com/maps/documentation/javascript/infowindows
2. Get the code and run the https://developers.google.com/maps/documentation/javascript/examples/infowindow-simple example.
3. Change the pin to another location of your choice instead, and change the description in the info window to description that location. You may consult Wikipedia or other sources.
4. Read the API documentation for InfoWindow: https://developers.google.com/maps/documentation/javascript/reference#InfoWindow and https://developers.google.com/maps/documentation/javascript/reference#InfoWindowOptions
5. Change some options for when you create an InfoWindow and see what happens.
6. Take the marker code from Part 1, add the ability to open an info window on each marker when you click on it. Give each location a descriptive blurb.

## Part 5: Places API

1. Read https://developers.google.com/maps/documentation/javascript/places
2. Use the place-search example https://developers.google.com/maps/documentation/javascript/examples/place-search
3. Change the location and other parameters to the search and see what you get back.
4. Try using https://developers.google.com/maps/documentation/javascript/places#TextSearchRequests instead. Play with the parameters and see what you get.

## Part 6: Learn Another Feature

Choose another Google Maps API feature to learn. Here are some ideas:

* Geocoding / Reverse geocoding
* Directions
* Distance Matrix
* Elevation
* Street View
* Drawing Library
* Geometry Library
* Autocomplete for Addresses and Search
* Visualization Library
* Shapes
* Symbols
* Ground Overlays
* Custom Overlays

## Self-Learning Tips

1. Run the example first to get an overview of what your are going to be learning - and whether you want to learn it.
2. If you decide to learn it, read the documentation for the topic.
3. Get the code - either by copy & paste or by typing in the example in a local file. Run it to see it working.
4. Tweak the code example to make it do slightly different things.
5. Change variable names and function names to your liking.
6. Re-type the example if you've copy & pasted the first time.
7. Try to modify it more by combining the example with existing knowledge or other functionality.

## Some Place Coordinates

* Atlanta Tech Village: 33.773887, -84.402853
* Atlanta: 33.748995, -84.387982
* San Francisco: 37.774929, -122.419416
* New York City: 40.712784, -74.005941
* Austin: 30.267153, -97.743061
* Portland: 45.523062, -122.676482
* London: 51.507351, -0.127758
* Hong Kong: 22.396428, 114.109497
* Paris: 48.856614, 2.352222
* Istanbul: 41.008238, 28.978359
* Dubai: 25.204849, 55.270783

For more: http://www.latlong.net/

## Troubleshooting

If you see a "Oops! Something went wrong." error. Open your console. If you see InvalidKeyMapError, that means you need to put in your API key.
