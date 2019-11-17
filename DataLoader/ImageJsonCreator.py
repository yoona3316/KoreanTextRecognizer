import json
import codecs
# Need refactoring for general usage
import os


class ImageJsonCreator:
    def __init__(self, path_kind="Fruits", pure_data_path="pure_data", data_list_path="data_list.json"):
        self.base_data_path = "../Data"
        self.path_kind = path_kind
        self.pure_data_path = pure_data_path
        self.data_list_path = data_list_path

    def create_json(self):
        pure_data_path = os.path.join(self.base_data_path, self.path_kind, self.pure_data_path)
        if os.path.exists(pure_data_path):
            f = codecs.open(pure_data_path, 'r', 'utf-8')
            dataList = dict()
        else:
            raise FileNotFoundError

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

        data_list_path = os.path.join(self.base_data_path, self.path_kind, self.data_list_path)
        if os.path.exists(data_list_path):
            with open(data_list_path, 'w', encoding='utf-8') as f:
                json.dump(dataList, f, indent='\t', ensure_ascii=False)
        else:
            raise FileNotFoundError

if __name__=='__main__':
    ImageJsonCreator("Fruits").create_json()