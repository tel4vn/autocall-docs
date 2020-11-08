**************************
OTP VOICE API 
**************************


Tạo Access Token Để Chạy OTP
============================

Thông Tin API
-----------------------

 ::

    POST  api/v1/users/generate_access_token
    Content-Type :  application/json 


Body Parameter
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
     - Code of response :200, 400, 404, ….
     - integer
   * - data
     - Main content of response 
     - object


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


Chạy OTP Voice
============================