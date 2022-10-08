class Cycle:
    def __init__(self, rowNumber, postID, text, url, price, timestamp):
        self.rowNumber = rowNumber
        self.postID = postID
        self.text = text
        self.url = url
        self.price = price
        self.timestamp = timestamp

    def __str__(self):
        output = ""
        output = output + "Row number : " + str(self.rowNumber) + "\n"
        output = output + "PostID : " + self.postID + "\n"
        output = output + "Timestamp : " + self.timestamp + "\n"
        output = output + "Text : " + self.text + "\n"
        output = output + "Price : " + self.price + "\n"
        output = output + "url : " + self.url + "\n"

        return output


class Results:
    def __init__(self):
        self.rows = []

    def appendRow(self,cycle_object):
        self.rows.append(cycle_object)

    def __str__(self):
        print("number of rows : " + str(len(self.rows)))
        print()
        for n in range(0,len(self.rows)):
            print(self.rows[n])
        return ""









