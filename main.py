import getFileFoo
import processFileFoo



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

    if (debug) : print("3. Process Data")
    #copy out just the relevant section from the downloaded html file.
    chunk = processFileFoo.extractChunk("temp_221007-052009.html")
    #save the relevant section as chunk.txt
    processFileFoo.saveChunk(chunk)
    #do some sanatizing on chunk.txt so it is ready to be parsed to .json.
    processFileFoo.sanatizeChunk()
    #convert the contents of chunk.txt into .json.
    processFileFoo.getJson()

    print("3. Display the data")




if __name__ == "__main__":
    main()