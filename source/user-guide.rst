#######################
Hướng dẫn sử dụng
#######################


Hướng dẫn sử dụng này bao gồm sử dụng giao diện web của user.

************
1. Đăng Nhập
************


Truy cập vào trang web quản trị, sau đó nhập username và password đã được cung cấp, ấn Login

.. image:: /images/dang-nhap.PNG
   :align: center
   :width: 30%


********************
2. Tạo File Audio 
********************


2.1. Convert File WAV
----------------------------------


* **Bước 1**. Truy cập vào trang web sau `https://audio.online-convert.com/ <https://audio.online-convert.com/>`_ 

.. image:: /images/audioconvert/home.PNG
   :align: center
   :width: 60%

* **Bước 2**. Chọn Convert tới WAV

* **Bước 3**.  Chọn "Choose Files" và chọn file cần convert

.. image:: /images/audioconvert/choosefile.PNG
   :align: center
   :width: 60%

* **Bước 4**. Chọn các options sau

.. image:: /images/audioconvert/convertoptions.PNG
   :align: center
   :width: 30%

* **Bước 5**. Ấn "Start conversion", sau đó đợi tải về.


2.2. Upload File WAV
-----------------------------------------------


Chọn upload file âm thanh vào hệ thống với một trong hai cách: 

* **Cách 1**. Chọn vào biểu tượng trong menu Dashboard.

   .. image:: /images/user/dashboard/voice.PNG
      :align: center
      :width: 40%
 

   Ấn "Browse", chọn file âm thanh WAV. Và sau đó chọn Submit để upload file ghi âm vào hệ thống.

   .. image:: /images/user/voice/upload.PNG
      :align: center
      :width: 80%

* **Cách 2**. Chọn "Add A Voice" trong menu Voice. 

   .. image:: /images/user/voice/home.PNG
      :align: center
      :width: 80%

   Ấn "Browse", chọn file âm thanh WAV. Và sau đó chọn Submit để upload file ghi âm vào hệ thống.

   .. image:: /images/user/voice/upload.PNG
      :align: center
      :width: 80%


****************************************
3. Import Contact 
****************************************


.. note::

    Hệ thống chỉ cho phép định dạng import là CSV. 


3.1. Import Contact
-----------------------------


* **Bước 1**. Chọn "Add Contact" trong menu Contact:

.. image:: /images/user/contact/home.PNG
   :align: center
   :width: 80%

* **Bước 2**. Điền đầy đủ thông tin sau để import danh sách contact 

   * *Input* -- Bạn có thể download file CSV mẫu và tạo file của chính bạn. 

   * *Name* -- Tên danh sách mà bạn đang import.  

   * *Choose CSV* -- Ấn "Browser", chọn file CSV cần import. 

   * *Description* -- Mô tả thông tin của danh sách đang import.

.. image:: /images/user/contact/upload.PNG
   :align: center
   :width: 80%


3.2. Mẫu File CSV
------------------------

.. csv-table::  Mẫu Contact CSV (:download:`contacts.csv <images/user/contact/contacts.csv>`)
   :widths: 10
   :class: styled-table
   :align: center

   "762847950"
   "762847951"
   "762847952"
   "762847953"


**********************************
4. Tạo Campaign 
**********************************


Tạo campaign với một trong hai cách: 

* **Cách 1**. Chọn vào biểu tượng sau trong menu Dashboard.

.. image:: /images/user/dashboard/campaign.PNG
   :align: center
   :width: 30%
 
* **Cách 2**. Chọn "Add A Campaign" trong menu Campaign. 

.. image:: /images/user/campaign/home.PNG
   :align: center
   :width: 60%

Điền đầy đủ thông tin sau để tạo chiến dịch mới:

   * *Name* -- Tên chiến dịch.  

   * *Voice* -- Chọn file âm thanh sẽ được phát trong chiến dịch. 

   * *Contact List* -- Chọn danh sách contact cần chạy cho chiến dịch.

   * *Submit* -- Nhấn Submit để hoàn thành tiến trình tạo chiến dịch. 

.. image:: /images/user/campaign/createcampaign.PNG
   :align: center
   :width: 60%


*************************
5. Chạy Campaign
*************************


* **Bước 1**. Chọn menu Campaign:

.. image:: /images/user/campaign/menu.PNG
   :align: center
   :width: 20%

* **Bước 2**. Chọn chiện dịch trong danh sách và click vào icon run

.. image:: /images/user/campaign/runcampaign.PNG
   :align: center
   :width: 70%

* **Bước 3**. Chọn các options sau để chạy autocall 


   * *Continue run* -- Chiến dịch chạy với danh sách contact đã được gán trước đó. 

   .. image:: /images/user/campaign/runcampaignoption1.PNG
      :align: center
      :width: 30%


   * *Choose contact list* -- Chọn lại contact trong tập danh sách contact có sẵn để chạy chiến dịch.  

   .. image:: /images/user/campaign/runcampaignoption2.PNG
      :align: center
      :width: 30%


   Chọn contact trong danh sách và Submit. Chiến dịch chạy với danh sách mới.

   .. image:: /images/user/campaign/runcampaignoption2contact.PNG
      :align: center
      :width: 80%


   * *Upload file* -- Import danh sách contact mới cho chiến dịch 

   .. image:: /images/user/campaign/runcampaignoption3.PNG
      :align: center
      :width: 30%


   Ấn Browser để import contact và Submit. Chiến dịch chạy với danh sách mới

   .. image:: /images/user/campaign/runcampaignoption3contact.PNG
      :align: center
      :width: 80%


*********
6. Report  
*********


* Tại menu Dashboard, chọn campaign để xem biểu đồ thống kê

.. image:: /images/user/dashboard/report01.PNG
   :align: center
   :width: 60%

.. image:: /images/user/dashboard/report02.PNG
   :align: center
   :width: 60%

* Tại menu Report, chọn campaign để xem thống kê chi tiết

.. image:: /images/user/report.PNG
   :align: center
   :width: 60%
