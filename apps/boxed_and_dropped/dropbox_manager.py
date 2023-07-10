from dropbox import Dropbox, DropboxOAuth2Flow
from dropbox.exceptions import AuthError, ApiError, DropboxException
from dropbox.files import FileMetadata


class DropboxManager:
    """
    Manager for integrating with Dropbox API.
    """

    SESSION_KEY = "dropbox_access_token"

    def __init__(self, app_key, app_secret, redirect_uri, csrf_token_session_key):
        """
        Initialize the DropboxManager.

        Args:
            app_key (str): The Dropbox app key.
            app_secret (str): The Dropbox app secret.
            redirect_uri (str): The redirect URI for the Dropbox OAuth2 flow.
            csrf_token_session_key (str): The session key for storing the CSRF token.
        """
        self.app_key = app_key
        self.redirect_uri = redirect_uri
        self.app_secret = app_secret
        self.csrf_token_session_key = csrf_token_session_key

    def get_dropbox_client(self, access_token):
        """
        Create a Dropbox client instance using the provided access token.

        Args:
            access_token (str): The Dropbox access token.

        Returns:
            dropbox.Dropbox: The Dropbox client instance.
        """
        return Dropbox(access_token)

    def set_access_token_in_session(self, access_token, session):
        """
        Store the access token in the session.

        Args:
            access_token (str): The Dropbox access token.
            session (object): The session object to store the access token.
        """
        session[self.SESSION_KEY] = access_token

    def get_access_token_from_session(self, session):
        """
        Retrieve the access token from the session.

        Args:
            session (object): The session object containing the access token.

        Returns:
            str: The Dropbox access token, or None if not found.
        """
        return session.get(self.SESSION_KEY)

    def is_authenticated(self, session):
        """
        Check if the user is authenticated with Dropbox.

        Args:
            session (object): The session object containing the access token.

        Returns:
            bool: True if authenticated, False otherwise.
        """
        access_token = self.get_access_token_from_session(session)
        if access_token is None:
            return False

        dbx = self.get_dropbox_client(access_token)

        try:
            dbx.users_get_current_account()
            return True
        except AuthError:
            return False

    def upload_file(self, file, access_token):
        """
        Upload a file to Dropbox.

        Args:
            file (File): The file to upload.
            access_token (str): The Dropbox access token.

        Raises:
            Exception: If an error occurs during file upload.
        """
        try:
            dbx = self.get_dropbox_client(access_token)
            dbx.files_upload(file.read(), f"/{file.name}")
        except (ApiError, AuthError, DropboxException) as e:
            raise Exception("An error occurred during file upload.") from e

    def list_files(self, access_token):
        """
        List files in the user's Dropbox.

        Args:
            access_token (str): The Dropbox access token.

        Returns:
            list: A list of image URLs.

        Raises:
            Exception: If an error occurs while listing files.
        """
        dbx = self.get_dropbox_client(access_token)
        try:
            response = dbx.files_list_folder("")

            image_urls = []

            for entry in response.entries:
                if isinstance(entry, FileMetadata):
                    image_urls.append(
                        dbx.files_get_temporary_link(entry.path_lower).link
                    )

            return image_urls
        except (ApiError, AuthError, DropboxException) as e:
            raise Exception("An error occurred while listing files.") from e

    def start_auth_flow(self, session):
        """
        Start the Dropbox OAuth2 flow and return the authorization URL.

        Args:
            session (object): The session object to store the CSRF token.

        Returns:
            str: The authorization URL.
        """
        flow = DropboxOAuth2Flow(
            self.app_key,
            self.redirect_uri,
            csrf_token_session_key=self.csrf_token_session_key,
            consumer_secret=self.app_secret,
            session=session,
        )
        auth_url = flow.start()
        return auth_url

    def finish_auth_flow(self, request):
        """
        Finish the Dropbox OAuth2 flow and retrieve the access token.

        Args:
            request (object): The request object containing the query parameters.

        Returns:
            str: The Dropbox access token, or None if the flow could not be completed.
        """
        flow = DropboxOAuth2Flow(
            self.app_key,
            self.redirect_uri,
            csrf_token_session_key=self.csrf_token_session_key,
            consumer_secret=self.app_secret,
            session=request.session,
        )

        try:
            oauth_result = flow.finish(request.GET)
            return oauth_result.access_token
        except Exception:
            return None
