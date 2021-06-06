class REGRUAPIResultsExtractor():

    def __init__(self, api_result):
        self.api_result = api_result

    # def get_domains():
    #    return self.api_result['answer']['domains']

    def subdomain_exists(self, domain, subdomain):
        if not 'answer' in self.api_result:
            return False
        if not 'domains' in self.api_result['answer']:
            return False
        for domain_info in self.api_result['answer']['domains']:
            if domain_info['dname'] != domain:
                continue
            if not 'rrs' in domain_info:
                continue
            for resource in domain_info['rrs']:
                if resource['subname'] == subdomain:
                    return True
        return False