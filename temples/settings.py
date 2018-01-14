# Scrapy settings for temples project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'temples'

SPIDER_MODULES = ['temples.spiders']
NEWSPIDER_MODULE = 'temples.spiders'
DOWNLOAD_DELAY = 5

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'temples (+http://www.yourdomain.com)'
