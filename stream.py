from google.appengine.ext import ndb
from google.appengine.ext import db
from Queue import Queue
from  datetime import datetime

class Stream(ndb.Model):
	owner=ndb.UserProperty()
	view_time=Queue()
	tag=ndb.StringProperty(repeated=True)
	name=ndb.StringProperty()
	subscribers=ndb.StringProperty(repeated=True)
	createDate=ndb.DateTimeProperty(auto_now_add=True)
	dateOfLastPic=ndb.DateTimeProperty(auto_now_add=True)
	url=ndb.StringProperty()
	coverUrl=ndb.StringProperty()
	numOfPictures=ndb.IntegerProperty()
	view_count=ndb.IntegerProperty()
	@classmethod
	def get_myStreams(cls,user):
		return cls.query(cls.owner==user).order(-cls.dateOfLastPic).fetch()
	def update(time_now):
		for item in self.view_time.queue:
			if time_now-item>deltatime(hour=1):
				self.view_time.get()
			else:
				break
		self.view_count=self.view_time.qsize()


def getSubscribers(user):
	subStreams=[]
	streams=Stream.query().fetch()
	for stream in streams:
		if user.email() in stream.subscribers:
			subStreams.append(stream)
	return subStreams

class Image(db.Model):
	image_key=db.StringProperty()
	create_date=db.DateTimeProperty(auto_now_add=True)
	cap=db.StringProperty("connexus image")
	location=db.GeoPtProperty()


