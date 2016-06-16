from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
import uuid
import json

@csrf_exempt
def upload_image(req):
	result = {'error':1,'message':'Upload error!'}
	files = req.FILES.get('imgFile',None)
	if files:
		result = image_upload(files)

	return HttpResponse(json.dumps(result), content_type="application/json")

def image_upload(files):
	allow_suffix = ['jpg','png','jpeg','gif','bmp']
	file_suffix =  files.name.split('.')[-1]
	if file_suffix not in allow_suffix:
		return {'error':1,'message':'Bad Format!'}

	path = os.path.join(settings.MEDIA_ROOT,'uploads','content')

	if not os.path.exists(path):
		os.makedirs(path)

	file_name = str(uuid.uuid1()) + "." + file_suffix
	path_file = os.path.join(path,file_name)
	file_url = os.path.join("/uploads","content",file_name)
	open(path_file,'wb').write(files.file.read())
	return {'error':0,'url':file_url}