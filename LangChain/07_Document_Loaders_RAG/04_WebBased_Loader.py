# 04_WebBased_Loader.py

from langchain_community.document_loaders import WebBaseLoader

url = 'https://developer.mozilla.org/en-US/docs/Web/JavaScript'
# url = 'https://www.flipkart.com/samsung-80-cm-32-inch-hd-ready-led-smart-tizen-tv-voice-assistance-remote-control-digital-tuner-hdr-10-support-purcolor-knox-security-100-free-channels-object-tracking-sound-lite-adaptive-q-symphony/p/itmae4a41a34ff1d?pid=TVSHCTP5GGEXHXNJ&lid=LSTTVSHCTP5GGEXHXNJYRFLX6&marketplace=FLIPKART'


# we can also pass list of url form multiple user processing
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))


print("Page Content", docs[0].page_content)
print("Metadata", docs[0].metadata)



