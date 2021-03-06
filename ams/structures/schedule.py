#!/usr/bin/env python
# coding: utf-8

from ams.structures import get_base_class, Targets, Period, Route

schedule_template = {
    "id": "uuid",
    "event": "default",
    "period": Period.get_template(),
    "route": Route.get_template(),
    "targets": Targets.get_template(),
}

schedule_schema = {
    "id": {
        "type": "string",
        "required": True,
        "nullable": False,
    },
    "event": {
        "type": "string",
        "required": True,
        "nullable": True,
    },
    "period": {
        "type": "dict",
        "schema": Period.get_schema(),
        "required": False,
        "nullable": True,
    },
    "route": {
        "type": "dict",
        "schema": Route.get_schema(),
        "required": False,
        "nullable": True,
    },
    "targets": Targets.get_schema(),
}


class Schedule(get_base_class(schedule_template, schedule_schema)):
    pass


schedules_template = [Schedule.get_template()]

schedules_schema = {
    "type": "list",
    "valueschema": {
        "schema": Schedule.get_schema(),
        "required": True,
        "nullable": False,
    },
    "nullable": True,
    "minlength": 1
}


class Schedules(get_base_class(schedules_template, schedules_schema)):
    pass
