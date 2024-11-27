# PhotographyWebsite using Python Fast API
Backend code developed with python's Fast API for ease of developement and use

Look as a code option above for clear structure to be seen
Website was intended for a camera studio client, with his customers to be able to send or upload him images to get them edited or to deliver hard copy, and owner of website shoiuld be able to post soem gallery of images in his website
 So, lets look at the Project Structure :
 photography_website/
├── main.py
├── templates/
│   ├── index.html
│   ├── gallery.html
│   ├── upload.html
│   ├── admin.html
│   └── login.html (if authentication is added)
├── static/
│   ├── css/
│   │   └── styles.css
│   └── images/
│       ├── user_uploads/
│       └── gallery/

i have added endpoints for uploading images, displaying the gallery, and an admin interface.
and a Separate directories for user-uploaded images and gallery images
