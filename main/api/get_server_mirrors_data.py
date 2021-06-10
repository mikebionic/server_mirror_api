from main.models import Mirror

def get_server_mirrors_data(name):
	data = []

	mirrors = Mirror.query.filter_by(MirrorAppName = name).all()

	for mirror in mirrors:
		if mirror.MirrorIsActive:
			mirror_data = mirror.to_json()
			url_prefix = mirror.MirrorUrlPrefix if mirror.MirrorUrlPrefix else ''
			domain = mirror.MirrorDomainName if mirror.MirrorDomainName else mirror.MirrorIp
			protocol = "https" if mirror.MirrorDomainName else "http"
			mirror_data["URL"] = f"{protocol}://{domain}{url_prefix}"
			data.append(mirror_data)

	return data