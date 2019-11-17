import json
import codecs
# Need refactoring for general usage


class ImageJsonCreator:
    def __init__(self, pure_data_path, json_path):
        self.pure_data_path = pure_data_path
        self.json_path = json_path

    def create_json(self):
        f = codecs.open(self.pure_data_path, 'r', 'utf-8')
        dataList = dict()

        id = 0
        while True:
            line = f.readline()
            if not line:
                break
            data = dict()
            line = line.strip('\n')
            data["name"] = line
            data['image'] = ""
            dataList[id] = data
            id += 1

        with open(self.json_path, 'w', encoding='utf-8') as f:
            json.dump(dataList, f, indent='\t', ensure_ascii=False)


pure_data_path = '../Data/pure_data'
json_path = '../Data/data_list.json'

if __name__=='__main__':
    ImageJsonCreator(pure_data_path, json_path).create_json()