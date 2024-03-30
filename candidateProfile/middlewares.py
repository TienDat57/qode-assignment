import logging as log
from candidateProfile.proxy import PROXIES
from candidateProfile.agents import AGENTS

import random

class CustomHttpProxyMiddleware(object):
    def process_request(self, request, spider):
        if self.use_proxy(request):
            p = random.choice(PROXIES)
            try:
                request.meta['proxy'] = "http://%s" % p['ip_port']
            except Exception as e:
                log.critical("Exception %s" % e)
                
    
    def use_proxy(self, request):
        if "depth" in request.meta and int(request.meta['depth']) <= 2:
            return False
        i = random.randint(1, 10)
        return i <= 2
    
    
"""
change request header nealy every time
"""
class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent
