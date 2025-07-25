# Create your views here.
from django.shortcuts import render, redirect
from .models import Member


def form_view(request):
    return render(request, 'form.html')


def submit_form(request):

    # yo function if hamro aako request ko method chai POST xa vane
    if request.method == 'POST':
        # name linu paryo kasari hamro request.POST bata name chai hamro database ma post gardinu paryo
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        # get ra normala post ko difference chai post garyo vane data dinai parxa diyena vane key error dinxa
        family_id = request.POST.get('family_id', '')
        show_age = request.POST.get('show_age') == 'on'
        # gae ko lagi chai hamro check box ma cliked vayo vane on natra empty dekhauxa

        # yo bata aaba hamro database ko lagi data hamle Memeber vanne class ko data rakheko aaba tyoo mathi ko dtaa lai nai rakahn paryo

        member = Member.objects.create(
            name=name,
            age=age,
            sex=sex,
            family_id=family_id,
            show_age=show_age
        )

        # if family_id user le diyo vane tyo user ra tesko aaba aaune fammily ko naya page banaera dekhauxa
        if family_id:
            return redirect('family_page', family_id=family_id)
        else:
            # edi family id cain vane chai tyo user ko lagi normal welcome page dekhauxa
            return render(request, 'welcome.html', {'member': member})


# hamle mathi ko function bata data lida family_id= family_id vanera parametwe pass garem
def family_page(request, family_id):
    # yo chai aaba hamro family page ma family_id leara janako lagi ho

    # esma chai hamro memebers haru chanera family_id herdai filter garxa aani tyo memebr haruko data dekhauxa
    members = Member.objects.filter(family_id=family_id)
    # family_page dekhaune jasma sabbai memers haru filter vako jati ko name haru aaos
    return render(request, 'family.html', {'members': members, 'family_id': family_id})
