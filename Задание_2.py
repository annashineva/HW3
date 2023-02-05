import requests


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, path_to_file, file_name):
        href = self._get_upload_link(path_to_file=path_to_file).get("href", "")
        with open('file_name', 'rb') as file:
            response = requests.put(href, file)
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")
                return


if __name__ == '__main__':
    path_to_file = '/Users/annasmolina/PycharmProjects/pythonProject/HW/HW3/Mscw.jpg'
    token = ''
    file_name = 'Mscw.jpg'
    uploader = YaUploader(token=token)
    result = uploader.upload_file_to_disk(path_to_file, file_name)



    # def upload_file(self, loadfile, savefile):
    #     savefile = self.get("https://cloud-api.yandex.net/v1/disk/resources", 'rb')
    #     loadfile = "HW/HW2 - открытие,чтение,запись файла/recipes.txt"
    #     response = requests.put(savefile, data=open(loadfile, 'rb'))
    #     response.raise_for_status()
    #     if response.status_code == 201:
    #         print("Success")
    #
    # if __name__ == '__main__':
    #     token = ''
    #     uploader = YaUploader(token)
    #     print(uploader)