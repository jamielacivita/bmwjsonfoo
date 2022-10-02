import xmltojson
import json
import xmltodict



def main():
    print("In Main.")

    with open("BMW5.html", "r", encoding="utf-8") as f:
        html = f.read()
        json_ = xmltojson.parse(html)
        #d = xmltodict.parse(html)
        #print(json_)
        x = json.loads(json_)
        print(x["html"]["body"]["ul"]["li"])
        print(type(x["html"]["body"]["ul"]["li"]))
        print(len(x["html"]["body"]["ul"]["li"]))
        print(type(x["html"]["body"]["ul"]["li"][0]))

        print(x["html"]["body"]["ul"]["li"][0])
        print(x["html"]["body"]["ul"]["li"][0]["a"].keys())
        print(x["html"]["body"]["ul"]["li"][0]["a"]["span"].keys())
        print(x["html"]["body"]["ul"]["li"][0]["a"]["span"]["#text"])

        #for n in range(0,5):
            #print(x["html"]["body"]["ul"]["li"][n]["a"]["span"]["#text"])











if __name__ == "__main__":
    main()