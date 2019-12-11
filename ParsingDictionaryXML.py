from xml.dom.minidom import parse
import urllib.request

#http://www.diveintopython.net/xml_processing/searching.html
def main():
    xml = urllib.request.urlopen("http://www.dictionaryapi.com/api/v1/references/collegiate/xml/thug?key=")
    xml_file = parse(xml)
    ref_list = xml_file.getElementsByTagName("dt")
    print(ref_list[0].toxml())

main()
