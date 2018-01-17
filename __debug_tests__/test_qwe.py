from tests.base_test import *
import os


class TestDocUpload(BaseTest):
    user = 'owner'

    def test_login(self):
        login(self.user)

    def test_go_to_tender(self):
        visit('http://40.69.95.23/#/tenderDetailes/50e4f97c5c5f45d9bd246c43290023db')
        Select(f('#docType')).select_by_index(1)
        f('#tend_doc_add').click()
        fc('input[type="file"]', [invisible]).send_keys(os.getcwd()+"\image.jpg")
        time.sleep(60)
        refresh()
