from dropbox.exceptions import AuthError
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views import View
from .dropbox_manager import DropboxManager


class UploadFileView(View):
    """
    View for uploading a file to Dropbox.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dropbox_manager = DropboxManager(
            settings.DROPBOX_APP_KEY,
            settings.DROPBOX_APP_SECRET,
            settings.DROPBOX_REDIRECT_URI,
            "dropbox-auth-csrf-token",
        )

    def post(self, request):
        """
        Handle the POST request for file upload.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            JsonResponse: JSON response indicating success or error.
        """
        file = request.FILES.get("file")

        if file:
            if not self.dropbox_manager.is_authenticated(request.session):
                return redirect("dropbox_auth")

            access_token = self.dropbox_manager.get_access_token_from_session(
                request.session
            )

            try:
                self.dropbox_manager.upload_file(file, access_token)
                return JsonResponse({"success": "File uploaded successfully"})
            except Exception as e:
                return JsonResponse({"error": str(e)})
        else:
            return JsonResponse({"error": "No file specified"})

    def get(self, request):
        """
        Handle the GET request for displaying the upload form.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered upload form HTML.
        """
        if not self.dropbox_manager.is_authenticated(request.session):
            return redirect("dropbox_auth")

        access_token = self.dropbox_manager.get_access_token_from_session(
            request.session
        )
        file_urls = self.dropbox_manager.list_files(access_token)

        return render(request, "upload_form.html", {"image_urls": file_urls})


class DropboxAuthView(View):
    """
    View for initiating the Dropbox authentication flow.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dropbox_manager = DropboxManager(
            settings.DROPBOX_APP_KEY,
            settings.DROPBOX_APP_SECRET,
            settings.DROPBOX_REDIRECT_URI,
            "dropbox-auth-csrf-token",
        )

    def get(self, request):
        """
        Handle the GET request for initiating the authentication flow.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Redirect response to the Dropbox authorization URL.
        """
        auth_url = self.dropbox_manager.start_auth_flow(request.session)
        return redirect(auth_url)


class DropboxCallbackView(View):
    """
    View for handling the Dropbox OAuth callback.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dropbox_manager = DropboxManager(
            settings.DROPBOX_APP_KEY,
            settings.DROPBOX_APP_SECRET,
            settings.DROPBOX_REDIRECT_URI,
            "dropbox-auth-csrf-token",
        )

    def get(self, request):
        """
        Handle the GET request for the Dropbox OAuth callback.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Redirect response to the upload file view or error view.
        """
        if "code" in request.GET:
            access_token = self.dropbox_manager.finish_auth_flow(request)
            if access_token is None:
                return redirect("error")

            self.dropbox_manager.set_access_token_in_session(
                access_token, request.session
            )
            return redirect("upload_file")

        return HttpResponse()
