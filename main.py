import time
from get_xml_data import GetXMLData
from compare_dates import CompareDates
from check_for_threats import CheckForThreats

if __name__ == '__main__':
    while True:
        try:
            filePath = input("[?] Please specify the path to the MBBR-STDOUT file or type 'EXIT' to quit >> ")  # prompt user for path
            if filePath == 'EXIT':  # exit program if requested
                print("[+] Closing program...")
                time.sleep(2)
                break
            elif '.XML' not in filePath:  # check that file path includes an XML file
                raise Exception
            else:
                getXmlData = GetXMLData()  # instantiate class object

                # print the dates for the databases
                compareDates = CompareDates(getXmlData.readFile(filePath))
                dbDates = compareDates.runDateCheck()
                print("\n---------------------------------------------------------------------------------")
                print("---------------------------------------------------------------------------------")
                for key, date in dbDates.items():

                    if date:
                        print(f'[-] The {key} is {date} days old, considering updating...')
                    else:
                        print(f'[+] The {key} is up to date...')

                # check to see if threats are present in output
                checkThreats = CheckForThreats(getXmlData.readFile(filePath))
                checkThreats.run()

                checkInput = input("[?] Would you like to check another file? [yes/EXIT] >> ")  # prompt user to continue
                if checkInput == 'yes':
                    continue
                elif checkInput == 'EXIT':
                    print("[+] Closing program...")
                    time.sleep(2)
                    break
                else:
                    print("[-] Input is unknown, please try again...")
                    time.sleep(2)
                    continue
        except:
            print("[-] Path provided did not include XML file, please retry...")
            time.sleep(2)
            continue
