"""Download and extract MEN file.

Simple script to download MEN file from:
https://staff.fnwi.uva.nl/e.bruni/resources/MEN.zip

author: Martino Ferrari
author_email: martino.ferrari@etu.unige.ch
"""
import os
import zipfile
import requests


if __name__ == "__main__":
    MEN_URL = "https://staff.fnwi.uva.nl/e.bruni/resources/MEN.zip"
    print("Downloading MEN resources from {}...".format(MEN_URL))
    RESPONSE = requests.get(MEN_URL, stream=True)
    if RESPONSE.status_code == 200:
        if not os.path.isdir(".tmp/"):
            os.mkdir(".tmp")
        with open("MEN.zip", 'wb') as f:
            for chunk in RESPONSE:
                f.write(chunk)
        print("Download done, extracting zip file...")
        with zipfile.ZipFile("MEN.zip", "r") as zip_ref:
            zip_ref.extractall("./")
        print("Extracting done, cleaning up...")
        os.remove("MEN.zip")
        print("Done.")
    else:
        print("!!! Download failed with code {} !!!".format(
            RESPONSE.status_code))
