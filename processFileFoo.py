import xmltojson


def getJson(filename="chunk.txt"):
    """
    Opens the (sanaztized) data file and converts the html within to .json.
    :param filename:
    :return: output file is data.json
    """
    with open(filename, "r", encoding="utf-8") as f:
        chunk = f.read()
    f.close()
    json_ = xmltojson.parse(chunk)

    #write json data to file.
    with open("data.json","w",encoding="utf-8") as f:
        f.write(json_)
    f.close()



def saveChunk(chunk,  filename = "chunk.txt"):
    """
    function to save the chunk text to its own file.
    :param chunk: the text to be saved.
    :param filename:
    :return: True if save successful.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(chunk)
    f.close()

    return True


def sanatizeChunk(filename="chunk.txt"):
    """
    :input: the filename of the data section pulled from the raw .html file.
    :return: that file sanatized (i.e. ready for the conversion to .json.
    """

    #remove the &ndash; if you don't it will break the xml to json conversion process.
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    f.close()

    cleanlines = []
    for l in lines:
        if "&ndash;" in l:
            l = l.replace("&ndash;","-")
            cleanlines.append(l)
        else:
            cleanlines.append(l)

    with open(filename, "w", encoding="utf-8") as f:
        lines = f.writelines(cleanlines)
    f.close()

    return True


def findDataStart(filename):
    """
    :param filename: the filename of the .html file.
    :return: the line number where the relevant (i.e. data) part of the .html file starts.
    """
    startData = 0
    with open(filename,"r", encoding="utf-8") as f:
        lines = f.readlines()
    f.close()
    for l in lines:
        if '<ul class="rows" id="search-results">' in l:
            startData = lines.index(l) - 1

    return startData


def findDataEnd(filename):
    """
    :param filename: the filename of the .html file.
    :return: the line number where the relevant (i.e. data) part of the .html file ends.
    """
    startData = findDataStart(filename)
    endData = 0

    with open(filename,"r", encoding="utf-8") as f:
        lines = f.readlines()
    f.close()

    lineNumber = 0
    for l in lines:
        if (lineNumber > startData) and "</ul>" in l:
            return lineNumber
        lineNumber = lineNumber + 1
    return 0


def extractChunk(filename):
    """
    :param filename: The raw .html file.
    :return: text of the the relevant data section copied from the .html file
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    f.close()

    startLine = findDataStart(filename) + 1
    endLine = findDataEnd(filename) + 1

    lineNumber = 0
    chunk = ""
    for l in lines:
        if (lineNumber >= startLine) and (lineNumber < endLine):
            chunk = chunk + l
        lineNumber = lineNumber + 1

    return chunk


def main():
    print("Process File Foo.")
    print("In Main.")


if __name__ == "__main__":
    main()
