from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image, ImageFile
import os

def _add_thumb(path):
    parts = path.split('.');
    parts.insert(-1, 'thumb')
    return '.'.join(parts)


class photoAndthumbFieldFile(ImageFieldFile):
    def save(self, name, content, save=True):
        super(photoAndthumbFieldFile, self).save(name, content, save)
        self.thumb_path=_add_thumb(self.path)
        thumb_img = Image.open(self.path)
        thumb_img.thumbnail((self.field.thumb_width,self.field.thumb_height),Image.ANTIALIAS)
        thumb_img.save(self.thumb_path)

    def delete(self,save=True):
        super(photoAndthumbFieldFile, self).delete(save)
        thumb_path=_add_thumb(self.path)
        if(os.path.exists(thumb_path)):
            os.remove(thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)

    def _get_thumb_path(self):
        return _add_thumb(self.path)

    thumb_path=property(_get_thumb_path)
    thumb_url=property(_get_thumb_url)

class photoAndthumbField(ImageField):
    attr_class = photoAndthumbFieldFile

    def __init__(self, upload_to, verbose_name, thumb_width=128, thumb_height=128, *args, **kwargs):
        super(photoAndthumbField, self).__init__(upload_to=upload_to, verbose_name=verbose_name, *args, **kwargs)
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
