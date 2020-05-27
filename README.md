# Demo of Gooey

Built during 'Do-a-thon' at ResBaz Arizona 2020 to give a Python script a graphical user interface (GUI).

See the [Gooey](https://github.com/chriskiehl/Gooey) project for more information.

Note: The following instructions depend on a working version of Python 3.

## Installation Instructions 

Clone this project to your local machine:

```
git clone https://github.com/julianpistorius/irods-gooey.git
``` 

>Alternatively, you can manually download the source [here](https://github.com/julianpistorius/irods-gooey/archive/master.zip)

Navigate the directory where you cloned the repo and pip install the dependencies

```
cd irods-gooey/

python3 -m pip install -r requirements.txt 
``` 

Note: The upload step will fail unless you first install and configure the CyVerse IRODS iCommands. Please follow [these instructions](https://learning.cyverse.org/projects/data_store_guide/en/latest/step2.html).


## Running the example app

```
python3 irods_upload.py
```
