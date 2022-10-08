import getFileFoo
import processFileFoo
import parseJsonFoo



def main():
    """
    The main function for this program acts as the controller.
    :return: Nothing.
    """
    debug = False
    if (debug) : print("In Main - the controller function.")
    if (debug) : print("1. Get URL - for now returns a hardcoded URL.")
    URL = getFileFoo.fetchURL()

    getFileFoo.fetchHTML(URL)
    #input : URL
    #endstate : raw html file downloaded and saved.

    print("Determine if this is the last page of results.")
    print("fetch any additional pages")

    if (debug) : print("3. Process Data")
    #copy out just the relevant section from the downloaded html file.
    chunk = processFileFoo.extractChunk("temp_221007-052009.html")
    #save the relevant section as chunk.txt
    processFileFoo.saveChunk(chunk)
    #do some sanatizing on chunk.txt so it is ready to be parsed to .json.
    processFileFoo.sanatizeChunk()
    #convert the contents of chunk.txt into .json.
    processFileFoo.getJson()

    print("3. Parse JSON to get results object.")
    parseJsonFoo.parseData()

    print("Determine how many results have been returned.")
    resultsReturned = processFileFoo.getRangeTo()
    totalCount = processFileFoo.getTotalCount()



if __name__ == "__main__":
    main()

    print(processFileFoo.getRangeFrom())





