# heuristicsProject
A mock online shop that will be used to carry out a psychology dissertation on heuristics.

### Running
Start the project with the following commands:
```
cd Website
python3 server.py
```
If there are any errors then please see [this link](https://github.com/lei-ezz/heuristicsProject/tree/master/Website) to install the project.

This will start a local server on [`http://127.0.0.1:5000`](http://127.0.0.1:5000). Going to that URL, the participant data can be entered which will be used for trail. 

After entering in the data, one can start the experiment. When the experiment concludes, results will be stored as CSV to `/Website/results`, the page *should* also redirect back to the start for another trail.