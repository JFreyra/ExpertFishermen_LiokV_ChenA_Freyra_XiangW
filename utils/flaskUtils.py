def redirect_url():
    return request.referrer or url_for("index")
