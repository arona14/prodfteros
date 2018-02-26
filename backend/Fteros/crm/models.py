from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

CUSTOMER_TYPES = (
    ('A','Agency'),
    ('C', 'Corporate'),
    ('L', 'Leisure'),
    ('V', 'Vendor'),
    ('U', 'User'),
)

CONTRACT_TYPES = (
    ('N','NET'),
    ('P','PUB'),
    ('C','COM'),
)

OWRT = (
    ('OW','One way'),
    ('RT', 'Round trip'),
    ('AN', 'Any'),
)

MRD = (
    ('M','Markup'),
    ('R','Rewards'),
    ('D','Dropnet'),
)

STATUS = (
    ('r','Resolved'),
)

class BaseEnity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length = 50, null = True, blank = True)

    class Meta:
        abstract = True


class Affiliate(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):     
        return self.name

    def __str__(self):
        return self.name


class Customer(BaseEnity):
    """
        Creates a customer table where all types as above will be stored
    """
    agency_id = models.CharField(max_length=100) 
    interface_id = models.CharField(max_length=100) # DK or code_iata
    name = models.CharField(max_length=100)    
    address1 = models.CharField(max_length=100, null = True, blank = True)
    address2 = models.CharField(max_length=100,null = True, blank = True)
    city = models.CharField(max_length=50, null = True, blank = True)
    state = models.CharField(max_length=25, null = True, blank = True)
    country = models.CharField(max_length=50, null = True, blank = True)
    zip_code = models.CharField(max_length=20, null = True, blank = True)
    customer_type = models.CharField(max_length=5,choices= CUSTOMER_TYPES)
    email = models.EmailField(null = True, blank = True)
    phone = models.CharField(max_length=25,null = True, blank = True)
    fax = models.CharField(max_length=25,null = True, blank = True)
    group = models.ForeignKey(Affiliate, related_name='group', on_delete=models.CASCADE)
    
    
    def __unicode__(self):     
        return self.name

    def __str__(self):
        return self.name


class Communication(BaseEnity):

    agency = models.OneToOneField(Customer,related_name='agency',on_delete=models.CASCADE)
    email_itin = models.EmailField(null = True, blank = True)
    email_sched = models.EmailField(null = True, blank = True)
    email_marketting = models.EmailField(null = True, blank = True)
    email_accounting = models.EmailField(null = True, blank = True)
    email_invoice = models.EmailField(null = True, blank = True)
    phone_cell = models.CharField(max_length=25)
    phone_home = models.CharField(max_length=25,null = True, blank = True)
    phone_office = models.CharField(max_length=25,null = True, blank = True)
    fax_1 = models.CharField(max_length=25,null = True, blank = True)
    fax_2 = models.CharField(max_length=25,null = True, blank = True)

class Role(BaseEnity):

    name = models.CharField(max_length=50)

    def __str__(self):
        
        return self.name

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, first_name, last_name, password = None):

        if not email:
            raise ValueError('Users must have a valid email address.')

        email = self.normalize_email(email)
        user = self.model(email = email, first_name = first_name, last_name = last_name)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, first_name,last_name, password):

        user = self.create_user(email, first_name,last_name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length = 30, null = True, blank = True)
    last_name = models.CharField( max_length = 30, null = True, blank = True)
    date_joined = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = True)
    updated_by = models.CharField(max_length = 50, null = True, blank = True)
    customer = models.ForeignKey(Customer, related_name='customer', on_delete = models.CASCADE, null = True, blank = True)
    role = models.ForeignKey(Role, related_name='role', on_delete=models.CASCADE, null = True, blank = True)

    # UserDetails
    agent_cc = models.CharField( max_length=30, null = True, blank = True)
    gds = models.CharField( max_length=30, null = True, blank = True)
    sign = models.CharField( max_length=30, null = True, blank = True)
    queue1 = models.CharField(max_length=25, null = True, blank = True)
    queue2 = models.CharField(max_length=25, null = True, blank = True)
    queue3 = models.CharField(max_length=25, null = True, blank = True)
    queue4 = models.CharField(max_length=25, null = True, blank = True)
    queue5 = models.CharField(max_length=25, null = True, blank = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        
       # Returns the first_name plus the last_name, with a space in between.
        
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


    def get_short_name(self):
        
        #Returns the short name for the user.
        
        return self.first_name


    def __unicode__(self):
        
        return self.email

    def __str__(self):
        
        return self.email


class Contract(BaseEnity):

    name = models.CharField(max_length = 50)
    owrt = models.CharField(max_length = 2, choices = OWRT)
    from_base_amt = models.FloatField(default = 0)
    from_total_amt = models.FloatField(default = 0)
    from_com_amt = models.FloatField(default = 0)
    to_base_amt = models.FloatField(default = 50000)
    to_total_amt = models.FloatField(default = 50000)
    to_com_amt = models.FloatField(default = 50000)
    class_svc = models.CharField(max_length = 10, null = True, blank = True)
    origin = models.CharField(max_length = 100, default = 'ANY', null = True, blank = True)
    destination = models.CharField(max_length = 100, default = 'ANY', null = True, blank = True)
    x_origin = models.CharField(max_length = 100, null = True, blank = True)
    x_destination = models.CharField(max_length = 100, null = True, blank = True)
    fare_basis = models.CharField(max_length = 50, default = 'ANY', null = True, blank = True)
    tour_code = models.CharField(max_length = 50, default = 'ANY', null = True, blank = True)
    tkt_designator = models.CharField(max_length = 50, default = 'ANY', null = True, blank = True)
    flight_no = models.CharField(max_length = 150, default = 'ANY', null = True, blank = True)
    inbound_flight = models.CharField(max_length = 150, default = 'ANY', null = True, blank = True)
    outbound_flight = models.CharField(max_length = 150, default = 'ANY', null = True, blank = True)
    issued_from = models.DateField(default = '0001-01-01', null = True, blank = True)
    issued_until = models.DateField(default = '0001-01-01', null = True, blank = True)
    dep_from = models.DateField(default = '0001-01-01', null = True, blank = True)
    dep_until= models.DateField(default = '0001-01-01', null = True, blank = True)
    ret_from = models.DateField(default = '0001-01-01', null = True, blank = True)
    ret_until = models.DateField(default = '0001-01-01', null = True, blank = True)
    issued_from_blackout = models.DateField(default = '0001-01-01', null = True, blank = True)
    issued_until_blackout = models.DateField(default = '0001-01-01', null = True, blank = True)
    dep_from_blackout = models.DateField(default = '0001-01-01', null = True, blank = True)
    dep_until_blackout= models.DateField(default = '0001-01-01', null = True, blank = True)
    ret_from_blackout = models.DateField(default = '0001-01-01', null = True, blank = True)
    ret_until_blackout = models.DateField(default = '0001-01-01', null = True, blank = True)
    arc_no = models.CharField(max_length = 50, default = 'ANY', null = True, blank = True)
    via_points = models.CharField(max_length = 100, default = 'ANY', null = True, blank = True)
    x_via_points = models.CharField(max_length = 100, null = True, blank = True)
    seasonality = models.CharField(max_length = 100, null = True, blank = True)
    trip_type = models.CharField(max_length = 25, null = True, blank = True)
    description = models.CharField(max_length = 600, null = True, blank = True)
    statut = models.BooleanField(default = True)

    def __unicode__(self):
        
        return self.name

    def __str__(self):
        return self.name


class Markup(BaseEnity):
    # The base contract that the customer is qualified
    contract = models.ForeignKey(Contract, related_name = 'markup_contract', on_delete = models.CASCADE)

    # The customer for the contract
    customer = models.ForeignKey(Customer, related_name = 'agency_markup', on_delete = models.CASCADE)
    
    # association class for airlines (customer of vendor type) exceptions
    x_airlines = models.ManyToManyField(Customer, related_name = 'contracts' , through='ExceptionAirline')

    # Markup Reward Dropnet
    net = models.CharField(max_length = 5, default = '0', null = True, blank = True)
    pub = models.CharField(max_length = 5, default = '0', null = True, blank = True)
    com = models.CharField(max_length = 5, default = '0', null = True, blank = True)

class Reward(BaseEnity):

    contract = models.ForeignKey(Contract, related_name = 'reward_contract', on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, related_name = 'agency_reward', on_delete = models.CASCADE)
    pax_type = models.CharField(max_length = 15, null = True, blank = True)
    airline = models.CharField(max_length = 5, null =True, blank = True)
    reward_value = models.CharField(max_length = 5, default = '0', null = True, blank = True)

class Dropnet(BaseEnity):

    contract = models.ForeignKey(Contract, related_name = 'dropnet_contract', on_delete = models.CASCADE)
    pax_type = models.CharField(max_length = 15, null = True, blank = True)
    airline = models.CharField(max_length = 5, null = True, blank = True)
    dropnet_value = models.CharField(max_length = 5, default = '0', null = True, blank = True)



class ExceptionAirline(BaseEnity):
    airline = models.ForeignKey(Customer, on_delete=models.CASCADE)
    markup = models.ForeignKey(Markup, on_delete=models.CASCADE)
    net_value = models.CharField(max_length = 5, default = '0', null = True, blank = True)
    pub_value = models.CharField(max_length = 5, default = '0', null = True, blank = True)
    com_value = models.CharField(max_length = 5, default = '0', null = True, blank = True)



class Traveler(BaseEnity):
    traveler_of = models.ForeignKey(Customer , on_delete=models.CASCADE)
    relationship = models.CharField(max_length=25,null = True, blank = True) #primary,son,daughter,wife, grandma etc...
    title = models.CharField(max_length=10,null = True, blank = True) # mr, mrs etc...
    first_name = models.CharField(max_length=30,null = True, blank = True)
    middle_name = models.CharField(max_length=30,null = True, blank = True)
    last_name = models.CharField(max_length=30,null = True, blank = True)
    gender = models.CharField(max_length=6,null = True, blank = True)
    citizenship = models.CharField(max_length=30,null = True, blank = True)
    passport_no = models.CharField(max_length=30,null = True, blank = True)
    notes = models.TextField(null = True, blank = True)#remarks
    birthdate = models.DateField(null = True, blank = True)


class BugReport(BaseEnity):

    title = models.CharField(max_length=30,blank=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    status  = models.CharField(max_length = 2, choices = STATUS)
