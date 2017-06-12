import json

from django.http import HttpResponse
from django.forms.widgets import Select
from django.contrib.auth.decorators import login_required

from flexselect import (FlexSelectWidget, FlexSelectMultipleWidget,
                        choices_from_instance, instance_from_request)

import logging
logger = logging.getLogger(__name__)

import logging
logger = logging.getLogger(__name__)


@login_required
def field_changed(request):
    """
    Ajax callback called when a trigger field or base field has changed. Returns
    html for new options and details for the dependent field as json.
    """
    hashed_name = request.POST.get('hashed_name', None)
    include_options = request.POST.get('include_options', None)
    options = None

    if hashed_name is None:
        logger.warn("Param 'hashed_name' not provided")
    elif include_options is None:
        logger.warn("Param 'include_options' not provided")
    else:
        widget = None
        if hashed_name in FlexSelectWidget.instances:
            widget = FlexSelectWidget.instances[hashed_name]
        elif hashed_name in FlexSelectMultipleWidget.instances:
            widget = FlexSelectMultipleWidget.instances[hashed_name]
        else:
            logger.error("No widget for hashed_name: {}".format(hashed_name))

        if widget is not None:
            instance = instance_from_request(request, widget)
            choices = choices_from_instance(instance, widget)
            options = Select(choices=choices).render_options(choices, [])

    return HttpResponse(json.dumps({
        'options': options,
    }), content_type='application/json')
