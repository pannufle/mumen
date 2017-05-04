import requests
import zipfile
import os
if __name__ == "__main__":
    url = "https://staff.fnwi.uva.nl/e.bruni/resources/MEN.zip"
    print(f"Downloading MEN resources from {url}...")
    reponse = requests.get(url, stream=True)
    if reponse.status_code == 200:
        if not os.path.isdir(".tmp/"):
            os.mkdir(".tmp")
        with open("MEN.zip", 'wb') as f:
            for chunk in reponse:
                f.write(chunk)
        print("Download done, extracting zip file...")
        with zipfile.ZipFile("MEN.zip", "r") as zip_ref:
            zip_ref.extractall("./")
        print("Extracting done, cleaning up...")
        os.remove("MEN.zip")
        print("Done.")
    else:
        print(f"!!! Download failed with code {reponse.status_code} !!!")
