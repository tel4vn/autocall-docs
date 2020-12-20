**************************
OTP Voice Autocall API
**************************

Tạo Access Token 
============================

Thông Tin API
-----------------------

 ::

    POST  api/v1/users/generate_access_token
    Content-Type :  application/json 


Body Request
-----------------------
.. rst-class:: fullwidth

.. list-table:: 
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
     - Require
     - Default Value
   * - secret_key
     - Secret  key of user
     - string
     - Yes
     - 

.. note::
  :class: admonition-note last admonition
  
  secret_key : người dùng nhận từ web quản lý hoặc được nhận từ nhà cung cấp

Response
-----------------------

.. rst-class:: fullwidth

.. list-table::  
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
   * - code
     - status codes of response :200, 400, 404, ….
     - integer
   * - data
     - Main content of response 
     - object

.. rst-class:: fullwidth

.. list-table::  Data Object 
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
   * - id
     - Secret key of user
     - string
   * - user_id
     - Id of user 
     - string 
   * - access_token
     - Access Token which uses in the Authorization header to call API 
     - string 
   * - expire_at
     - the time when the access token will be expired  
     - integer
   * - scope
     - role of user : member or admin  
     - string

Example API
-----------------------

.. admonition:: Body Request 

  .. code-block:: json

    {
      "secret_key": "30511f666-f888-411b-a6e0-11111fb6gg7a"
    }

.. admonition:: Response  200 OK 

  .. code-block:: json

    {
        "message": "OK",
        "code": 200,
        "status": true,
        "data": {
            "id": "30511f666-f888-411b-a6e0-11111fb6gg7a",
            "user_id": "f461",
            "access_token": "1ebe8f88MzA1MTNkZjMtZjc3My00MTmY",
            "refresh_token": "",
            "expire_at": 15552000,
            "token_type": "Bearer",
            "scope": "member"
        }
    }

.. admonition:: Response Fail 

  .. code-block:: json 

    {
      "messsage":  "Bad Request"
      "code": 400, 
      "status": false,
      "data": {
        "error":  "detail of error"
      }
    }



Chạy OTP Voice
============================

Thông Tin API
-----------------------

 ::

    POST  api/v1/campaigns/{{campainId}}/voiceotp
    Content-Type :  application/json 
    Authorization:  {{access_token}}


Body Request
-----------------------

.. rst-class:: fullwidth

.. list-table:: 
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
     - Require
     - Default Value
   * - user_id
     - Id of user
     - string
     - Yes
     -
   * - callback_url
     - callback url 
     - string
     - No
     -
   * - contact
     - Object contains phone number and otp voice 
     - object
     - Yes
     -

.. rst-class:: fullwidth

.. list-table:: Contact Object 
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
     - Require
     - Default Value
   * - phone_number
     - Phone number of contact  
     - string
     - Yes
     - 
   * - otp
     - Voice OTP. OTP is numeric 
     - string
     - Yes
     -

.. note::
  :class: admonition-note last admonition

  user_id và access_token: thông tin nhận được từ API tạo access_token

  campaign_id: người dùng nhận từ web quản lý hoặc được nhận từ nhà cung cấp


Response
-----------------------

.. rst-class:: fullwidth

.. list-table::  
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
   * - code
     - status codes of response :200, 400, 404, ….
     - integer
   * - data
     - Main content of response 
     - object

.. rst-class:: fullwidth

.. list-table::  Data Object 
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
   * - campaign_id
     - Id of campaign 
     - string
   * - call_id
     - id of the call which will be used to get status of the call  
     - string

Example API
-----------------------

.. admonition:: Body Request 

  .. code-block:: json

    {
      "user_id": "f461",
      "callback_url": "https://example.com",
      "contact": 
      {
        "phone_number": "0771122330", 
        "otp": "123456"
      }
    }

.. admonition:: Response  200 OK 

  .. code-block:: json

    {
        "message": "OK",
        "code": 200,
        "status": true,
        "data": {
            "campaign_id": "c78af",
            "call_id": "88aa4744-d567-49fa-88b1-26e09da884a5"
        }
    }

.. admonition:: Response Fail 

  .. code-block:: json 

    {
      "messsage":  "Not Found"
      "code": 404, 
      "status": false,
      "data": {
        "error":  "detail of error"
      }
    }

Request To Callback Url 
============================

Hệ thống sẽ gọi tới callback url với format sau:

  ::
  
    POST  https://example.com
    Content-Type :  application/json


.. admonition:: Body Request 

  .. code-block:: json

    {
      "call_id": "88aa4744-d567-49fa-88b1-26e09da884a5",
      "campaign_id": "c78af",
      "duration": 11,
      "keypress": "123456",
      "phone_number": "0771122330",
      "start_time": "2020-11-10 23:23:11",
      "status": "Success",
      "user_id": "f461"
    }

.. rst-class:: fullwidth

.. list-table::  
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
   * - call_id
     - id of the call  
     - string
   * - campaign_id
     - Id of campaign 
     - string
   * - user_id
     - Id of user 
     - string
   * - duration
     - duration of the call  
     - integer
   * - phone_number
     - phone number of the callee  
     - string
   * - start_time
     - start time of the call   
     - string
   * - status
     - status of the call such as "Success" or "Fail"
     - string
   * - keypress
     - otp number
     - string

Trạng Thái Của Cuộc Gọi
============================

Thông Tin API
-----------------------

 ::

    GET  api/v1/report/{{call_id}}?user_id={{user_id}}
    Content-Type :  application/json 
    Authorization:  {{access_token}}

.. note::
  :class: admonition-note last admonition

  user_id và access_token: thông tin nhận được từ API tạo access_token

  call_id: thông tin người dùng nhận được từ cuộc gọi otp api 

Response
-----------------------

.. rst-class:: fullwidth

.. list-table::  
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
   * - code
     - status codes of response :200, 400, 404, ….
     - integer
   * - data
     - Main content of response 
     - object

.. rst-class:: fullwidth

.. list-table::  Data Object 
   :header-rows: 1   
   :class: styled-table
 
   * - Parameter
     - Description
     - Type
   * - call_id
     - id of the call  
     - string
   * - campaign_id
     - Id of campaign 
     - string
   * - user_id
     - Id of user 
     - string
   * - duration
     - duration of the call  
     - integer
   * - phone_number
     - phone number of the callee  
     - string
   * - start_time
     - start time of the call   
     - string
   * - status
     - status of the call such as "Success" or "Fail"
     - string
   * - keypress
     - otp number
     - string

Example API
-----------------------

.. admonition:: Response  200 OK 

  .. code-block:: json
  
    {
        "message": "OK",
        "code": 200,
        "status": true,
        "data": {
            "call_id": "88aa4744-d567-49fa-88b1-26e09da884a5",
            "campaign_id": "c78af",
            "duration": 11,
            "keypress": "123456",
            "phone_number": "0771122330",
            "start_time": "2020-11-10 23:23:11",
            "status": "Success",
            "user_id": "f461"
        }
    }

.. admonition:: Response Fail 

  .. code-block:: json 

    {
      "messsage":  "Not Found"
      "code": 404, 
      "status": false,
      "data": {
        "error":  "detail of error"
      }
    }

Status Codes
============================

Standard HTTP status codes ::

  200: OK 
  400: Bad Request 
  401: Unauthorized
  403: Forbidden
  404: Not Found 
  500: Service Error
