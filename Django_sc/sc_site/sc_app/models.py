from django.db import models
from django.db import connection
# # モデル読込
# from django.db import model

# # モデルクラスを作成
# class People(models.Model):
# 	# 項目定義
#     Name     = models.CharField(max_length=100)           # 文字列
#     Tell     = models.IntegerField(blank=True, null=True) # 整数
#     Mail     = models.EmailField(max_length=100)          # Email
#     Birthday = models.DateField()                         # 日付
#     Website  = models.URLField()                          # URL
#     FreeText = models.TextField()                         # フリーテキスト

#     # テキスト表示
#     def __str__(self):
#     	return self.name

class Sample(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    
class mst_business(models.Model):
    business_code = models.CharField(max_length=4,primary_key=True,blank=False)
    business_name = models.CharField(max_length=40,blank=False)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False)
    
class mst_customer_headers(models.Model):
    customer_code = models.CharField(max_length=6,blank=False,primary_key=True)
    business_code = models.CharField(max_length=4,blank=False)
    customer_name = models.CharField(max_length=50,blank=False)
    zip_code = models.IntegerField(blank=True,null=True)
    address_1 = models.CharField(max_length=10,blank=True,null=True)
    address_2 = models.CharField(max_length=30,blank=True,null=True)
    address_3 = models.CharField(max_length=30,blank=True,null=True)
    address_4 = models.CharField(max_length=20,blank=True,null=True)
    address_5 = models.CharField(max_length=40,blank=True,null=True)
    telephon_number = models.IntegerField(blank=True,null=True)
    mail_address = models.CharField(max_length=50,blank=True,null=True)
    corporatesite_url = models.CharField(max_length=200,blank=True,null=True)
    service_code = models.CharField(max_length=1,blank=True,null=True)
    start_service_day = models.DateField(blank=True,null=True)
    end_service_day = models.DateField(blank=True,null=True)
    service_period = models.IntegerField(blank=True,null=True)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False)
    
class mst_customer_details(models.Model):
    customer_code = models.CharField(max_length=6,blank=False,primary_key=True)
    customer_branch_code = models.CharField(max_length=3,blank=False)
    customer_alias_name = models.CharField(max_length=50,blank=False)
    service_period = models.IntegerField(blank=True,null=True)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False)
    
class mst_number_control(models.Model):
    number_division = models.CharField(max_length=1,blank=False,primary_key=True)
    number_year = models.IntegerField(blank=False)
    number_count = models.IntegerField(default='0',blank=False)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False)
    

class mst_scraping_site_headers(models.Model):
    business_code = models.CharField(max_length=4,blank=False,primary_key=True)
    scraping_site_code = models.CharField(max_length=4,blank=False)
    scraping_site_url = models.CharField(max_length=200,blank=False)
    scraping_site_name = models.CharField(max_length=200,blank=True,null=True)
    scraping_site_status = models.IntegerField(blank=True,null=True)
    scraping_check_day = models.DateField(blank=True,null=True)
    scraping_check_time = models.TextField(blank=True,null=True)
    scraping_check_information = models.CharField(max_length=100,blank=True,null=True)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False)  

#変更箇所
# class mst_scraping_site_information(models.Model):
#     business_code = models.CharField(max_length=4,blank=False,primary_key=True)
#     scraping_site_code = models.CharField(max_length=4,blank=False)
#     scraping_site_branch_code = models.IntegerField(blank=False)
#     scraping_site_sub_url = models.CharField(max_length=200,blank=False)
#     scraping_site_sub_name = models.CharField(max_length=200,blank=True,null=True)
#     scraping_code_status = models.IntegerField(blank=True,null=True)
#     scraping_code_check_day = models.DateField(blank=True,null=True)
#     scraping_code_check_time = models.TimeField(blank=True,null=True)
#     scraping_code_check_information = models.CharField(max_length=100,blank=True,null=True)
#     sys_insert_day = models.DateField(blank=False)
#     sys_insert_time = models.TimeField(blank=False)
#     sys_insert_user = models.CharField(max_length=40,blank=False)
#     sys_update_day = models.DateField(blank=False)
#     sys_update_time = models.TimeField(blank=False)
#     sys_update_user = models.CharField(max_length=40,blank=False)  

class mst_scraping_site_details(models.Model):
    business_code = models.CharField(max_length=4,blank=False,primary_key=True)
    scraping_site_code = models.CharField(max_length=4,blank=False)
    scraping_site_branch_code = models.IntegerField(blank=False)
    scraping_html_code = models.CharField(max_length=4,blank=False)
    scraping_html_name = models.CharField(max_length=50,blank=True,null=True)
    scraping_code_status = models.IntegerField(blank=True,null=True)
    scraping_code_check_day = models.DateField(blank=True,null=True)
    scraping_code_check_time = models.TimeField(blank=True,null=True)
    scraping_code_check_information = models.CharField(max_length=100,blank=True,null=True)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False)  
    
class trn_scraping_headers(models.Model):
    business_code = models.CharField(max_length=4,blank=False,primary_key=True)
    scraping_site_code = models.CharField(max_length=4,blank=False)
    customer_code = models.CharField(max_length=6,blank=False)
    operation_code = models.IntegerField(blank=False)
    scraping_exe_day = models.CharField(max_length=8,blank=False)
    scraping_exe_time = models.CharField(max_length=6,blank=False)
    scraping_exe_status = models.IntegerField(blank=True,null=True)
    scraping_exe_infomation = models.CharField(max_length=100,blank=True,null=True)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False) 

#中間
class trn_scraping_search_information(models.Model):
    business_code = models.CharField(max_length=4,blank=False,primary_key=True)
    scraping_site_code = models.CharField(max_length=4,blank=False)
    scraping_site_custoner_code = models.IntegerField(blank=False)
    scraping_search_day = models.CharField(max_length=8,blank=False)
    scraping_search_time = models.CharField(max_length=6,blank=False)
    scraiping_site_sub_url = models.CharField(max_length=200,blank=False)
    scraping_site_custoner_name = models.CharField(max_length=50,blank=False)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False) 

class trn_scraping_details(models.Model):
    business_code = models.CharField(max_length=4,blank=False,primary_key=True)
    scraping_site_code = models.CharField(max_length=4,blank=False)
    customer_code = models.CharField(max_length=6,blank=False)
    customer_branch_code = models.CharField(max_length=3,blank=False)
    operation_code = models.IntegerField(blank=False)
    scraping_exe_day = models.CharField(max_length=8,blank=False)
    scraping_exe_time = models.CharField(max_length=6,blank=False)
    scraping_html_code = models.CharField(max_length=4,blank=False)
    scraping_html_name = models.CharField(max_length=50,blank=True,null=True)
    customer_alias_name = models.CharField(max_length=50,blank=True,null=True)
    scraping_exe_html_target = models.CharField(max_length=100,blank=True,null=True)
    scraping_exe_status = models.IntegerField(blank=True,null=True)
    scraping_exe_information = models.CharField(max_length=100,blank=True,null=True)
    scraping_exe_html_result = models.CharField(max_length=2000,blank=True,null=True)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False)
    
class sys_operation_log(models.Model):
    log_id = models.CharField(max_length=6,blank=True,null=True)
    application_code = models.CharField(max_length=20,blank=True,null=True)
    operation_kind_code = models.CharField(max_length=1,blank=True,null=True)
    person_name = models.CharField(max_length=20,blank=True,null=True)
    result_status = models.IntegerField(blank=True,null=True)
    ip = models.CharField(max_length=20,blank=True,null=True)
    at = models.DateField(blank=True,null=True)
    operation_information = models.CharField(max_length=100,blank=True,null=True)
    operation_details = models.CharField(max_length=100,blank=True,null=True)
    
class sys_error_log(models.Model):
    eroor_code = models.CharField(max_length=3,blank=False,primary_key=True)
    error_message = models.CharField(max_length=50)
    sys_insert_day = models.DateField(blank=False)
    sys_insert_time = models.TimeField(blank=False)
    sys_insert_user = models.CharField(max_length=40,blank=False)
    sys_update_day = models.DateField(blank=False)
    sys_update_time = models.TimeField(blank=False)
    sys_update_user = models.CharField(max_length=40,blank=False)
    

class testdata_for_select(models.Model):
    business_code = models.CharField(max_length=4,blank=False,primary_key=True,verbose_name='1',)
    scraping_site_code = models.CharField(max_length=4,blank=False,verbose_name='2',)
    customer_code = models.CharField(max_length=6,blank=False,verbose_name='3',)
    customer_branch_code = models.CharField(max_length=3,blank=False,verbose_name='4',)
    operation_code = models.IntegerField(blank=False,verbose_name='5',)
    scraping_exe_day = models.CharField(max_length=8,blank=False,verbose_name='6',)
    scraping_exe_time = models.CharField(max_length=6,blank=False,verbose_name='7',)
    scraping_html_code = models.CharField(max_length=4,blank=False,verbose_name='8',)
    scraping_html_name = models.CharField(max_length=50,blank=True,null=True,verbose_name='9',)
    customer_alias_name = models.CharField(max_length=50,blank=True,null=True,verbose_name='10',)
    scraping_exe_html_target = models.CharField(max_length=100,blank=True,null=True,verbose_name='11',)
    scraping_exe_status = models.IntegerField(blank=True,null=True,verbose_name='12',)
    scraping_exe_information = models.CharField(max_length=100,blank=True,null=True,verbose_name='13',)
    scraping_exe_html_result = models.CharField(max_length=2000,blank=True,null=True,verbose_name='14',)
        
        
class Item(models.Model):
    date = models.DateField(verbose_name='date',)
    col1 = models.FloatField(verbose_name='col1',)
    col2 = models.FloatField(verbose_name='col2',)
    col3 = models.FloatField(verbose_name='col3',)
    col4 = models.FloatField(verbose_name='col4',)
    
    
# def db_select():
#     with connection.cursor() as cursor:
#         cursor.execute('SELECT * FROM persons')
#         #cursor.execute('INSERT INTO sc_app_sample(title,text) values("インサート","する")')
#         #cursor.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING,text STRING)')
#         #cursor.execute('INSERT INTO persons(name,text) values("Sato","です")')
#         #cursor.execute('INSERT INTO persons(name,text) values("Suzuki","ます")')
#         #cursor.execute('INSERT INTO persons(name,text) values("Takahashi","であります")')
#         row = cursor.fetchall()
#         # print(row)
#         cursor.close()
#         return row