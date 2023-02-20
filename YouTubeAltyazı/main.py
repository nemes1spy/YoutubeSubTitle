import requests, json


subtitle = "https://youtube-media-downloader.p.rapidapi.com/v2/video/subtitles"
url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
headers = {
	"X-RapidAPI-Key": json.loads(open("config.json", mode="r").read())["apiKey"],
	"X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com",
}

def videoUrl(Id:str):
    response = requests.request("GET", url, headers=headers, params={"videoId": str(Id)})

    subtitleURL = (response.json()['subtitles']['items'][0]['url'])
    return subtitleURL

def SubTitle(Id:str):

    response = requests.get(subtitle, headers=headers, params={"subtitleUrl": videoUrl(Id)})
    return response.text


