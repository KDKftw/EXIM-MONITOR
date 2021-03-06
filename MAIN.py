from VARIABLES import *
from FUNCTIONS import *


def test_SearchDetail():
    driver.get(URL)
    driver.maximize_window()
    try:
        lmZajezdNej = driver.find_element_by_xpath(
            "//*[@class='f_tourTable-tour-item f_tourTable-tour-item--destination']")
        wait.until(EC.visibility_of(lmZajezdNej))
        ##lmZajezdNej.click()
        driver.execute_script("arguments[0].click();", lmZajezdNej)  ####.click nefunguje na fischer NNN LM/FM, chrome
    except NoSuchElementException:
        url = driver.current_url
        msg = " Problem HP-Nej. nabidka - nenasel se LM zajezd " + url
        sendEmail(msg)


    time.sleep(3)

    try:
        hotelySingle = driver.find_element_by_xpath("//*[@id='divHotelCard']")
        hotelyAll = driver.find_elements_by_xpath("//*[@id='divHotelCard']")
        wait.until(EC.visibility_of(hotelySingle))
        if hotelySingle.is_displayed():
            for WebElement in hotelyAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass

                else:
                    url = driver.current_url
                    msg = " Problem s hotely v searchi - hotelCard " + url
                    sendEmail(msg)
    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s hotely v searchi - hotelCard " + url
        sendEmail(msg)


    try:
        fotkyAll = driver.find_elements_by_xpath("//*[@class='fshr-searchResults-thumbnail']")
        fotkaSingle = driver.find_element_by_xpath("//*[@class='fshr-searchResults-thumbnail']")
        wait.until(EC.visibility_of(fotkaSingle))
        if fotkaSingle.is_displayed():
            for WebElement in fotkyAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
                else:
                    url = driver.current_url
                    msg = " Problem s fotkami hotelu v searchi " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = " Problem s fotkami hotelu v searchi " + url
        sendEmail(msg)


    try:
        cenaAll = driver.find_elements_by_xpath("//*[@class='fshr-searchResult-item-summary']")
        cenaSingle = driver.find_element_by_xpath("//*[@class='fshr-searchResult-item-summary']")
        wait.until(EC.visibility_of(cenaSingle))
        if cenaSingle.is_displayed():
            for WebElement in cenaAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
                else:
                    url = driver.current_url
                    msg = " Problem s cenami hotelu v searchi " + url
                    sendEmail(msg)


    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s cenami hotelu v searchi " + url
        sendEmail(msg)


    try:
        detailHotelu = driver.find_element_by_xpath("//*[@class='fshr-bubble-wrapper']")
        wait.until(EC.visibility_of(detailHotelu))
        detailHotelu.click()


    except NoSuchElementException:
        url = driver.current_url
        msg = "Neprokliknuti na detail hotelu ze searche " +url
        sendEmail(msg)


    time.sleep(2.5)
    driver.switch_to.window(driver.window_handles[-1])

    try:
        detailFotka = driver.find_element_by_xpath("//*[@class='fshr-detailGallery']")
        wait.until(EC.visibility_of(detailFotka))
        if detailFotka.is_displayed():
            pass
    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s fotkami na detailu hotelu " +url
        sendEmail(msg)


    try:
        sedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary js-detailSummary']")
        wait.until(EC.visibility_of(sedivka))
        if sedivka.is_displayed():
            pass


    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem se sedivkou na detailu hotelu " + url
        sendEmail(msg)

    try:
        terminyCeny = driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
        wait.until(EC.visibility_of(terminyCeny))
        terminyCeny.click()
        potvrdit = driver.find_element_by_xpath(
            "//*[@class='fshr-button fshr-button--commonImportance fshr-button--big js-popupWindow--close']")
        driver.execute_script("arguments[0].click();", potvrdit)
    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem prepnuti na terminy a ceny na detailu hotelu " +url
        sendEmail(msg)

    try:
        terminySingle = driver.find_element_by_xpath("//*[@data-hotel]")
        wait.until(EC.visibility_of(terminySingle))

        if terminySingle.is_displayed():
            pass
        else:
            url = driver.current_url
            msg = "Problem s terminy a ceny na detailu hotelu " +url
            sendEmail(msg)


    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s terminy a ceny na detailu hotelu " +url
        sendEmail(msg)

    driver.quit()
##test searchdetail mus?? byt posledn?? - jako jediny ma driver.quit

def test_SDO():
        driver.get(URL_stat)
        try:
            destinaceAll = driver.find_elements_by_xpath("//*[@class='fshr-listTable-item']")
            destinaceSingle = driver.find_element_by_xpath("//*[@class='fshr-listTable-item']")
            if destinaceSingle.is_displayed():
                for WebElement in destinaceAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass

                    else:
                        url = driver.current_url
                        msg = "Nenasli se destinace v /stat " +url
                        sendEmail(msg)

        except NoSuchElementException:
            url = driver.current_url
            msg = "Nenasli se destinace v /stat " +url
            sendEmail(msg)


        try:
            dlazdiceFotoSingle = driver.find_element_by_xpath("//*[@class='f_tile-image-content']")
            dlazdiceFotoAll = driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
            if dlazdiceFotoSingle.is_displayed():
                for WebElement in dlazdiceFotoAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass

                    else:
                        url = driver.current_url
                        msg = "Nenasli se fotky v dlazdicich v /stat " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = driver.current_url
            msg = "Nenasli se fotky v dlazdicich v /stat " +url
            sendEmail(msg)


        try:
            mapa = driver.find_element_by_xpath("//*[@id='google-map']")
            if mapa.is_displayed():
                pass
            else:
                url = driver.current_url
                msg = "Nenasli se mapa v /stat " +url
                sendEmail(msg)

        except NoSuchElementException:
            url = driver.current_url
            msg = "Nenasli se mapa v /stat " +url
            sendEmail(msg)

def test_LM():
        driver.get(URL_lm)
        try:
            zajezdyLMsingle = driver.find_element_by_xpath("//*[@class='page-tour']")
            zajezdyLMall = driver.find_elements_by_xpath("//*[@class='page-tour']")
            wait.until(EC.visibility_of(zajezdyLMsingle))
            if zajezdyLMsingle.is_displayed():
                for WebElement in zajezdyLMall:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass

                    else:
                        url = driver.current_url
                        msg = "Problem s LM  zajezdy se neukazuji " + url
                        sendEmail(msg)


        except NoSuchElementException:
            url = driver.current_url
            msg = "Problem s LM  zajezdy se neukazuji " +url
            sendEmail(msg)
        try:
            rozbal = driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
            driver.execute_script("arguments[0].click();", rozbal)
            time.sleep(2)

        except NoSuchElementException:
            url = driver.current_url
            msg = " Nepodarilo se rozbalit LM zajezd " + url
            sendEmail(msg)

        try:
            rozbalenyZajezd = driver.find_element_by_xpath("//*[@class='page-tour-hotel-name']")
            rozbalenyZajezdAll = driver.find_elements_by_xpath("//*[@class='page-tour-hotel-name']")
            wait.until(EC.visibility_of(rozbalenyZajezd))
            if rozbalenyZajezd.is_displayed():
                for WebElement in rozbalenyZajezdAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass
        except NoSuchElementException:
            url = driver.current_url
            msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu v last minute " + url
            sendEmail(msg)

def test_HomePage():
        driver.get(URL)
        try:
            bannerSingle = driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            bannerAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(bannerSingle))
            if bannerSingle.is_displayed():
                for WebElement in bannerAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass
                    else:
                        url = driver.current_url
                        msg = "Problem na HP s bannery " + url
                        sendEmail(msg)


        except NoSuchElementException:
            url = driver.current_url
            msg = "Problem na HP s bannery " + url
            sendEmail(msg)



        time.sleep(1.5)

        try:
            nejnabidkyLMsingle = driver.find_element_by_xpath("//*[@class='f_tourTable-tour']")
            nejnabidkyLMall = driver.find_elements_by_xpath("//*[@class='f_tourTable-tour']")
            wait.until(EC.visibility_of(nejnabidkyLMsingle))
            if nejnabidkyLMsingle.is_displayed():
                for WebElement in nejnabidkyLMall:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass
                    else:
                        url = driver.current_url
                        msg = "Problem na HP s nej. nabidky LM " + url
                        sendEmail(msg)



        except NoSuchElementException:
            url = driver.current_url
            msg = "Problem na HP s nej. nabidky LM " + url
            sendEmail(msg)


        try:
            switchButton = driver.find_element_by_xpath("//*[@class='f_switch-button']")
            driver.execute_script("arguments[0].click();", switchButton)
            time.sleep(2.5)

        except NoSuchElementException:
            url = driver.current_url
            msg = "Problem s HP - switch button u nej. nabidky " + url
            sendEmail(msg)



        try:
            nejnabidkyFMsingle = driver.find_element_by_xpath("//*[@class='f_tourTable-tour']")
            nejnabidkyFMall = driver.find_elements_by_xpath("//*[@class='f_tourTable-tour']")
            wait.until(EC.visibility_of(nejnabidkyFMsingle))
            if nejnabidkyFMsingle.is_displayed():

                for WebElement in nejnabidkyFMall:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass
                    else:
                        url = driver.current_url
                        msg = "Problem na HP s nej. nabidky FM " + url
                        sendEmail(msg)


        except NoSuchElementException:
            url = driver.current_url
            msg = "Problem na HP s nej. nabidky FM " +url
            sendEmail(msg)



        time.sleep(1)

        try:
            topnabidkaSingle = driver.find_element_by_xpath("//*[@class='f_tile-image-content']")
            topnabidkaAll = driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
            wait.until(EC.visibility_of(topnabidkaSingle))
            if topnabidkaSingle.is_displayed():
                for WebElement in topnabidkaAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass
                    else:
                        url = driver.current_url
                        msg = "Problem na HP - top nabidka " +url
                        sendEmail(msg)


        except NoSuchElementException:
            url = driver.current_url
            msg = "Problem na HP - top nabidka " +url
            sendEmail(msg)

def test_FM():
        driver.get(URL_fm)
        time.sleep(1.5)
        try:
            zajezdyFMsingle = driver.find_element_by_xpath("//*[@class='page-tour']")
            zajezdyFMall = driver.find_elements_by_xpath("//*[@class='page-tour']")
            wait.until(EC.visibility_of(zajezdyFMsingle))
            if zajezdyFMsingle.is_displayed():
                for WebElement in zajezdyFMall:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass

                    else:
                        msg = "Problem s FM - zajezdy se neukazuji"
                        sendEmail(msg)


        except NoSuchElementException:
            msg = "Problem s FM - zajezdy se neukazuji"
            sendEmail(msg)


        try:
            rozbal = driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
            wait.until(EC.visibility_of(rozbal))
            driver.execute_script("arguments[0].click();", rozbal)
            time.sleep(2)

        except NoSuchElementException:
            msg = " Nepodarilo se rozbalit FM zajezd "
            sendEmail(msg)



        try:
            rozbalenyZajezd = driver.find_element_by_xpath("//*[@class='page-tour-hotel-name']")
            rozbalenyZajezdAll = driver.find_elements_by_xpath("//*[@class='page-tour-hotel-name']")
            wait.until(EC.visibility_of(rozbalenyZajezd))
            if rozbalenyZajezd.is_displayed():
                for WebElement in rozbalenyZajezdAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass

                    else:
                        msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu ve FM "
                        sendEmail(msg)


        except NoSuchElementException:
            msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu ve FM "
            sendEmail(msg)



test_HomePage()
test_SDO()
test_LM()
test_FM()
test_SearchDetail()