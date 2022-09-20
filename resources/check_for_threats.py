class CheckForThreats:
    keyTup = ('processes', 'modules', 'folders', 'sectors', 'keys', 'datas', 'files', 'values')  # tuple used to denote the types of items in xmlcontent[3] position

    def __init__(self, xmlContent):
        self.checkListLength = []  # list used to determine if any threats were found by Malwarebytes
        self.xmlContent = xmlContent  # xml content gather from get_xml_data.py
        self.numberDict = {}  # used to find the item and number of threats found for that item in xmlcontent[3] position
        self.childDict = {}  # used to parse entries to only those with events and keys that matched keyTup

        # loop to update checkListLength -- needed to see if threats were found
        for child in xmlContent[5]:
            self.checkListLength.append(child)

        # loop to create the KV pair for item and number of threats found
        for child in xmlContent[3]:
            self.numberDict[child.tag] = child.text

    # parse the numberDict and update the childDict with only items that had threats and the number of those threats
    def findNumber(self):
        for key, value in self.numberDict.items():
            if key in CheckForThreats.keyTup and '0' < value <= '1':  # if item matches keyTup and 0 < val < 1 event
                self.childDict[key] = value

            if key in CheckForThreats.keyTup and value > '1':  # if item matches keyTup and val >= 2
                self.childDict[key] = value

    # find the threats and create loops to print all findings per item
    def findThreats(self):
        checkList = len(self.checkListLength)  # check to see the length of list is > 0, which means threats were found
        startPos = 0  # start position var for range
        if checkList > 0:  # if threats are found
            print("\n[!] THREATS DETECTED -- please review the below items...")
            for key, val in self.childDict.items():
                print(f'\n[-] {key.upper()} ({val}):')
                endPos = int(val) + startPos  # to find the correct 0-based position of the child items, this var was created for the endPos in range
                for x in range(startPos, endPos):  # iterate over range
                    startPos = endPos  # update the startPos with the last endPos
                    for child in self.xmlContent[5][x]:  # print data in the xmlcontent[5] position
                        print(f'    {child.text}')
        else:  # no threats were found
            print(f'\n[+] All items scanned successfully, no threats detected...')

    def run(self):  # run the methods
        self.findNumber()
        self.findThreats()
