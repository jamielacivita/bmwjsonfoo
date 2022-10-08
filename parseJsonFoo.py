import json
import objResults

def buildDataDict():
    with open('data.json') as f:
        data_dict = json.load(f)
    f.close()

    return data_dict


def parseTitleText(rowNumber, data_dict):
    titleText = data_dict["ul"]["li"][rowNumber]["div"]["h3"]["a"]["#text"]
    return titleText


def parseID(rowNumber, data_dict):
    idText = data_dict["ul"]["li"][rowNumber]["div"]["h3"]["a"]["@id"]
    return idText


def parseHref(rowNumber, data_dict):
    hrefText = data_dict["ul"]["li"][rowNumber]["div"]["h3"]["a"]["@href"]
    return hrefText


def parseRow(rowNumber):
    data_dict = buildDataDict()
    title = parseTitleText(rowNumber,data_dict)
    id = parseID(rowNumber,data_dict)
    href = parseHref(rowNumber,data_dict)
    return (rowNumber, id, title, href)


def parseDataScratch():
    data_dict = buildDataDict()
    rootKey = data_dict.keys()
    print("Root Keys" + str(rootKey))
    print("level one keys")
    levelOneKeys = data_dict["ul"].keys()
    print(levelOneKeys)
    print("Level 2 D")
    leveltwoDKeys = data_dict["ul"]["li"]
    #print(type(leveltwoDKeys))

    k_dict = {}
    k_dict["listOfDictionaries"] = data_dict["ul"]["li"]
    k_dict["rows"] = data_dict["ul"]["li"]
    k_dict["rows0"] = data_dict["ul"]["li"][0]
    k_dict["rows1"] = data_dict["ul"]["li"][1]
    k_dict["rows2"] = data_dict["ul"]["li"][2]
    k_dict["rows0pid"] = data_dict["ul"]["li"][0]["@data-pid"]
    k_dict["rows1pid"] = data_dict["ul"]["li"][1]["@data-pid"]
    k_dict["rows2pid"] = data_dict["ul"]["li"][2]["@data-pid"]
    k_dict["rows0a"] = data_dict["ul"]["li"][0]["a"]
    k_dict["rows1a"] = data_dict["ul"]["li"][1]["a"]
    k_dict["rows0div"] = data_dict["ul"]["li"][0]["div"]
    k_dict["rows0div@class"] = data_dict["ul"]["li"][0]["div"]["@class"]
    k_dict["rows0divspan"] = data_dict["ul"]["li"][0]["div"]["span"]
    k_dict["rows0divtime"] = data_dict["ul"]["li"][0]["div"]["time"]
    k_dict["rows0divtime#text"] = data_dict["ul"]["li"][0]["div"]["time"]["#text"]
    k_dict["rows0divtime@class"] = data_dict["ul"]["li"][0]["div"]["time"]["@class"]
    k_dict["rows0divtime@datetime"] = data_dict["ul"]["li"][0]["div"]["time"]["@datetime"]

    k_dict["rows0divh3a"] = data_dict["ul"]["li"][0]["div"]["h3"]["a"]
    k_dict["rows0divh3a#text"] = data_dict["ul"]["li"][0]["div"]["h3"]["a"]["#text"]

    print(k_dict["rows0divtime@datetime"])

def parseData():
    ro = objResults.Results()

    for n in range(0,5):
        rd = parseRow(n)
        c = objResults.Cycle(rd[0], rd[1], rd[2], rd[3], "price", "timestamp")
        ro.appendRow(c)

    print(ro)
























def main():
    print("In main")




if __name__ == "__main__":
    main()
