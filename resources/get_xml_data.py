from defusedxml.ElementTree import parse


class GetXMLData:

    # parse and extract the XML
    @staticmethod
    def readFile(filePath):
        tree = parse(filePath)
        root = tree.getroot()
        return root
