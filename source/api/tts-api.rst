****************************
Text To Speech Autocall API
****************************


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

Import Text To Speech
============================

Thông Tin API
-----------------------

 ::

    POST  api/v1/campaigns/{{campainId}}/import_tts
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
   * - content
     - text which will be transformed to speech for campaign run. Key field of text must put between ``"{{"`` and ``"}}"``.  
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
   * - tts_id
     - Id of text
     - string

Example API
-----------------------


Example 1
+++++++++++++++++++++++

.. admonition:: Body Request Without Key Field 

  .. code-block:: json

    {
      "userid": "f461", 
      "content": "Chào mừng đến với giải pháp gọi tự động trên nền tảng tổng đài VoIP có sẳn của doanh nghiệp, thích hợp sử dụng quảng bá dịch vụ, thông báo cước, nhắc nợ, nhắc nhở tham gia sự kiện, thông báo lịch giao nhận hàng hóa."
    }

.. admonition:: Response  200 OK 

  .. code-block:: json

    {
        "message": "OK",
        "code": 200,
        "status": true,
        "data": {
            "campaign_id": "c78af",
            "tts_id": "rt56"
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

Example 2
+++++++++++++++++++++++

.. admonition:: Body Request With Key Field

  .. code-block:: json

    {
      "userid": "f461", 
      "content": "Kính chào quý khách {{khach_hang_name}}, cảm ơn quý khách đã sử dụng dịch vụ tổng đài nội bộ của VHT.  Dịch vụ của quý khách đến hạn thanh toán vào ngày {{ngay_thanh_toan}}. Quý khách vui long thanh toán trong hôm nay, hoặc chậm nhất là ngày mai với số tiền là {{tien_thanh_toan}}. Quý khách cần hỗ trợ thêm thông tin,  vui lòng liên hệ số điện thoại 1 8 0 0, 1 5 6 2. Xin cảm ơn quý khách."
    }

.. note::
  :class: admonition-note last admonition
 
  Key Field được đặt trong ``"{{"``  và  ``"}}"`` của đoạn text.  Ví dụ: ``{{khach_hang_name}}``
  
  Các Key Fields sẽ được thay thế bởi các giá trị tương ứng khi thực hiện autocall.  Các Key Fields được định nghĩa bởi người dùng. 

  Cấu trúc của Key Field::

  	Chứa các ký tự từ A đến Z, a đến z, 0-9, dấu gạch dưới '_'


.. admonition:: Response  200 OK 

  .. code-block:: json

    {
        "message": "OK",
        "code": 200,
        "status": true,
        "data": {
            "campaign_id": "c78af",
            "tts_id": "yu78"
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


Chạy Text To Speech Voice
============================

Thông Tin API
-----------------------

 ::

    POST  api/v1/campaigns/{{campainId}}/voicetts
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
   * - contacts
     - Object list contains set of phone numbers and set of value correspond to key fields
     - [object]
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
   * - key_field1
     - key field of text.  
     - string
     - Yes
     -
   * - key_field1
     - key field of text 
     - string
     - Yes
     -

.. note::
  :class: admonition-note last admonition

  user_id và access_token: thông tin nhận được từ API tạo access_token

  campaign_id: người dùng nhận từ web quản lý hoặc được nhận từ nhà cung cấp

  key_field: tương ứng với đoạn text import vào campaign người dùng định nghĩa. 

  Ví dụ::

  	key_field1 là 'khach_hang_name'
  	key_field1 là 'ngay_thanh_toan'. Nếu giá trị của key field là ngày tháng, yêu cầu format 'dd/mm/yyyy'
  	key_field1 là 'tien_thanh_toan' 


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
   * - results
     - Information of success calls and fail calls. Fail calls indicate the reason of failure such as *Wrong Format, Blacklist, Missing TTS Key* 
     - string

Example API
-----------------------

Example 1
+++++++++++++++++++++++

Với đoạn text người dùng import vào campaign: *"Chào mừng đến với giải pháp gọi tự động trên nền tảng tổng đài VoIP có sẳn của doanh nghiệp, thích hợp sử dụng quảng bá dịch vụ, thông báo cước, nhắc nợ, nhắc nhở tham gia sự kiện, thông báo lịch giao nhận hàng hóa."*  

Request để run autocall như sau: 


.. admonition:: Body Request 

	.. code-block:: json

		{
		  "userid": "f461", 
		  "contacts": [
			  {
			    "phone_number": "0771122330"
			  },
			  {
			    "phone_number": "0771122440"
			  }
		  ]
		}

.. admonition:: Response  200 OK 

	.. code-block:: json

		{
		    "message": "OK",
		    "code": 200,
		    "status": true,
		    "data": {
		        "campaign_id": "c78af",
		        "results": {
		        	"success_call": ["0771122330"],
		        	"fail_call": {
		        		"0771122440": "Blacklist"
		        	}
		        }
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

Example 2
+++++++++++++++++++++++

Với đoạn text người dùng import vào campaign: *"Kính chào quý khách {{khach_hang_name}}, cảm ơn quý khách đã sử dụng dịch vụ tổng đài nội bộ của VHT.  Dịch vụ của quý khách đến hạn thanh toán vào ngày {{ngay_thanh_toan}}. Quý khách vui long thanh toán trong hôm nay, hoặc chậm nhất là ngày mai với số tiền là {{tien_thanh_toan}}. Quý khách cần hỗ trợ thêm thông tin,  vui lòng liên hệ số điện thoại 1 8 0 0, 1 5 6 2. Xin cảm ơn quý khách.".*  

Request để run autocall như sau: 

.. admonition:: Body Request 

  .. code-block:: json

    {
      "userid": "f461", 
      "contacts": [
	      {
	        "phone_number": "0771122330",
	        "khach_hang_name": "Chị Ngọc Hiếu",
	        "ngay_thanh_toan": "10/09/2020",
	        "tien_thanh_toan": "1.000.000"
	      },
	      {
	        "phone_number": "0771122440",
	        "khach_hang_name": "Anh Quốc Ong",
	        "ngay_thanh_toan": "10/09/2020",
	        "tien_thanh_toan": "500.000"
	      }
	    ]
    }

.. admonition:: Response  200 OK 

  .. code-block:: json

    {
        "message": "OK",
        "code": 200,
        "status": true,
        "data": {
            "campaign_id": "c78af",
            "results": {
            	"success_call": ["0771122330"],
            	"fail_call": {
            		"0771122440": "Blacklist"
            	}
            }
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
