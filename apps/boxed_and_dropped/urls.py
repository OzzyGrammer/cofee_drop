from django.urls import path
from .views import UploadFileView, DropboxAuthView, DropboxCallbackView

urlpatterns = [
    path("upload-file/", UploadFileView.as_view(), name="upload_file"),
    path("auth/", DropboxAuthView.as_view(), name="dropbox_auth"),
    path("auth/callback/", DropboxCallbackView.as_view(), name="dropbox_auth_callback"),
]
