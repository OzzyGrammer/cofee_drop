# Dropbox Integration App(Boxed and dropped)

> The Dropbox Integration App is a web application that allows users to upload files to their Dropbox account and view the uploaded files. It provides seamless integration with Dropbox's API to securely handle file storage and retrieval.



### How to Use the App

To use the app, follow these steps:
>1. In the [settings.py](../../project/settings.py)you will need to enter  your dropbox secrets which you will can retrieve by follwing this [guide]("https://developers.dropbox.com/oauth-guide")

>2. Visit the application [URL]("http://localhost:8000/dropbox/upload-file/"). If not signed in to dropbox you will be redirected to reate an account or log in if you already have one.

>3. Once logged in, you will see the file upload form.

>4. Select a file from your local system using the "Choose File" button. You want to see thumbnails I'd suggest you chooose pictures

>5. Click the "Upload" button to upload the selected file to your Dropbox account.

>6. After successful upload, you can view the list of uploaded files



### Assumptions and Constraints

>- The dropbox app needs to have the appropriate permissions for the API to work

>- Users are required to have a Dropbox account to use this application.

>- Users need to authorize the application to access their Dropbox account during the authentication flow.

>- The application currently supports uploading and viewing files only. Other Dropbox features like folder management, file sharing, etc., are not implemented.

>- File size limitations imposed by Dropbox's API apply (e.g., maximum file size of 150MB for the /files/upload endpoint).

>- The application assumes a single-user environment and does not provide multi-user access control.




### Future Features

> - If this Dropbox integration app were a real product, here are some hypothetical future features that could be considered for further development:

> - Multiple Dropbox Account Support: Allow users to connect and manage multiple Dropbox accounts within the app. This would provide flexibility for users who use multiple Dropbox accounts for different purposes.


> - Enhanced Security and Encryption: Implement additional security measures such as two-factor authentication, client-side encryption, and secure transmission protocols to enhance the protection of user data and ensure the privacy and security of files stored in Dropbox.
> - The ability to download files

