# temp-converter
This is a simple tool that allows teachers to grade student responses to temperature unit-conversion problems. The command line supports converting to and from the following units: Farenheit, Celcius, Rankine, Kelvin. You must specify your source
unit ( the unit to be converted), the target unit ( The unit to convert to), the starting temperature ( the tempearture to be converted), an answer ( the students answer to the conversion). After the conversion is performed, both the converted answer
and the students supplied answered are rounded to the one's place and compared for equality. If the answer is correct, the tool will display the message "correct". If the answer is incorrect, the tool will print "incorrect". If you do not supply the appropriate values,
The tool will output "invalid". 

## Installation

You will need python 3.x installed for this tool to work properly. It will likely work on python 2.x however it has not been tested for anything other then python 3. You will also need python-pip and python-virtualenv installed. Follow the guide [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) to install.

Steps to install

```
git clone https://github.com/zfeldstein/temp-converter
cd temp-converter 
virtualenv -p python3 tmp-venv
source tmp-venv/bin/activate
pip install -r ./requirements.txt
```


## Usage

Command line arguments
- -s or --source, this is the source unit to convert from, specified as either f,k,r,c
- -t or --target, this is the target unit to convert to, specified as either f,k,r,c
- -a or --answer, this is the answer the student supplied (i.e. 54)
- positional argument temperature, this is the intial temperature that was asked to be converted (i.e. 54)

# Example
If the student was asked to convert 54 degrees farenheit to celcius. You would run the following command if the student supplied the answer of 12
```
python main.py  -s f -t c 54 -a 12
Correct
```
