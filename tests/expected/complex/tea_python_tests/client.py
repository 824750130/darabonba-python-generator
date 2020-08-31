# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Source.source_client import SourceClient
from tea_python_tests import models as main_models
from Source import models as source_models
from Tea.request import TeaRequest
from Tea.exceptions import TeaException
from Tea.core import TeaCore
from Tea.response import TeaResponse
from Tea.exceptions import UnretryableException


class Client(SourceClient):
    def __init__(self, config, _configs=None):
        self._configs = _configs
        super(Client, self).__init__(config)
        self._configs[0] = config

    def complex_1(self, request, client):
        request.validate()
        _runtime = {
            "timeouted": "retry"
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                name = "complex"
                map_val = {
                    "test": "ok"
                }
                version = "/" + "2019-01-08" + "" + str(self._pathname) + ""
                module_model_map_val = {}
                module_map_val = {}
                model_map_val = {}
                sub_model_map_val = {}
                _request.protocol = self._protocol
                _request.port = 80
                _request.method = "GET"
                _request.pathname = "/" + str(self._pathname) + ""
                _request.query = SourceClient.query(TeaCore.merge({
                    "date": "2019"
                }, request.header,
                    map_val))
                _request.body = SourceClient.body()
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                if True and True:
                    return
                elif True or False:
                    return source_models.RuntimeObject(

                    )
                client.print(request.to_map(), "1")
                client.print_async(request.to_map(), "1")
                self.hello(request.to_map(), [
                    "1",
                    "2"
                ])
                self.hello(None, None)
                return main_models.RuntimeObject().from_map({})
                self.complex_3(None)
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def complex_2(self, request, str, val):
        request.validate()
        _request = TeaRequest()
        name = "complex"
        config = source_models.Config(

        )
        client = SourceClient(config)
        _request.protocol = "HTTP"
        _request.port = 80
        _request.method = "GET"
        _request.pathname = "/"
        _request.query = SourceClient.query({
            "date": "2019",
            "version": "2019-01-08",
            "protocol": _request.protocol
        })
        _request.body = SourceClient.body()
        _last_request = _request
        _response = TeaCore.do_action(_request)

    def complex_3(self, request):
        request.validate()
        _request = TeaRequest()
        name = "complex"
        _request.protocol = self.template_string()
        _request.port = 80
        _request.method = "GET"
        _request.pathname = "/"
        _request.query = SourceClient.query({
            "date": "2019"
        })
        _request.body = SourceClient.body()
        _request.headers["host"] = "hello"
        _last_request = _request
        _response = TeaCore.do_action(_request)
        resp = _response
        req = source_models.Request(
            accesskey=request.access_key,
            region=resp.status_message
        )
        self.array_0(request.to_map())
        req.accesskey = "accesskey"
        req.accesskey = request.access_key
        SourceClient.parse(main_models.ComplexRequest())
        SourceClient.array(request.to_map(), "1")
        SourceClient.async_func()
        return main_models.ComplexRequest().from_map(TeaCore.merge(_request.query))

    def hello(self, request, strs):
        return self.array_1()

    @staticmethod
    def print(reqeust, reqs, response, val):
        pass

    @staticmethod
    def array_0(req):
        temp = source_models.Config(

        )
        any_arr = [
            temp
        ]
        return {}

    @staticmethod
    def array_1():
        return [
            "1"
        ]

    def template_string(self):
        return "/" + str(self._protocol) + ""

    def empty_model(self):
        main_models.ComplexRequest()
        main_models.ComplexRequestHeader()
        status = ""
        try:
            status = "failed"
        except Exception as e:
            status = "catch exception"
        finally:
            status = "ok"

    @staticmethod
    def array_access():
        configs = [
            "a",
            "b",
            "c"
        ]
        config = configs[0]
        return config

    @staticmethod
    def array_access_2():
        data = {
            "configs": [
                "a",
                "b",
                "c"
            ]
        }
        config = data['configs'][0]
        return config

    @staticmethod
    def array_access_3(request):
        config_val = request.configs.value[0]
        return config_val

    @staticmethod
    def array_assign(config):
        configs = [
            "a",
            "b",
            "c"
        ]
        configs[3] = config
        return configs

    @staticmethod
    def array_assign_2(config):
        data = {
            "configs": [
                "a",
                "b",
                "c"
            ]
        }
        data['configs'][3] = config
        return data.get('configs')

    @staticmethod
    def array_assign_3(request, config):
        request.configs.value[0] = config

    @staticmethod
    def map_access(request):
        config_info = request.configs.extra.get('name')
        return config_info

    @staticmethod
    def map_access_2(request):
        config_info = request.configs.extra.get('name')
        return config_info

    @staticmethod
    def map_access_3():
        data = {
            "configs": {
                "value": "string"
            }
        }
        return data['configs'].get('value')

    @staticmethod
    def map_assign(request, name):
        request.configs.extra["name"] = name
