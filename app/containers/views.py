from flask import Blueprint, render_template, session, redirect, url_for, current_app, flash
from werkzeug.wrappers import StreamOnlyMixin
from .. import db
from ..models import Container, Containertype, Status, Batch
from . import containers
from .forms import ContainerAddForm, VesselMoveContentsForm, VesselUpdateStatusForm, VesselFillForm

_label_base_url = "http://"+"192.168.1.101:5000"