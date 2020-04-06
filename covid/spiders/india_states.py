# -*- coding: utf-8 -*-
import scrapy


class IndiaStatesSpider(scrapy.Spider):
    name = 'india_states'
    allowed_domains = ['www.mohfw.gov.in']
    start_urls = ['http://www.mohfw.gov.in/']

    def parse(self, response):
        rows = response.xpath("//table[@class='table table-striped']/tbody/tr[position()<=30]")
        total_rows = response.xpath("//table[@class='table table-striped']/tbody/tr[position()=31]")
        for row in rows:
            states_no = row.xpath(".//td[1]/text()").get()
            states_name = row.xpath(".//td[2]/text()").get()
            total_confirmed_cases = row.xpath(".//td[3]/text()").get()
            cured_discharged_migrated = row.xpath(".//td[4]/text()").get()
            death = row.xpath(".//td[5]/text()").get()
            yield {
                'states_no': states_no,
                'states_name': states_name,
                'total_cases': total_confirmed_cases,
                'cured': cured_discharged_migrated,
                'death': death
            }

        for total in total_rows:
            total_india = total.xpath(".//td[1]/strong/span/text()").get()
            total_confirmed_cases_india = total.xpath(".//td[2]/strong/text()").get()
            total_cured_discharged_migrated = total.xpath(".//td[3]/strong/text()").get()
            total_death = total.xpath(".//td[4]/strong/text()").get()
            yield {
                'total_india': total_india,
                'total_cases': total_confirmed_cases_india,
                'total_cured': total_cured_discharged_migrated,
                'total_death': total_death
            }
