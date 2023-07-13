from django.db import models

class Ticket(models.Model):
    name=models.CharField(max_length=100)
    contactNumber=models.CharField(max_length=10)
    email=models.EmailField()
    vehicleMake=models.CharField(max_length=20)
    vehicleRegNumber=models.CharField(max_length=10)
    breakdownIssue=models.TextField()
    location=models.TextField()
    comments=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.name

class Accounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    create_date = models.DateField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    # alternate_phone = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)

class AccountTypes(models.Model):
    account_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    #create_date = models.DateField()

class Cases(models.Model):
    case_id = models.AutoField(primary_key=True)
    dispatch_entry_id = models.ForeignKey('DispatchEntry', on_delete=models.CASCADE)
    csr_id = models.ForeignKey('SystemUser',on_delete=models.CASCADE)

class Company(models.Model):
    company_id = models.IntegerField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    create_date = models.DateField()
    company_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    auth_token = models.CharField(max_length=100)
    is_deleted = models.BooleanField()
    monthly_fee = models.FloatField()
    notes = models.TextField()
    #free_trial_date_left = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class CompanyFeatures(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    company_features_id = models.IntegerField()
    feature_id = models.ForeignKey('Features', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    create_date = models.DateField()

class CompanyPricing(models.Model):
    id = models.AutoField(primary_key=True)
    rate_item_id = models.ForeignKey('RateItem', on_delete=models.CASCADE)
    default_rate = models.FloatField()
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=100)

class CustomerFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customers', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    notes = models.TextField()

class DispatchEntry(models.Model):
    dispatch_entry_id = models.AutoField(primary_key=True)
    case = models.ForeignKey('Cases', on_delete=models.CASCADE)
    create_date = models.DateField()
    partner_caseid = models.IntegerField()
    partner_service_id = models.IntegerField()
    account_id = models.ForeignKey('Accounts', on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    service_type_id = models.ForeignKey('ServiceTypes', on_delete=models.CASCADE)
    reason_id = models.ForeignKey('Reasons', on_delete=models.CASCADE)
    customer_id = models.ForeignKey('Customers', on_delete=models.CASCADE)
    asset_id = models.ForeignKey('DispatchEntryAssets', on_delete=models.CASCADE)
    dispatch_status_id = models.ForeignKey('DispatchStatus', on_delete=models.CASCADE)
    repair_status = models.CharField(max_length=100)
    csr_id = models.ForeignKey('SystemUser',on_delete=models.CASCADE)
    company_id = models.ForeignKey('Company',on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    is_scheduled = models.BooleanField()
    invoice_id = models.ForeignKey('Invoices', on_delete=models.CASCADE)
    payment_id = models.ForeignKey('Payments', on_delete=models.CASCADE, related_name='dispatch_entries_payment_id')
    payment_status = models.ForeignKey('Payments', on_delete=models.CASCADE, related_name='dispatch_entries_payment_status')
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    eta = models.DateTimeField()
    ata = models.DateTimeField()

class DispatchEntryAssets(models.Model):
    asset_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customers', on_delete=models.CASCADE)
    dispatch_entry_id = models.ForeignKey('DispatchEntry', on_delete=models.CASCADE)
    colorid = models.CharField(max_length=100)
    body_type_id = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    model_year = models.IntegerField()
    license_plate = models.CharField(max_length=100)
    license_state = models.CharField(max_length=100)
    license_year = models.IntegerField()
    create_date = models.DateField()
    
class DispatchEntryStatusRecords():
    id = models.AutoField(primary_key=True)
    dispatch_entry_id = models.ForeignKey('DispatchEntry', on_delete=models.CASCADE)
    owner_user_id = models.IntegerField()
    previous_status_d=models.IntegerField()
    new_status_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    driver_id =  models.IntegerField()
    create_date = models.DateField()

class DispatchStatus(models.Model):
    dispatch_status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class DriverLocation(models.Model):
    driverLocation_id = models.AutoField(primary_key=True)
    create_date = models.DateField()
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    client_version_id = models.IntegerField()
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

class Features(models.Model):
    feature_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    create_date = models.DateField()

class Invoices(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    create_date = models.DateField()
    reference_number = models.CharField(max_length=100)
    ponumber = models.CharField(max_length=100)
    txn_number = models.CharField(max_length=100)
    customer = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    subtotal = models.FloatField()
    tax = models.FloatField()
    total_amount = models.FloatField()
    billing_email = models.EmailField()
    dispatch_amount = models.FloatField()
    dispatch_rate = models.FloatField()

class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey('Invoices', on_delete=models.CASCADE)
    notes = models.TextField()
    txn_number = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    amount = models.FloatField()
    create_date = models.DateField()
    status = models.CharField(max_length=100)

class RateItem(models.Model):
    rate_item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    account_id = models.ForeignKey('Accounts', on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    account_company_id = models.IntegerField()
    # min_quantity = models.IntegerField()
    # max_quantity = models.IntegerField()
    vehicle_id = models.ForeignKey('Vehicles', on_delete=models.CASCADE)
    # extended_rate_item = models.IntegerField()
    default_rate_4w = models.IntegerField()
    default_rate_2w = models.IntegerField()
    budget_2w = models.IntegerField()
    premium_2w = models.IntegerField()
    luxury_2w = models.IntegerField()
    budget_4w = models.IntegerField()
    premium_4w = models.IntegerField()
    luxury_4w = models.IntegerField()
    suv_4w = models.IntegerField()

class Reasons(models.Model):
    reason_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    create_date = models.DateField()
    service_type = models.CharField(max_length=100)

class ServiceTypes(models.Model):
    service_type_id = models.AutoField(primary_key=True)
    service = models.CharField(max_length=100)
    service_type=models.CharField(max_length=10)

class SystemUser(models.Model):
    csr_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    create_date = models.DateField()
    role=models.CharField(max_length=50)
    role_id = models.IntegerField()
    status = models.CharField(max_length=100)

class SystemUserStatusRecords(models.Model):
    id = models.AutoField(primary_key=True)
    dispatch_entry_id = models.ForeignKey('DispatchEntry', on_delete=models.CASCADE)
    previous_csr_id = models.IntegerField()
    new_csr_id=models.IntegerField()
    create_date = models.DateField()
    
class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    # make_id = models.IntegerField()
    make = models.CharField(max_length=100)
    # model_id = models.IntegerField()
    # model = models.CharField(max_length=100)
    # year = models.IntegerField()
    vehicle_class = models.CharField(max_length=100)
    vehicle_type = models.IntegerField()