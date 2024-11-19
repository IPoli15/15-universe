from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import check_password_hash
from config import Config
from models import db, Usuario
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError