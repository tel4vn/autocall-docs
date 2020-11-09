**************************
OTP Voice API
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
   * - userid
     - Id of user
     - string
     - Yes
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

  userid và access_token: thông tin nhận được từ API tạo access_token

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

Example API
-----------------------

.. admonition:: Body Request 

  .. code-block:: json

    {
      "userid": "f461", 
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
            "campaign_id": "c78af"
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

Standard HTTP status codes.

===== =====
Code  Name
===== =====
200   OK                 
400   Bad Request     
401   Unauthorized
403   Forbidden 
404   Not Found          
500   Service Error           
===== =====
