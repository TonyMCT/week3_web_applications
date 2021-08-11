import os.path
import mimetypes

attachment_path = "bridge.jpg"
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

#with open(attachment_path, 'rb') as ap: 
 #   message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))