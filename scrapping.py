import scrapy

#C:\Users\berka\anaconda3

class homespider(scrapy.Spider):
    name= "home"

    urller=[]

    for i in range(1,29):
            url="https://www.hurriyetemlak.com/istanbul-satilik?counties=besiktas,sisli&p32=450000&p33=1&page={}".format(i)
            urller.append(url)

    start_urls=urller

    def parse(self,response):
        prices=response.css("div.upper.sibling div.top div.list-view-price::text").getall()
        rooms= response.css("div.middle.sibling div.right span.celly.houseRoomCount span span::text").getall()
        sqm=response.css("div.middle.sibling div.right span.celly.squareMeter.list-view-size span span::text").getall()
        ages=response.css("div.middle.sibling div.right span.celly.buildingAge span::text").getall()
        locs=response.css("div.bottom.sibling div.left div.down div.list-view-location span::text").getall()
        header=response.css("div.bottom.sibling div.left div.upper div.list-view-header span::text").getall()
        print(prices)
        print(rooms)
        print(sqm)
        print(ages)
        print(locs)

        pricesf=[]
        roomsf=[]
        sqmf=[]
        agesf=[]
        locsf=[]
        for i in prices:
            pricesf.append(i.strip("\n"))
        for k in rooms:
            roomsf.append(k.strip("\n"))
        for j in sqm:
            sqmf.append(j.strip("\n"))
        for m in ages:
            agesf.append(m.strip("\n"))
        x=0
        j=2
        locse=[]
        for n in locs:
            locse.append(n.strip("\n"))
        
        print(locse)

        while j < len(locse):
            locsf.append(locse[x:j])
            x+=2
            j+=2

        headerf=[]
        for g in header:
            headerf.append(g.strip("\n"))

       
        
        for i in range(len(prices)):
            print(i)
            yield {
                "Fiyat":pricesf[i],
                "Oda-Salon":roomsf[i],
                "Metrekare":sqmf[i],
                "Yaş":agesf[i],
                "Adres":locsf[i],
                "İlan Başlığı":headerf[i] 
            }

        
        
        
        
        
