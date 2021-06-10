from main import db

class Mirror(db.Model):
	__tablename__ = "tbl_me_mirror"
	MirrorId = db.Column("MirrorId",db.Integer,nullable=False,primary_key=True)
	MirrorName = db.Column("MirrorName",db.String(100),nullable=False)
	MirrorAppName = db.Column("MirrorAppName",db.String(500))
	MirrorIp = db.Column("MirrorIp",db.String(500))
	MirrorDomainName = db.Column("MirrorDomainName",db.String(500))
	MirrorUrl = db.Column("MirrorUrl",db.String(500))
	MirrorIsActive = db.Column("MirrorIsActive",db.Boolean,default=False)
	MirrorUrlPrefix = db.Column("MirrorUrlPrefix",db.String(100))

	def to_json(self):
		return {
			"MirrorId": self.MirrorId,
			"MirrorName": self.MirrorName,
			"MirrorAppName": self.MirrorAppName,
			"MirrorIp": self.MirrorIp,
			"MirrorDomainName": self.MirrorDomainName,
			"MirrorUrl": self.MirrorUrl,
			"MirrorIsActive": self.MirrorIsActive,
			"MirrorUrlPrefix": self.MirrorUrlPrefix,
		}