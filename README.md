# Enpass To PassLocker

Recently I switched from [Enpass](http://enpass.io/) to [PassLocker](http://innovationbox.com/passlocker/), because PassLocker has a simple, but usefull feature — it is located in your tray and always available on simple hotkey combination.

But I had almost 100 entries in Enpass and didn't want to transfer them manually. So I decided to write a converter from Enpass txt export to PassLocker csv import.

## Usage

Export your database from Enpass in txt format. Open terminal, run `python3 converter.py` with your file as argument. Then grab a `export.csv` file and import it to PassLocker.

## TODO

* Line-breaks in notes
* python 2
* Tests