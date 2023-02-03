import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bonhams.com/_next/data/LHCdNBs3UymY35cy1_aIx/default/auction/28352/american-art-bonhams-skinner.json?page=1&auctionId=28352&auctionName=american-art-bonhams-skinner"

response = json.loads(requests.request('GET', url, headers={}, data={}).text)

auctionHouseNameList = []
auctionLocationList = []
auctionNumberList = []
auctionStartDateList = []
auctionEndDateList = []
auctionNameList = []
lotNumList = []
priceEstimateMinList = []
priceEstimateMaxList = []
priceSoldList = []
artistNameList = []
artistNantionalityList = []
artistBirthList = []
artistDeathList = []
artWorkNameList = []
artWorkMaterialsList = []
artWorkMarkingList = []
artWorkMeasurementsHeightList = []
artWorkMeasurementsWidthList = []
artWorkMeasurementsDepthList = []
artWorkMeasurementUnitList = []
artWorkMeasurementsNotesList = []
artWorkImage1List = []
artWorkImage2List = []
artWorkImage3List = []
artWorkImage4List = []
artWorkImage5List = []
lotUrlList = []

for i in range(len(response['pageProps']['lotData']['auctionLots'])):
    print(i)
    auctionHouseNameList.append(response['globalProps']['brand'].upper())
    auctionLocationList.append(response['pageProps']['auction']['sVenue'])
    auctionNumberList.append(response['pageProps']['auction']['iSaleNo'])
    auctionStartDateList.append(pd.to_datetime(response['pageProps']['auction']['dtStartUTC']).to_pydatetime().date())
    auctionEndDateList.append(pd.to_datetime(response['pageProps']['auction']['end_time_utc']).to_pydatetime().date())
    auctionNameList.append(response['pageProps']['auction']['sSaleName'])
    lotNumList.append(response['pageProps']['lotData']['auctionLots'][i]['lotId'])
    priceEstimateMinList.append(response['pageProps']['lotData']['auctionLots'][i]['price']['estimateLow'])
    priceEstimateMaxList.append(response['pageProps']['lotData']['auctionLots'][i]['price']['estimateHigh'])
    priceSoldList.append(response['pageProps']['lotData']['auctionLots'][i]['price']['hammerPremium'])

    soup = BeautifulSoup(response['pageProps']['lotData']['auctionLots'][i]['_highlightResult']['catalogDesc']['value'], 'html.parser')
    lotNameClass = soup.find("div", {"class": "LotName"})
    lotDescClass = soup.find("div", {"class": "LotDesc"})

    if lotDescClass:
        artistName = lotNameClass.text.split("(")
        if len(artistName) == 2:
            artistNameList.append(artistName[0])
            if ',' in artistName[1]:
                newData = artistName[1].split(', ')
                artistNantionalityList.append(newData[0])
                if '-' in newData[1]:
                    artistBirthList.append(newData[1].split('-')[0])
                    artistDeathList.append(newData[1].split('-')[1].replace(')', ''))
                else:
                    artistBirthList.append(newData[1].split(' ')[1].replace(')', ''))
                    artistDeathList.append('')
            else:
                artistNantionalityList.append('')
                artistBirthList.append(artistName[1].replace(')', ''))
                artistDeathList.append('')
        elif len(artistName) == 3:
            artistNameList.append(f"{artistName[0]} {artistName[1].replace(')', '')}")
            newData = artistName[2].split(', ')
            artistNantionalityList.append(newData[0])
            if '-' in newData[1]:
                artistBirthList.append(newData[1].split('-')[0])
                artistDeathList.append(newData[1].split('-')[1].replace(')', ''))
            else:
                artistBirthList.append(newData[1].split(' ')[1].replace(')', ''))
                artistDeathList.append('')
        else:
            artistNameList.append('')
            artistNantionalityList.append('')
            artistBirthList.append('')
            artistDeathList('')

        iList = soup.find("div", {"class": "LotDesc"}).findAll('i')
        if len(iList) == 1:
            mainString = iList[0].text.split(" ")
            if len(mainString) == 8:
                artWorkMeasurementsHeightList.append(mainString[0])
                artWorkMeasurementsWidthList.append(mainString[2])
                artWorkMeasurementUnitList.append(mainString[3])
            elif len(mainString) == 9:
                artWorkMeasurementsHeightList.append(mainString[0])
                artWorkMeasurementsWidthList.append(f"{mainString[2]} {mainString[3]}")
                artWorkMeasurementUnitList.append(mainString[4])
            elif len(mainString) == 10:
                artWorkMeasurementsHeightList.append(f"{mainString[0]} {mainString[1]}")
                artWorkMeasurementsWidthList.append(f"{mainString[3]} {mainString[4]}")
                artWorkMeasurementUnitList.append(mainString[5])
            elif len(mainString) == 12:
                artWorkMeasurementsHeightList.append(f"{mainString[2]} {mainString[3]}")
                artWorkMeasurementsWidthList.append(f"{mainString[5]} {mainString[6]}")
                artWorkMeasurementUnitList.append(mainString[7])
            else:
                artWorkMeasurementsHeightList.append("")
                artWorkMeasurementsWidthList.append("")
                artWorkMeasurementUnitList.append('')

        elif len(iList) == 2:
            mainString = iList[0].text.split(" ")
            if len(mainString) == 8:
                artWorkMeasurementsHeightList.append(mainString[0])
                artWorkMeasurementsWidthList.append(mainString[2])
                artWorkMeasurementUnitList.append(mainString[3])
            elif len(mainString) == 9:
                artWorkMeasurementsHeightList.append(mainString[0])
                artWorkMeasurementsWidthList.append(f"{mainString[2]} {mainString[3]}")
                artWorkMeasurementUnitList.append(mainString[4])
            elif len(mainString) == 10:
                artWorkMeasurementsHeightList.append(f"{mainString[0]} {mainString[1]}")
                artWorkMeasurementsWidthList.append(f"{mainString[3]} {mainString[4]}")
                artWorkMeasurementUnitList.append(mainString[5])
            elif len(mainString) == 12:
                artWorkMeasurementsHeightList.append(f"{mainString[2]} {mainString[3]}")
                artWorkMeasurementsWidthList.append(f"{mainString[5]} {mainString[6]}")
                artWorkMeasurementUnitList.append(mainString[7])
            else:
                artWorkMeasurementsHeightList.append("")
                artWorkMeasurementsWidthList.append("")
                artWorkMeasurementUnitList.append('')
        else:
            artWorkMeasurementsHeightList.append("")
            artWorkMeasurementsWidthList.append("")
            artWorkMeasurementUnitList.append('')
        artWorkDetailList = soup.find("div", {"class": "LotDesc"}).decode_contents().split("<br/>")
        artWorkName = artWorkDetailList[0].replace('<i>', '')
        artWorkName = artWorkName.replace('</i>', '')
        artWorkNameList.append(artWorkName)
        artWorkMarkingList.append(artWorkDetailList[1])
        if len(artWorkDetailList) == 5:
            artWorkMaterialsList.append(artWorkDetailList[2])
            sizeNotes = artWorkDetailList[3].replace('<i>', '')
            sizeNotes = sizeNotes.replace('</i>', '')
            artWorkMeasurementsNotesList.append(sizeNotes + artWorkDetailList[4])
        elif len(artWorkDetailList) == 4:
            artWorkMaterialsList.append('')
            sizeNotes = artWorkDetailList[2].replace('<i>', '')
            sizeNotes = sizeNotes.replace('</i>', '')
            artWorkMeasurementsNotesList.append(sizeNotes + artWorkDetailList[3])
        else:
            artWorkMaterialsList.append('')
            artWorkMeasurementsNotesList.append('')
    else:
        artistNameList.append('')
        artistNantionalityList.append('')
        artistBirthList.append('')
        artistDeathList.append('')
        artWorkNameList.append('')
        artWorkMaterialsList.append('')
        artWorkMarkingList.append('')
        artWorkMeasurementsHeightList.append('')
        artWorkMeasurementsWidthList.append('')
        artWorkMeasurementsNotesList.append('')
        artWorkMeasurementUnitList.append('')

    artWorkMeasurementsDepthList.append('')
    artWorkImage1List.append(response['pageProps']['lotData']['auctionLots'][0]['image']['url'])
    artWorkImage2List.append('')
    artWorkImage3List.append('')
    artWorkImage4List.append('')
    artWorkImage5List.append('')
    lotUrlList.append(
        f"{response['baseUrl']}/auctions/{response['pageProps']['auction']['iSaleNo']}/lot/{response['pageProps']['lotData']['auctionLots'][0]['lotId']}/")

mainCsvDict = {'auction_house_name': auctionHouseNameList,
               'auction_location': auctionLocationList,
               'auction_num': auctionNumberList,
               'auction_start_date': auctionStartDateList,
               'auction_end_date': auctionEndDateList,
               'auction_name': auctionNameList,
               'lot_num': lotNumList,
               'price_estimate_min': priceEstimateMinList,
               'price_estimate_max': priceEstimateMaxList,
               'price_sold': priceSoldList,
               'artist_name': artistNameList,
               'artist_birth': artistBirthList,
               'artist_death': artistDeathList,
               'artist_nationality': artistNantionalityList,
               'artwork_name': artWorkNameList,
               'artwork_materials': artWorkMaterialsList,
               'artwork_markings': artWorkMarkingList,
               'artwork_measurements_height': artWorkMeasurementsHeightList,
               'artwork_measurements_width': artWorkMeasurementsWidthList,
               'artwork_measurements_depth': artWorkMeasurementsDepthList,
               'artwork_size_notes': artWorkMeasurementsNotesList,
               'auction_measureunit': artWorkMeasurementUnitList,
               'artwork_images1': artWorkImage1List,
               'artwork_images2': artWorkImage2List,
               'artwork_images3': artWorkImage3List,
               'artwork_images4': artWorkImage4List,
               'artwork_images5': artWorkImage5List,
               'lot_origin_url': lotUrlList}

dataFrameData = pd.DataFrame(mainCsvDict)
dataFrameData.to_csv('Bonhams_28352.csv')
