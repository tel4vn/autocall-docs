==========
Hướng dẫn người sử dụng
==========

Hướng dẫn sử dụng này bao gồm sử dụng giao diện web của user.

Một số tính năng UI web liên quan đến quản trị chỉ khả dụng cho 
người dùng có phân quyền là admin và đây là tài liệu trong :doc:`admin-guide`.


Đăng nhập
======================================

Truy cập vào trang web quản trị, sau đó nhập username và password đã được cung cấp, ấn Login

.. image:: /images/dang-nhap.PNG
:align: center


Tạo file âm thanh 
======================================

---------------
Convert file âm thanh tới WAV
---------------

**Bước 1**. Truy cập vào trang web sau: ``https://audio.online-convert.com/``

.. image:: /images/audioconvert/home.PNG
:align: center

**Bước 2**. Chọn Convert tới WAV

**Bước 3**.  Chọn "Choose Files" và chọn file cần convert

.. image:: /images/audioconvert/choosefile.PNG
:align: center

**Bước 4**. Chọn các options sau

.. image:: /images/audioconvert/convertoptions.PNG
:align: center

**Bước 5**. Ấn "Start conversion", sau đó đợi tải về.


---------------
Upload file âm thanh vào hệ thống autocall
---------------

Chọn upload file âm thanh vào hệ thống với một trong hai cách: 

#. Chọn vào biểu tượng trong menu Dashboard.

.. image:: /images/user/dashboard/voice.PNG
:align: center
 
Ấn "Browse", chọn file âm thanh WAV. Và sau đó chọn Submit để upload file ghi âm vào hệ thống.

.. image:: /images/user/voice/upload.PNG
:align: center

#. Chọn "Add A Voice" trong menu Voice. 

.. image:: /images/user/voice/home.PNG
:align: center

Ấn "Browse", chọn file âm thanh WAV. Và sau đó chọn Submit để upload file ghi âm vào hệ thống.

.. image:: /images/user/voice/upload.PNG
:align: center


Import danh sách Contact vào hệ thống 
======================================

.. note::

    Hệ thống chỉ cho phép định dạng import là CSV. 

---------------
Import danh sách Contact
---------------

**Bước 1**. Chọn "Add Contact" trong menu Contact:

.. image:: /images/user/contact/home.PNG
:align: center

**Bước 2**. Điền đầy đủ thông tin sau để import danh sách contact 

* *Input* -- Bạn có thể download file CSV mẫu và tạo file của chính bạn. 

* *Name* -- Tên danh sách mà bạn đang import.  

* *Choose CSV* -- Ấn "Browser", chọn file CSV cần import. 

* *Description* -- Mô tả thông tin của danh sách đang import.

.. image:: /images/user/contact/upload.PNG
:align: center

---------------
Mẫu File CSV Import
---------------

Format mẫu file CSV như sau:

.. csv-table:: Mẫu Contact CSV
   :file: /images/user/contact/contacts.csv
   :widths: 30, 70
   :header-rows: 1


Tạo campaign để chạy chiến dịch  
======================================

Tạo campaign với một trong hai cách: 

#. Chọn vào biểu tượng sau trong menu Dashboard.

.. image:: /images/user/dashboard/campaign.PNG
:align: center
 
#. Chọn "Add A Campaign" trong menu Campaign. 

.. image:: /images/user/campaign/home.PNG
:align: center


Điền đầy đủ thông tin sau để tạo chiến dịch mới:

* *Name* -- Tên chiến dịch.  

* *Voice* -- Chọn file âm thanh sẽ được phát trong chiến dịch. 

* *Contact List* -- Chọn danh sách contact cần chạy cho chiến dịch.

* *Submit* -- Nhấn Submit để hoàn thành tiến trình tạo chiến dịch. 

.. image:: /images/user/campaign/createcampaign.PNG
:align: center


Chạy campaign autocall  
======================================

**Bước 1**. Chọn menu Campaign:

.. image:: /images/user/campaign/menu.PNG
:align: center

**Bước 2**. Chọn chiện dịch trong danh sách và click vào icon run

.. image:: /images/user/campaign/runcampaign.PNG
:align: center

**Bước 3**. Chọn các options sau để chạy autocall 

---------------
Chạy chiến dịch 
---------------

* *Continue run* -- Chiến dịch chạy với danh sách contact đã được gán trước đó. 

.. image:: /images/user/campaign/runcampaignoption1.PNG
:align: center

---------------
Tái sử dụng chiến dịch 
---------------

* *Choose contact list* -- Chọn lại contact trong tập danh sách contact có sẵn để chạy chiến dịch.  

.. image:: /images/user/campaign/runcampaignoption2.PNG
:align: center

Chọn contact trong danh sách và Submit

.. image:: /images/user/campaign/runcampaignoption2contact.PNG
:align: center

Chiến dịch chạy với danh sách contact mới. 

* *Upload file* -- Import danh sách contact mới cho chiến dịch 

.. image:: /images/user/campaign/runcampaignoption3.PNG
:align: center

Ấn Browser để import contact và Submit

.. image:: /images/user/campaign/runcampaignoption3contact.PNG
:align: center

Chiến dịch chạy với danh sách contact mới. 



Report  
======================================

Tại menu Dashboard, chọn campaign để xem biểu đồ thống kê

.. image:: /images/user/dashboard/report01.PNG
:align: center

.. image:: /images/user/dashboard/report02.PNG
:align: center

Tại menu Report, chọn campaign để xem thống kê chi tiết

.. image:: /images/user/report.PNG
:align: center
