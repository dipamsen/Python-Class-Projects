import dropbox


class FileUploader():
    def __init__(self, token):
        self.access_token = token

    def upload(self, source, destination):
        file = open(source, "rb")
        dbx = dropbox.Dropbox(self.access_token)
        dbx.files_upload(file.read(), destination)
        print("File uploaded succcessfully")


def main():
    token = "sl.Al1iGvC-sQGMWpWuz0G89xHuCrBWJhO3fJWWtMY6wYrPQ_QXfUQjUhCxVruPUcC2t49p7UjhG3FDx0QbqTpRku0YJm2Wdxa91Der729CAV9icUUEq2MGyMsou-Kn9rHa-UDcg9c"
    uploader = FileUploader(token)
    source = input("Enter Source file path ")
    destination = input("Enter Destination file path ")
    uploader.upload(source, destination)


main()
