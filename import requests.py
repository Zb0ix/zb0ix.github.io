import requests
import os

# List of URLs for each Surah
surah_urls = [
"http://server11.mp3quran.net/minsh_mjwd/001.mp3",
"http://server11.mp3quran.net/minsh_mjwd/002.mp3",
"http://server11.mp3quran.net/minsh_mjwd/003.mp3",
"http://server11.mp3quran.net/minsh_mjwd/004.mp3",
"http://server11.mp3quran.net/minsh_mjwd/005.mp3",
"http://server11.mp3quran.net/minsh_mjwd/006.mp3",
"http://server11.mp3quran.net/minsh_mjwd/007.mp3",
"http://server11.mp3quran.net/minsh_mjwd/008.mp3",
"http://server11.mp3quran.net/minsh_mjwd/009.mp3",
"http://server11.mp3quran.net/minsh_mjwd/010.mp3",
"http://server11.mp3quran.net/minsh_mjwd/011.mp3",
"http://server11.mp3quran.net/minsh_mjwd/012.mp3",
"http://server11.mp3quran.net/minsh_mjwd/013.mp3",
"http://server11.mp3quran.net/minsh_mjwd/014.mp3",
"http://server11.mp3quran.net/minsh_mjwd/015.mp3",
"http://server11.mp3quran.net/minsh_mjwd/016.mp3",
"http://server11.mp3quran.net/minsh_mjwd/017.mp3",
"http://server11.mp3quran.net/minsh_mjwd/018.mp3",
"http://server11.mp3quran.net/minsh_mjwd/019.mp3",
"http://server11.mp3quran.net/minsh_mjwd/020.mp3",
"http://server11.mp3quran.net/minsh_mjwd/021.mp3",
"http://server11.mp3quran.net/minsh_mjwd/022.mp3",
"http://server11.mp3quran.net/minsh_mjwd/023.mp3",
"http://server11.mp3quran.net/minsh_mjwd/024.mp3",
"http://server11.mp3quran.net/minsh_mjwd/025.mp3",
"http://server11.mp3quran.net/minsh_mjwd/026.mp3",
"http://server11.mp3quran.net/minsh_mjwd/027.mp3",
"http://server11.mp3quran.net/minsh_mjwd/028.mp3",
"http://server11.mp3quran.net/minsh_mjwd/029.mp3",
"http://server11.mp3quran.net/minsh_mjwd/030.mp3",
"http://server11.mp3quran.net/minsh_mjwd/031.mp3",
"http://server11.mp3quran.net/minsh_mjwd/032.mp3",
"http://server11.mp3quran.net/minsh_mjwd/033.mp3",
"http://server11.mp3quran.net/minsh_mjwd/034.mp3",
"http://server11.mp3quran.net/minsh_mjwd/035.mp3",
"http://server11.mp3quran.net/minsh_mjwd/036.mp3",
"http://server11.mp3quran.net/minsh_mjwd/037.mp3",
"http://server11.mp3quran.net/minsh_mjwd/038.mp3",
"http://server11.mp3quran.net/minsh_mjwd/039.mp3",
"http://server11.mp3quran.net/minsh_mjwd/040.mp3",
"http://server11.mp3quran.net/minsh_mjwd/041.mp3",
"http://server11.mp3quran.net/minsh_mjwd/042.mp3",
"http://server11.mp3quran.net/minsh_mjwd/043.mp3",
"http://server11.mp3quran.net/minsh_mjwd/044.mp3",
"http://server11.mp3quran.net/minsh_mjwd/045.mp3",
"http://server11.mp3quran.net/minsh_mjwd/046.mp3",
"http://server11.mp3quran.net/minsh_mjwd/047.mp3",
"http://server11.mp3quran.net/minsh_mjwd/048.mp3",
"http://server11.mp3quran.net/minsh_mjwd/049.mp3",
"http://server11.mp3quran.net/minsh_mjwd/050.mp3",
"http://server11.mp3quran.net/minsh_mjwd/051.mp3",
"http://server11.mp3quran.net/minsh_mjwd/052.mp3",
"http://server11.mp3quran.net/minsh_mjwd/053.mp3",
"http://server11.mp3quran.net/minsh_mjwd/054.mp3",
"http://server11.mp3quran.net/minsh_mjwd/055.mp3",
"http://server11.mp3quran.net/minsh_mjwd/056.mp3",
"http://server11.mp3quran.net/minsh_mjwd/057.mp3",
"http://server11.mp3quran.net/minsh_mjwd/058.mp3",
"http://server11.mp3quran.net/minsh_mjwd/059.mp3",
"http://server11.mp3quran.net/minsh_mjwd/060.mp3",
"http://server11.mp3quran.net/minsh_mjwd/061.mp3",
"http://server11.mp3quran.net/minsh_mjwd/062.mp3",
"http://server11.mp3quran.net/minsh_mjwd/063.mp3",
"http://server11.mp3quran.net/minsh_mjwd/064.mp3",
"http://server11.mp3quran.net/minsh_mjwd/065.mp3",
"http://server11.mp3quran.net/minsh_mjwd/066.mp3",
"http://server11.mp3quran.net/minsh_mjwd/067.mp3",
"http://server11.mp3quran.net/minsh_mjwd/068.mp3",
"http://server11.mp3quran.net/minsh_mjwd/069.mp3",
"http://server11.mp3quran.net/minsh_mjwd/070.mp3",
"http://server11.mp3quran.net/minsh_mjwd/071.mp3",
"http://server11.mp3quran.net/minsh_mjwd/072.mp3",
"http://server11.mp3quran.net/minsh_mjwd/073.mp3",
"http://server11.mp3quran.net/minsh_mjwd/074.mp3",
"http://server11.mp3quran.net/minsh_mjwd/075.mp3",
"http://server11.mp3quran.net/minsh_mjwd/076.mp3",
"http://server11.mp3quran.net/minsh_mjwd/077.mp3",
"http://server11.mp3quran.net/minsh_mjwd/078.mp3",
"http://server11.mp3quran.net/minsh_mjwd/079.mp3",
"http://server11.mp3quran.net/minsh_mjwd/080.mp3",
"http://server11.mp3quran.net/minsh_mjwd/081.mp3",
"http://server11.mp3quran.net/minsh_mjwd/082.mp3",
"http://server11.mp3quran.net/minsh_mjwd/083.mp3",
"http://server11.mp3quran.net/minsh_mjwd/084.mp3",
"http://server11.mp3quran.net/minsh_mjwd/085.mp3",
"http://server11.mp3quran.net/minsh_mjwd/086.mp3",
"http://server11.mp3quran.net/minsh_mjwd/087.mp3",
"http://server11.mp3quran.net/minsh_mjwd/088.mp3",
"http://server11.mp3quran.net/minsh_mjwd/089.mp3",
"http://server11.mp3quran.net/minsh_mjwd/090.mp3",
"http://server11.mp3quran.net/minsh_mjwd/091.mp3",
"http://server11.mp3quran.net/minsh_mjwd/092.mp3",
"http://server11.mp3quran.net/minsh_mjwd/093.mp3",
"http://server11.mp3quran.net/minsh_mjwd/094.mp3",
"http://server11.mp3quran.net/minsh_mjwd/095.mp3",
"http://server11.mp3quran.net/minsh_mjwd/096.mp3",
"http://server11.mp3quran.net/minsh_mjwd/097.mp3",
"http://server11.mp3quran.net/minsh_mjwd/098.mp3",
"http://server11.mp3quran.net/minsh_mjwd/099.mp3",
"http://server11.mp3quran.net/minsh_mjwd/100.mp3",
"http://server11.mp3quran.net/minsh_mjwd/101.mp3",
"http://server11.mp3quran.net/minsh_mjwd/102.mp3",
"http://server11.mp3quran.net/minsh_mjwd/103.mp3",
"http://server11.mp3quran.net/minsh_mjwd/104.mp3",
"http://server11.mp3quran.net/minsh_mjwd/105.mp3",
"http://server11.mp3quran.net/minsh_mjwd/106.mp3",
"http://server11.mp3quran.net/minsh_mjwd/107.mp3",
"http://server11.mp3quran.net/minsh_mjwd/108.mp3",
"http://server11.mp3quran.net/minsh_mjwd/109.mp3",
"http://server11.mp3quran.net/minsh_mjwd/110.mp3",
"http://server11.mp3quran.net/minsh_mjwd/111.mp3",
"http://server11.mp3quran.net/minsh_mjwd/112.mp3",
"http://server11.mp3quran.net/minsh_mjwd/113.mp3",
"http://server11.mp3quran.net/minsh_mjwd/114.mp3"

]

# Directory to save the downloaded files
download_directory = "Surahs7"
os.makedirs(download_directory, exist_ok=True)

# Function to download a file from a URL
def download_file(url):
    local_filename = url.split('/')[-1]
    local_filepath = os.path.join(download_directory, local_filename)
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(local_filepath, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print(f"Downloaded {local_filepath}")
        return local_filepath
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

# Download all Surahs
for surah_url in surah_urls:
    print(f"Downloading {surah_url}...")
    filepath = download_file(surah_url)
    if filepath is None:
        print(f"Skipping {surah_url} due to error")

print("All Surahs have been downloaded successfully.")