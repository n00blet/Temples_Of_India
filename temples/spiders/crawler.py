from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from temples.items import *
import wikipedia


# b = sel.xpath('//div[@id="mw-content-text"]/ul/li/a/@title').extract()
# c = sel.xpath('//div[@id="mw-content-text"]/ul/li/a/@href').extract()
# a = sel.xpath('//div[@id="mw-content-text"]/h2/span/text()').extract()


def complete_url(string):
	return "https://en.wikipedia.org" + string


class CrawlSpider(CrawlSpider):
	name='temples'
	allowed_domains = ['en.wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/List_of_Hindu_temples_in_India']

	def parse(self,response):
		sel = Selector(response)
		red_link = "redlink"
		temple_links = sel.xpath('//div[@id="mw-content-text"]/ul/li/a/@href').extract()
		for i in range(0,1018):
			if red_link not in temple_links[i]:
				yield Request(complete_url(temple_links[i]),callback=self.parse_each)


	def parse_each(self,response):
		
		temple_url = response.url
		#xpath wiki
		sel = Selector(response)
		content = sel.xpath("//div[@id='content']")
		temple_name = content.xpath("//h1/text()").extract()[0]
		temple_country = content.xpath("//table[contains(@class,'infobox')]/tr[contains(th,'Country')]/td/a/text()").extract()
		temple_state = content.xpath("//table[contains(@class,'infobox')]/tr[contains(th,'State')]/td/a/text()").extract()
		temple_district =content.xpath("//table[contains(@class,'infobox')]/tr[contains(th,'District')]/td/a/text()").extract()
		temple_locale = content.xpath("//table[contains(@class,'infobox')]/tr[contains(th,'Locale')]/td/a/text()").extract()
		try:
			temple_coordinates = content.xpath("//table[contains(@class,'infobox')]//span[@class='geo-dec']/text()").extract()[0].strip().replace(u'\xb0',u' ')
		except IndexError:
			temple_coordinates ="not available"
		temple_website = content.xpath("//table[contains(@class,'infobox')]/tr[contains(th,'Website')]/td/a/text()").extract()
		temple_arch_style = content.xpath("//table[contains(@class,'infobox')]/tr[contains(th,'Architectural styles')]/td/a/text()").extract()
		temple_imp_festivals = content.xpath("//table[contains(@class,'infobox')]/tr[contains(th,'Important festivals')]/td/a/text()").extract()
		temple_poets = content.xpath("//table[contains(@class,'infobox')]/tr[contains(th,'Poets')]/td/a/text()").extract()
		
		#wikipedia lib crawl
		wiki_lib = wikipedia.page(temple_name)
		temple_summary = wiki_lib.summary
		temple_images = wiki_lib.images
		
		#dump into list of item objects
		items = []
		item = TemplesItem()
		item['temple_url'] = temple_url
		item['temple_name'] = temple_name

		if not temple_country:
			item['temple_country'] = "not available"
		else:
			item['temple_country'] = temple_country[0]

		if not temple_state:
			item['temple_state'] = "not available"
		else:
			item['temple_state'] = temple_state[0]

		if not temple_district:
			item['temple_district'] = "not available"
		else:
			item['temple_district'] = temple_district[0]

		if not temple_locale:
			item['temple_locale'] = "not available"
		else:
			item['temple_locale'] = temple_locale[0]

		if not temple_coordinates:
			item['temple_coordinates'] = wiki_lib.coordinates
		else:
			item['temple_coordinates'] = temple_coordinates

		if not temple_summary:
			item['temple_summary'] = "not available"
		else:
			item['temple_summary'] = temple_summary

		if not temple_images:
			item['temple_images'] = "not available"
		else:
			item['temple_images'] = temple_images

		if not temple_website:
			item['temple_website'] = "not available"
		else:
			item['temple_website'] = temple_website[0]

		if not temple_arch_style:
			item['temple_arch_style'] = "not available"
		else:
			item['temple_arch_style'] = temple_arch_style

		if not temple_imp_festivals:
			item['temple_imp_festivals'] = "not available"
		else:
			item['temple_imp_festivals'] = temple_imp_festivals
		
		if not temple_poets:
			item['temple_poets'] = "not available"
		else:
			item['temple_poets'] = temple_poets
		items.append(item)

		return items






		