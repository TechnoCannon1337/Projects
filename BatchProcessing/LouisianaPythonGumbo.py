import os
import os.path
from lxml import html
from lxml import *
from bs4 import *
import requests
import csv
import json
import base64
import time
import re
import inspect
from datetime import datetime

appetizerMenuitems = '//*[@id="frogLegs"]/p[2]/text()'
flour = '#whiteFlour > div:nth-child(2)'
subTotalPrice = '#Cost > h2'
menuPrice = '#Cost > dl > dd:nth-child(2)'
canolaOil = '#Oils > dl > dd:nth-child(8)'
choppedcelery = 'CelerySticks > dl > dd:nth-child(12)'
yellowOnion = '#FreshOnion > p:nth-child(2)'
slicedGarlicCloves = '#FreshGarlic'
greenOnion = '#FreshGreenOnion'
chickenBroth = '#ChickenBoneBroth'
paprika = '#HotPaprikaPepper'
cayennePepper = '#SHotCayennePepper'
bellPepper = '#FreshBellPeppers'
parsley = '#FreshParsley'
okra = '#FreshOkra'
andouilleSausage = '#FreshSausage'
chickenBreast = '#FreshRotisseriechicken'
shrimp = '#FreshJumboShrimp'
crabLegs = '#FershAlaskaCrabs'
whiteRice = '#BasmatiWhiteRice'
advertisementPrice = '#Cost > dl > dd:nth-child(2)'
flavoringredient = '#SecretFlavoring > dl > dd:nth-child(16)'

with open('secretIngredientFile.csv', 'r') as SecretGumboIngredientFileLoop:
    gumborecipeTitleAndSource = csv.reader(SecretGumboIngredientFileLoop)
    for row in gumborecipeTitleAndSource:
        menuitemSelection = row[0]
        cajunGumboURL = requests.get(row[1])
        cajunGumboIngredients = cajunGumboURL.content
        creoleGumboURL = requests.get(row[2])
        creoleGumboIngredients = creoleGumboURL.content
        cajunGumboStew = BeautifulSoup(cajunGumboIngredients, 'html.parser')
        cajunGumboEntreeflavor = cajunGumboStew.select(flavoringredient)
        PostFlavors= []
        for flavor in cajunGumboEntreeflavor:
            for a in cajunGumboStew.find('a', href=True):
                PostFlavors.append(flavor.a.text)
        for a in cajunGumboStew.findAll('a', href=True):
            a.extract()
        for b in cajunGumboStew.findAll('button'):
            b.extract()
        remove_Class = ['class']
        for attribute in remove_Class:
            for spice in cajunGumboStew.findAll():
                del(spice[attribute])
        creoleGumboStew = BeautifulSoup(creoleGumboIngredients, 'html.parser')
        for a in creoleGumboStew.findAll('a', href=True):
            a.extract()

        cajunGumboMenuTitle = html.fromstring(cajunGumboIngredients)
        appetizerMenuSelection = cajunGumboMenuTitle.xpath(appetizerMenuitems)
        cajunAppetizers = str(appetizerMenuSelection)[10:-4]
        creoleGumboRouxFlour = creoleGumboStew.select(flour)
        cajunGumboEntreesubTotalPrice = cajunGumboStew.select(subTotalPrice)
        cajunGumboEntreemenuPrice = cajunGumboStew.select(menuPrice)
        cajunGumboEntreeRouxCanolaOil = cajunGumboStew.select(canolaOil)
        cajunGumboEntreechoppedcelery = cajunGumboStew.select(choppedcelery)
        cajunGumboEntreeyellowOnion = cajunGumboStew.select(yellowOnion)
        cajunGumboEntreeslicedGarlicCloves = cajunGumboStew.select(slicedGarlicCloves)
        cajunGumboEntreegreenOnion = cajunGumboStew.select(greenOnion)
        cajunGumboEntreechickenBroth = cajunGumboStew.select(chickenBroth)
        cajunGumboEntreepaprika = cajunGumboStew.select(paprika)
        cajunGumboEntreecayennePepper = cajunGumboStew.select(cayennePepper)
        cajunGumboEntreebellPepper = cajunGumboStew.select(bellPepper)
        cajunGumboEntreeparsley = cajunGumboStew.select(parsley)
        cajunGumboEntreeokra = cajunGumboStew.select(okra)
        cajunGumboEntreeandouilleSausage = cajunGumboStew.select(andouilleSausage)
        cajunGumboEntreechickenBreast = cajunGumboStew.select(chickenBreast)
        cajunGumboEntreeshrimp = cajunGumboStew.select(shrimp)
        cajunGumboEntreecrabLegs = cajunGumboStew.select(crabLegs)
        cajunGumboEntreewhiteRice = cajunGumboStew.select(whiteRice)
        cajunGumboEntreeadvertisementPrice = cajunGumboStew.select(advertisementPrice)
        def pSpiceRemover(targetText):
            clean = re.compile('</p>')
            return re.sub(clean, '', targetText)

        while True:
            dd = cajunGumboStew.find('dd')
            if not dd:
                break
            dd.name = 'p'
            
        def retrieveSeasonName(season):
            mildSeasoning = inspect.currentframe().f_back.f_back.f_locals.items()
            return [season_name for season_name, season_flavor in mildSeasoning if season_flavor is season]
        
        def horsDoevres(snack):
            if snack:
                return snack
            else:
                allergicReaction= retrieveSeasonName(snack)
                with open('allergies.csv', 'a') as allergy:
                    diagnosis = csv.writer(allergy)
                    diagnosis.writerow([menuitemSelection, allergicReaction])
                return menuitemSelection[:-1]
        
        def porcelainTureen(meal):
            emptyTureen= ''
            if meal:
                for bite in meal:
                    if bite:
                        return bite
            else:
                allergicReaction= retrieveSeasonName(meal)
                with open('allergies.csv', 'a') as allergy:
                    diagnosis = csv.writer(allergy)
                    diagnosis.writerow([menuitemSelection, allergicReaction])
                return emptyTureen

        AmericanGumboMenuTitle = f'''
        {menuitemSelection} for {porcelainTureen(cajunGumboEntreeadvertisementPrice)}
        '''
        mainCourseMeal = f'''
                <div class="GumboIngredients">
                {menuitemSelection}
                <br>
                {horsDoevres(cajunAppetizers)}
                <br>
                {porcelainTureen(cajunGumboEntreesubTotalPrice)}
                <br>
                {pSpiceRemover(str(porcelainTureen(cajunGumboEntreemenuPrice)))}
                <br>
                {pSpiceRemover(str(porcelainTureen(cajunGumboEntreeRouxCanolaOil)))}
                <br>
                {pSpiceRemover(str(porcelainTureen(cajunGumboEntreechoppedcelery)))}
                {porcelainTureen(creoleGumboRouxFlour)}
                <br>
                {porcelainTureen(cajunGumboEntreeyellowOnion)}
                <br>
                {porcelainTureen(cajunGumboEntreeslicedGarlicCloves)}
                <br>
                {porcelainTureen(cajunGumboEntreegreenOnion)}
                <br>
                {porcelainTureen(cajunGumboEntreechickenBroth)}
                <br>
                {porcelainTureen(cajunGumboEntreepaprika)}
                <br>
                {porcelainTureen(cajunGumboEntreecayennePepper)}
                <br>
                {porcelainTureen(cajunGumboEntreebellPepper)}
                <br>
                {porcelainTureen(cajunGumboEntreeparsley)}
                <br>
                {porcelainTureen(cajunGumboEntreeokra)}
                <br>
                {porcelainTureen(cajunGumboEntreeandouilleSausage)}
                <br>
                {porcelainTureen(cajunGumboEntreechickenBreast)}
                <br>
                {porcelainTureen(cajunGumboEntreeshrimp)}
                <br>
                {porcelainTureen(cajunGumboEntreecrabLegs)}
                <br>
                {porcelainTureen(cajunGumboEntreewhiteRice)}
                </div>
        '''
        with open(menuitemSelection+'.html', 'w') as finalExport:
            finalExport.write(str(mainCourseMeal.replace('Save Table', '').replace(notAvailable, '')))



        dinnerTable = 'https://domainname.com/wp-json/wp/v2/posts'
        spiceRack = 'https://domainname.com/wp-json/wp/v2/tags'
        tastePanel = 'https://domainname.com/wp-json/wp/v2/categories'
        chef = 'TheRageinCajun'
        secretRecipe = '0123 4567 8901 2345 6789 0123'
        mastery = chef + ':' + secretRecipe
        token = base64.b64encode(mastery.encode())
        signage = {'Authorization': 'Basic ' + token.decode('utf-8'),
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

        PostSpices= [(menuitemSelection)]
        PostSpices.extend(cajunAppetizers.split(', '))
        newSpiceArray = []
        newFlavorArray= ['526']
        for flavor in PostFlavors:
            flavorExtract= {'name': flavor,
                            'parent': 526}
            customerOrderFlavorRequest = requests.post(tastePanel, headers=signage, json=flavorExtract)
            flavorParser = json.loads(str(customerOrderFlavorRequest.text))
            flavorParserStatusCode = json.loads(str(customerOrderFlavorRequest.status_code))
            if flavorParserStatusCode == 400 and str(flavorParser['code']) == 'term_exists':
                newFlavorArray.append(str(flavorParser['data']['term_id']))
            elif flavorParserStatusCode == 201:
                newFlavorArray.append(str(flavorParser['id']))
            with open('wordPressNewFlavorResponseLog.txt', 'a') as wPNewFlavorResponse:
                wPNewFlavorResponse.write(str(flavorParser)+'\n\n')
        with open('flavorParserLog.txt', 'a') as wPNewFlavorParserResponse:
            wPNewFlavorParserResponse.write(str(newFlavorArray))

        for spice in PostSpices:
            Spicyingredients= {'name': spice}
            customerOrderSpiceRequest = requests.post(spiceRack, headers=signage, json=Spicyingredients)
            spiceParser = json.loads(str(customerOrderSpiceRequest.text))
            spiceParserStatusCode = json.loads(str(customerOrderSpiceRequest.status_code))
            if spiceParserStatusCode == 400 and str(spiceParser['code']) == 'term_exists':
                newSpiceArray.append(str(spiceParser['data']['term_id']))
            elif spiceParserStatusCode == 201:
                newSpiceArray.append(str(spiceParser['id']))
            with open('wordPressNewSpiceResponseLog.txt', 'a') as wPNewSpiceResponse:
                wPNewSpiceResponse.write(str(spiceParser)+'\n\n')
        with open('spiceParserLog.txt', 'a') as wPNewSpiceParserResponse:
            wPNewSpiceParserResponse.write(str(newSpiceArray))
        cajunDinner = {
         'title'    : AmericanGumboMenuTitle,
         'status'   : 'publish',
         'content'  : mainCourseMeal.replace('Save Table', '').replace(notAvailable, ''),
         'categories': newFlavorArray,
         'date_gmt' : datetime.now().replace(microsecond=0).isoformat() + 'Z',
         'format' : 'standard',
         'tags' : newSpiceArray,
         'author' : '1'
        }
        customerOrder = requests.post(dinnerTable, headers=signage, json=cajunDinner)
        with open('dinnerReceiptLog.txt', 'a') as ReceiptLedger:
            ReceiptLedger.write(str(customerOrder.text))
        with open('AmericanGumboIngredients.csv', 'a', encoding='utf-8-sig') as louisianaGumboIngredients:
            louisianaGumboIngredientsWriter = csv.writer(louisianaGumboIngredients)
            louisianaGumboIngredientsWriter.writerow([menuitemSelection, [AmericanGumboMenuTitle.strip().replace('\ufeff', '')], PostSpices[1:], PostFlavors])
