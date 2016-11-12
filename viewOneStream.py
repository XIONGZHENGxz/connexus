import jinja2
import os
import re
import urllib
import webapp2
import datetime
from stream import *
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import db,ndb,blobstore
from google.appengine.api import users,images

JINJA_ENV=jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class viewStreamPage(webapp2.RequestHandler):
	def get(self):
		upload_url=blobstore.create_upload_url('/uploadimage')
		stream_name=re.findall('%3D(.*)',self.request.url)[0]
		stream=Stream.query(Stream.name==stream_name).fetch()[0]
		if not stream.owner == users.get_current_user():
			time_now=datetime.datetime.now()
			stream.view_time.put(time_now)
			stream.update(time_now)
		stream.put()
		num_image=re.findall('numImageToShow=(.*)',self.request.url)
		if not num_image:
			images=db.GqlQuery("SELECT *FROM Image "+"WHERE ANCESTOR IS :1 "+"ORDER BY create_date DESC LIMIT 3", db.Key.from_path('Stream',stream_name))
		else:
			num=num_image[0]+3
			images=db.GqlQuery(" SELECT *FROM Image "+"WHERE ANCESTOR IS :1 "+"ORDER BY create_date DESC LIMIT "+num, db.Key.from_path('Stream',stream_name))
		showmore_url=urllib.urlencode({'showmore': stream_name+"%%"+users.get_current_user().nickname()})
		template_values={
		'stream': stream_name,
		'images': images,
		'upload_url': upload_url,
		'showmore_url': showmore_url,
		}
		template=JINJA_ENV.get_template('viewOneStream.html')
		self.response.write(template.render(template_values))
		
class uploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		referer_url=self.request.referer
		stream_name=re.findall('=(.*)',referer_url)[0]
		print referer_url
		stream=Stream.query(Stream.name==stream_name,Stream.owner==users.get_current_user()).fetch()[0]
		if stream.owner==users.get_current_user():
			uploads=self.get_uploads()
			for upload in uploads:
				image=Image(parent=db.Key.from_path('Stream',stream_name),image_key=str(upload.key()))
				stream.dateOfLastPic=image.create_date
				stream.put()
				image.put()
		else:
			self.response.out.write('<h2>Action not allowed!</h2>')
		self.redirect(referer_url)
		

class viewImageHandler(blobstore_handlers.BlobstoreDownloadHandler):
	def get(self,image_key):
		if not blobstore.get(image_key):
			self.error(404)
		else:
			self.send_blob(image_key)

		

app=webapp2.WSGIApplication([('/stream.*',viewStreamPage),('/view_image/([^/])?',viewImageHandler),
('/uploadimage',uploadHandler),('/showmore.*',viewStreamPage)],
debug=True)
