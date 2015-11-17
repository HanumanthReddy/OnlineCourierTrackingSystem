from django.shortcuts import render
from centeradmin.forms import OnlineForm
from centeradmin.models import Parcel_Data
from haystack.query import SearchQuerySet
import unirest
from django.db import connection
from datetime import datetime
from mainadmin.models import UserProfile


def index(request):
    category_list = Parcel_Data.objects.all()
    context_dict = {'categories': category_list}

    return render(request, 'index.html', context_dict)


def profile(request):
    return render(request, 'profile.html')  # , context_dict)


# Create your views here.
def search_PID(request):
    pids = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
    return render('search.html', {'pids': pids})


def sms(request):
    pid = str(request.POST.get('pid', ''))
    phno = str(request.POST.get('phno', ''))
    plast = str(request.POST.get('plast', ''))
    pnext = str(request.POST.get('pnext', ''))
    pstatus = str(request.POST.get('pstatus', ''))

    print(phno)
    msg = "YOUR PARCEL WITH ID : " + pid + " IS AT " + plast + ". NEXT STATION : " + pnext + ". STATUS : " + pstatus + "- Regards : MIST Courier Services."

    print(msg)

    response = unirest.get(
        "https://site2sms.p.mashape.com/index.php?msg=" + msg + "&phone=" + phno + "&pwd=nsknsp10&uid=9494473579",
        headers={
            "X-Mashape-Key": "8Mm8na6YEamsh3KZtQjBfHVXQjl4p1nM6G7jsntyy4P1F2By56",
            "Accept": "application/json"
        }
    )

    cont = {'phno': phno, 'pid': pid}
    return render(request, 'profile.html', cont)


def online(request):
    if request.method == 'POST':
        form = OnlineForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            home = 'hello'
            return render(request, 'profile.html', {'home': home})
        else:
            print form.errors
    else:
        form = OnlineForm()

    return render(request, 'online.html', {'form': form})


def submit(request):
    ptype = str(request.POST.get('ptype', ''))
    pemail = str(request.POST.get('pemail', ''))
    psource = str(request.POST.get('psource', ''))
    pdestination = str(request.POST.get('pdestination', ''))
    psaddress = str(request.POST.get('psaddress', ''))
    pdaddress = str(request.POST.get('pdaddress', ''))
    pmobile = str(request.POST.get('pmobile', ''))

    cursor = connection.cursor()

    cursor.execute("SELECT P_ID FROM centeradmin_parcel_data ORDER BY id DESC LIMIT 1;")
    row = cursor.fetchone()

    print row

    print (psource)
    print(pdestination)

    # C_ID = models.ForeignKey(UserProfile)
    # P_ID = models.CharField(max_length='128')
    # P_Date = models.DateField(default='1990-11-05')
    # P_Source = models.CharField(max_length='128')
    # P_Destination = models.CharField(max_length='128')
    # P_A_Time = models.DateTimeField(auto_now_add = True, auto_now = False)
    # P_D_Time = models.DateTimeField(auto_now_add = True, auto_now = False)
    # P_Last = models.CharField(max_length='128')
    # P_Next = models.CharField(max_length='128')
    # P_Status = models.CharField(max_length='128', choices=[('In_Transit', 'In_Transit'), ('Delivered', 'Delivered'),('Cancelled', 'Cancelled')])

    p = Parcel_Data(P_ID='1_P1113', P_Source=psource, P_Destination=pdestination, P_A_Time=datetime.now(),
                    P_D_Time=datetime.now(), P_Last=psource, P_Next='-', P_Status='In_Transit')
    p.save()

    msg = "WE HAVE RECEIVED AN ONLINE PARCEL ORDER . GENERATED PARCEL ID : 1_P1113. OUR REPRESENTATIVE WILL COME AND COLLECT YOUR PARCEL WITH IN TWO HOURS. Regards : MIST Courier Services."

    print(msg)

    response = unirest.get(
        "https://site2sms.p.mashape.com/index.php?msg=" + msg + "&phone=" + pmobile + "&pwd=nsknsp10&uid=9494473579",
        headers={
            "X-Mashape-Key": "8Mm8na6YEamsh3KZtQjBfHVXQjl4p1nM6G7jsntyy4P1F2By56",
            "Accept": "application/json"
        }
    )
    #    formonline = {'ptype':ptype, 'pemail':pemail,'psource':psource,'pdestination':pdestination,'psaddress':psaddress,'pdaddress':pdaddress,'pmobile':pmobile}
    homee = "homee"
    return render(request, 'profile.html', {'homee': homee})


def cancel(request):
    return render(request, 'cancel.html')


def cancelled(request):
    pid = str(request.POST.get('pid', ''))
    t = Parcel_Data.objects.get(P_ID=pid)
    t.P_Status = "Cancelled"  # change field
    t.save()  # this will update only

    canc = 'canc'
    return render(request, 'profile.html', {'canc': canc})


def submitfeedback(request):
    feed = 'feed'
    return render(request, 'index.html', {'feed': feed})

    # def add_page(request, category_name_slug):
    #
    #     try:
    #         cat = Category.objects.get(slug=category_name_slug)
    #     except Category.DoesNotExist:
    #                 cat = None
    #
    #     if request.method == 'POST':
    #         form = PageForm(request.POST)
    #         if form.is_valid():
    #             if cat:
    #                 page = form.save(commit=False)
    #                 page.category = cat
    #                 page.views = 0
    #                 page.save()
    #                 # probably better to use a redirect here.
    #                 return category(request, category_name_slug)
    #         else:
    #             print form.errors
    #     else:
    #         form = PageForm()
    #
    #     context_dict = {'form':form, 'category': cat}
    #
    #     return render(request, 'rango/add_page.html', context_dict)
