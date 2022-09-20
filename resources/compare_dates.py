from datetime import date, datetime


class CompareDates:

    def __init__(self, xmlContent):
        self.childDict = {}
        self.dateToday = str(date.today())

        # get the child fields from the XML data provided
        for child in xmlContent[1]:
            self.childDict[child.tag] = child.text

    # convert date to int
    @staticmethod
    def convertDateToInt(inputDate):
        intDate = datetime.strptime(inputDate, "%Y-%m-%d")
        return intDate

    # compare delta of dates
    @staticmethod
    def numOfDaysDifference(date1, date2):
        return (date1 - date2).days

    @staticmethod
    def convertChild(text):
        # replace characters in output for comparison
        replaceText = text.replace(".", "-", 2).replace("v", "")
        slicedText = replaceText[:-3]
        return slicedText

    # take the dates and determine if today's date is more current than database date
    def keyComparison(self, keyName):
        for key in self.childDict.keys():
            if key == keyName:
                # update the XML date format to align with datetime module format
                updatedDate = self.convertChild(self.childDict[keyName])
                # define time since malware db was updated
                if updatedDate < self.dateToday:
                    dateDiff = self.numOfDaysDifference(self.convertDateToInt(self.dateToday),
                                                        self.convertDateToInt(updatedDate))
                    return dateDiff
                else:
                    return

    # get malware DB date
    def malwareDB(self):
        checkMalwareDBDate = self.keyComparison('malware-database')
        return checkMalwareDBDate

    # get rootkit DB date
    def rootkitDB(self):
        checkRootkitDBDate = self.keyComparison('rootkit-database')
        return checkRootkitDBDate

    # return dates to main.py
    def runDateCheck(self):
        returnDBDict = {'malware-database': self.malwareDB(), 'rootkit-database' : self.rootkitDB()}
        return returnDBDict

