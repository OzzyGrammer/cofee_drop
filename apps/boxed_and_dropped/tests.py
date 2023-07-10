import dropbox

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

# from dropbox.files import WriteMode
from unittest.mock import patch

from .dropbox_manager import DropboxManager


class DropboxTest(TestCase):
    def test_dropbox_authentication(self):
        dbx = dropbox.Dropbox(settings.DROPBOX_OAUTH2_TOKEN)
        account = dbx.users_get_current_account()
        self.assertIsNotNone(account)


class DropboxUploadViewTest(TestCase):
    def setUp(self):
        self.file_path = "coffee-drop/apps/boxed_and_dropped/testimages/test.jpeg"
        dbx = dropbox.Dropbox(settings.DROPBOX_OAUTH2_TOKEN)
        account = dbx.users_get_current_account()
        self.assertIsNotNone(account)

        self.DM = DropboxManager(
            app_key=settings.DROPBOX_APP_KEY,
            app_secret=settings.DROPBOX_APP_SECRET,
            redirect_uri=settings.DROPBOX_REDIRECT_URI,
            csrf_token_session_key="your_csrf_token_session_key",
        )
        self.access_token = settings.DROPBOX_OAUTH2_TOKEN
        self.dbx = self.DM.get_dropbox_client(self.access_token)
        session = self.client.session
        session[self.DM.SESSION_KEY] = self.access_token
        session.save()
        dbx = self.DM.set_access_token_in_session(self.access_token, session)

    @patch.object(dropbox.Dropbox, "files_upload")
    def test_upload_view(self, mock_files_upload):
        url = reverse("upload_file")

        mock_file = self._create_mock_file()

        # Upload file via the view

        with open(self.file_path, "rb") as file:
            response = self.client.post(
                url,
                {
                    "file": file,
                },
            )

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # mock_files_upload.assert_called_once_with(
        #     b'mock file content',
        #     mode=WriteMode('overwrite', None)
        # )

    def _create_mock_file(self):
        from io import BytesIO

        return BytesIO(b"mock file content")
