from flask import Flask, render_template, url_for, request, redirect, session
def redirect_url():
    return request.referrer or url_for("index")
