from scrapy.spider import Spider
from scrapy.selector import Selector
from math241.items import Website
from scrapy.contrib.spiders import Rule
import re

class MathSpider(Spider):
    name = "math"
    allowed_domains = ["math.uiuc.edu"]
    login_page = 'http://www.math.uiuc.edu/~schenck/M241S15_files/schedule2.html'
    start_urls = [
    "http://www.math.uiuc.edu/~schenck/M241S15_files/schedule2.html"
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=r'-\w+.html$'),
             callback='parse_item', follow=True),
    )

    def init_request(self):
        """This function is called before crawling starts."""
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        """Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'name': 'herman', 'password': 'password'},
                    callback=self.check_login_response)

    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        if "Hi Herman" in response.body:
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            self.initialized()
        else:
            self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.


    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//dl[@class="week"]/dd')
        items = []
# /html/body/dl[1]/dd[2]/text()[4]
        for site in sites:
            item = Website()
            #item['name'] = site.xpath('text()').re(re.compile('\w+', re.UNICODE))
            item['name'] = site.xpath('text()').extract()
            items.append(item)

        return items
