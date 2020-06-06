import json

def compile_or(lst):
    o = ''
    for item in lst:
        o += item
        o += '/'
    return o[:-1]



class Helper:
    def __init__(self):
        self.content = {}
        self.load_content()

    def load_content(self):
        f = open('content.json')
        self.content = json.load(f)
        f.close()

    def solve(self, reactor, power):
        o = {"power": power, "reactor": reactor}
        data = self.content["power"][reactor]
        count_reactors = power / data["power"]
        o["count"] = count_reactors
        if "resources" in data:
            resources_per_second = count_reactors * (1 / data["resources-time"])
            o["resources"] = [data["resources"], resources_per_second]
        if "liquid" in data:
            liquid_per_second = count_reactors * data["liquid"][1]
            o["liquid"] = [data["liquid"][0], liquid_per_second]
        return o


class Languages:
    def __init__(self):
        self.languages = {}
        self.active_language = 'en'

    def load_language(self, language):
        f = open('languages/'+language+'.txt')
        self.languages[language] = dict()
        for line in f:
            line = line.strip()
            line_data = line.split(':')
            self.languages[language][line_data[0]] = line_data[1]
        f.close()

    def find(self, translate):
        key = ''
        for item in self.languages[self.active_language]:
            if self.languages[self.active_language][item] == translate:
                key = item
        return key

    def get(self, key):
        try:
            return self.languages[self.active_language][key]
        except KeyError:
            return key