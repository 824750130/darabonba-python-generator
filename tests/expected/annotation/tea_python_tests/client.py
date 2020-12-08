# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.request import TeaRequest
from Tea.core import TeaCore
from Tea.exceptions import UnretryableException


class Client:
    """
    top annotation
    """
    _a = None  # type: str

    def __init__(self):
        """
        Init Func
        """
        pass

    def test_api(self):
        """
        testAPI
        """
        _runtime = {}
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
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                return
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    @staticmethod
    def test_func():
        """
        testFunc
        """
        pass


class AioClient(Client):
    """
    top annotation
    """
    _a = None  # type: str

    def __init__(self):
        """
        Init Func
        """
        pass

    async def test_api(self):
        """
        testAPI
        """
        _runtime = {}
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
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                return
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    @staticmethod
    async def test_func():
        """
        testFunc
        """
        pass
