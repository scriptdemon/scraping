import gensim
from gensim import models
import logging
import csv
import json
import nltk

'''
infile = open("spam_data.json","r")
outfile = open("spam_data.csv","w")

writer = csv.writer(outfile)

for row in json.loads(infile.read()):
    writer.writerow(row)
'''

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

infile = open("reviews.txt","r")
data = json.load(infile)
print(data[0]['reviewText'])

#review_text=["Redmi Note 5 Pro 6Gb ram is very awesome. Front Cam 10/10 Back Cam 8/10 Battery 10/10 Performance 10/10 Look 10/10 Display 10/10 Face Lock 8/10 Finger Lock 10/10 Cost 10/10 Over all redmi note 5 Pro is awesome mobile under 20k","Best flagship phone under 20k Box includes: Phone, Data cable, Soft transparent back cover, wall power adapter and user manual. Pros: + Super smart phone+ Excellent build quality + Gorgeous display + Very good rear camera with DSLR grade bokeh, it is one of the best under 25K. + Sleek, sturdy and very premium + One of the best selfie in the market under 25K.+ No heat, no lagging.+ Dual band WiFi + Smooth performance from SD-636 coupled with 6GB RAM. + Great connectivity package - 4G, Dual SIM, FM Radio, WiFi+ Above average sunlight legibility.Cons:  - No Oreo out of the box.  - No NFC - Protruding camera lens","If you are looking for a powerful processor at this price.. You can highly consider this phone.. It has a nice built quality with a sturdy look.. Although I wll recommend to go for 4GB RAM version if u are not a too heavy user.. Because 3k more for just 2GB extra RAM is not worth it.. Camera quality is decent.. Not up to the mark as the hype was created.. But overall it's a great phone at this price.","I have to say this is the best sexy looking device that I have used ever. Xiaomi just nailed it. The main attraction of Redmi Note 5 Pro is the display with great in-hand-feel. Talking about the display its is bright(under sun) and gets dim as low as possible at night. Snapdragon 636 SOC is a very much battery efficient phone. A clean successor to Snapdragon 625SOC. I have upgraded from LENOVO P2 to Redmi Note 5 Pro last week. Except the battery the rest Redmi Note 5 Pro excels, battery LENOVO P2 is having that extra 1100mAh takes an edge. Camera is awesome in Redmi Note 5 Pro. I took Redmi Note 5 Pro 6GB version intentionally because for a future perspective its on the safer, more settling sideFew Positives that I found in Redmi Note 5 Pro +SD 636- low heating and stellar performance than SD625  +6GB RAM- the extra 2GB of RAM can hold upto 39 apps (including high end games) in memory +MiUi 9- feels light and very much responsive. +Battery- The 4000mAH battery is just outstanding when compared to many high end phones like OP5t+Camera- The bokeh and depth-of-feel are top notch. +Front flash- It is an added advantage to take selfies in No-Light scenarios.+Fingerprint- The fastest in the segment, can even beat speed against the higher priced flagships. +Video Recording- the Electronic Image Stabilisation(EIS) gives an outstanding video recording experience. +Weight- The phone feels light to hold on.  Negatives of Redmi Note 5 Pro -Only Fast Charge 2.0 available -no 4K recording -Face unlock is just a hit or a miss(it unlocks to all my family members) -6GB version when compared to 4GB is 3K Rupee more, which has no upgrade in ROM as well","Super delivery and super phone","Very good product","Undoubtedly the Best Smartphone that you could get under 15k. Pros: * Great display (9/10). * Awesome rear&front camera (9/10). * Battery backup is excellent (10/10). * Good build quality (8/10).* Brilliant performance (9/10).* Call quality is super clear (9/10).Cons:* Might have been even great if it runs on Android One.* Hybrid slot.* No 2x optical zoom. Overall it's a great smartphone under it's price segment. Go for it with no doubts. Flash sale is something that irritates a lot. I hope they won't be relying on flash sale in future. Seriously it causes more haters due to loss of patience. Flash sale must be eliminated since it's a cheap business trick that actually s*cks.","Bought 6 GB ram version. I was unable to get 4Gb version due to heavy rush among customers. But now I feel very good when got 6GB one. Because RAM means a lot. Price could be little lower. Phone is awesome. Nothing can be better at this price. It has almost everything which we need. Amazing display quality, amazing battery backup, quick charging takes almost 2hours to be fully charged. Lots of specific features are there. Camera of this phone killer one. What a perfection. Clear with bokeh effect with portrait mode for both rear and front. Nice build quality with firm grip on phone looks smartest. Thanks Xiaomi to provide a beautiful soft case. Latest Snapdragon 636 processor makes it fastest. Go for it without any thinking. Most of all thank you so much Flipkart for fastest delivery as always.","Superb mobile...... great value for money......on that price no company will give you there mobile.....camera is awesome.....only issue is charger is normal one not the fast charging...and that is not a deal breaker.....if any one want to buy ..You can buy blindly","Decent product Good, faster. Observed issue with VoLET SI<, I am using jio SIM. Observed that when network is not reachable, making the SIM down but not getting resumed automatically. I mean I have to so some flip/flop like going to plane mode and switching back to normal, make jio SIM operational.","Product per performance is very good for the value. However, there is very high radiation near the earpiece when taking calls. Have been asked by Mi showroom to request a replacement as they confirmed it has high radiation. Have sought a replacement and waiting to meet the technical specialist for it to be checked. Hope they do not do any drama to avoid replacement. All those who have ordered it please check if there is too much heat while taking calls near earpiece.","Build quality is good Camara's very poor quality, it doesn't meet my expectations.","The product is much hyped.But processor capability is restricted.It simply lags in asphalt 8 though using this 6GB variant .Specifically laggng is observed in Tokyo race when one repeatedly attempt to push neon race from right hand side touch.I am at high graphics and i must expect if its a power end device.","Old wine in new bottle... All features are average not as expected.. Battery charging bus taking too much time full charge approx 3½ hrs. Camera performance is good not as much as in others of 12 mp like Honor Selfie is very poor nothing changes in compare of note 4 series. Its 20 MP camera is not equivalent to 5 even of oppo or vivo. I think there is no LPDDR4 RAM, it is the same LPDDR4 RAM. Design of display is good but it is not bezelless . It's pettern of home and menus button is same it always appears on under the screen block the bottom area..","its been 9 days since i got this mobile. its been hanging from the day one itself. everyday atleast twice im rebooting the device. Right from the day its been launched i ve tried a lot to get this device. but im absolutely disappointed with the performance of this mobile. the only good thing is the battery. feeling humiliated.","I got defective unit becasue of that i had to go through multiple processes to get the new unit.","PROXIMITY SENSOR IS NOT WORKING. I CANT SEE THE DISPLAY WHILE CALLING UNTIL THE OTHER PERSON CUT THE CALL. AUTOMATICALLY MUTING THE VOICE. PHONE IS HEATING WHILE CHARGING. I TRIED THE TROUBLE SHOOT EXPLAINED BY THE FLIPKART CUSTOMER CARE AGENT. AGAIN THE SAME PROBLEM. THE FLIPKART CUSTOMER CARE IS NOT GIVING REFUND."]

all_reviews = []
prep = [
  "a",
  "abaft",
  "aboard",
  "about",
  "above",
  "absent",
  "across",
  "afore",
  "after",
  "against",
  "along",
  "alongside",
  "amid",
  "amidst",
  "among",
  "amongst",
  "an",
  "anenst",
  "apropos",
  "apud",
  "around",
  "as",
  "aside",
  "astride",
  "at",
  "athwart",
  "atop",
  "barring",
  "before",
  "behind",
  "below",
  "beneath",
  "beside",
  "besides",
  "between",
  "beyond",
  "but",
  "by",
  "circa",
  "concerning",
  "despite",
  "down",
  "during",
  "except",
  "excluding",
  "failing",
  "following",
  "for",
  "forenenst",
  "from",
  "given",
  "in",
  "including",
  "inside",
  "into",
  "lest",
  "like",
  "mid",
  "midst",
  "minus",
  "modulo",
  "near",
  "next",
  "notwithstanding",
  "of",
  "off",
  "on",
  "onto",
  "opposite",
  "out",
  "outside",
  "over",
  "pace",
  "past",
  "per",
  "plus",
  "pro",
  "qua",
  "regarding",
  "round",
  "sans",
  "save",
  "since",
  "than",
  "through",
  "throughout",
  "till",
  "times",
  "to",
  "toward",
  "towards",
  "under",
  "underneath",
  "unlike",
  "until",
  "unto",
  "up",
  "upon",
  "versus",
  "via",
  "vice",
  "with",
  "within",
  "without",
  "worth",
  "a",
    "an"
]

for i in data:
    #for j in i['reviews']:

    #for rev in i:
      list = i['reviewText'].lower().split('.')
      list = set(list)
      tru_list = list.copy()
      for k in tru_list:
          if k in prep:
              list.remove(k)
      all_reviews.append(list)

#tok_corp = [nltk.word_tokenize(sent.decode('utf-8')) for sent in all_reviews]

model = gensim.models.Word2Vec(all_reviews, min_count=5,size=200,sg=1,window=15)

#print(model['ram'])
#print(model.similarity('lens','camera'))
print(model.similarity('memory','ram'))
#print(all_reviews[0])

#sentences = word2vec.Text8Corpus('w2v_reviews')
#model = word2vec.Word2Vec(sentences, size = 20)



