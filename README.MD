Pipeline:
Collect sample data from Synthea (Data/raw folder)
Use helper methods to make some data invalid and save to new csv (Data/invalid) (blank, reference non-existant record, etc)
Validate data and toss rejected records into a new file (Data/rejected) along with their rejection reason 
Use helper method to messy up data, making data formats inconsistent (Data/messy)
Transform data into consistent formats and more to a new csv

raw -> invalid -> rejected -> summary/breakdown
               -> accepted ->

raw -> messy -> cleaned

end needs to be        
                       -> rejected -> summary/breakdown
raw -> messy & invalid 
                       -> accepted -> cleaned -> SQL



i should do messy and invalid data to the same csv file at one point 

Tech Stack:__
Python__
Pandas__
pytest__
Jupyter Notebooks__