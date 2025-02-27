import requests
import json
import re
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36 OPR/63.0.3216.58473",
    "Accept": "application/json, text/plain, */*",
    "Alt-Used": "www.howtohackmoritzonlinefast.com"
}

class hackmoritz():
    """
    Hi NetFlix, bitte macht diese Challenges auch so dass keiner cheaten kann :)
    HackMoritz class, neues Game starten und Challenges solven.
    """
    apiPath = "https://www.howtohackmoritzonlinefast.com/api"
    gameID = json.loads(requests.post(f"{apiPath}/game/start", headers=headers).text)["game-id"] # Start a game, get its ID

    dataBeg = {
        "game-id": gameID,
    }

    dataCom = {
        "game-id": gameID,
        "first-name": "your",
        "last-name": "name",
        "age-agreement": "true",
        "country": "true",
        "email": "your@email.com",
        "answer": "drugflix",
        "terms-agreement": "true"
    }

    def dataRes(self, unix):
        """
        :param self: class variables
        :param unix: UNIX zeit
        :return: challenge result data
        """
        return {
            "game-id": self.gameID,
            "score": "10",
            "time": unix
        }

    def solve(self):
        """
        Alle challenges mit der API solven
        :param self: class variables
        """
        num = 1
        while num <= 4:
            # Begin Challenge
            begin = json.loads(requests.post(f"{self.apiPath}/game/challenge/{num}/begin", headers=headers, data=self.dataBeg).text)
            if begin["success"] != True:
                print(f"Couldn't start challenge N{num}!")
            else:
                print(f"Started Challenge N{num} ...")

            startTime = int(time.time()) # Get current UNIX time

            # Send Challenge result
            result = requests.post(f"{self.apiPath}/game/challenge/{num}/result", headers=headers, data=self.dataRes(startTime)).text
            if num == 4:
                resData = re.findall(r"{.+[:,].+}|\[.+[,:].+\]", result)[0] # Get JSON data
                result = json.loads(resData)
            else:
                result = json.loads(result)

            if result["success"] != True:
                print(f"Couldn't solve challenge N{num}!")
            else:
                print(f"Challenge N{num} solved!")
                if num == 4:
                    timer = result["total"]
                    print(f"All Challenges done in {timer}!")
            
            num += 1

        # Send form submition
        submit = json.loads(requests.post(f"{self.apiPath}/competition", headers=headers, data=self.dataCom).text)
        if submit["success"] != True:
            print(submit)
            print(f"Couldn't submit results!")
        else:
            print(f"Results submited!")


if '__main__' in __name__:
    # Ach und übrigens, das Challenge 3 Passwort: zimmer.CEO 
    # got from https://www.howtohackmoritzonlinefast.com/js/chunk-2d215cbf.ecc2243c.js ;)
    game = hackmoritz()
    game.solve()
