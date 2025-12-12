from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from orange.models import Event,Day,Organization
from accounts.models import Account
from django.contrib.auth import get_user_model, authenticate, login
User= get_user_model()
from django.core.exceptions import ObjectDoesNotExist
import math
import json
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core import serializers
from datetime import timedelta
from django.utils import timezone
from orange.language import languagedic
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.
class Homepage(TemplateView):
    template_name= 'orange/home.html'
    def get(self, request):

        specific_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        days = Day.objects.filter(date__gte=specific_date)[:7]

        languagecookie="de"
        try:
            languagecookie=request.COOKIES["language"]
        except:
            pass
        else:
            pass
        finally:
            pass


        args = {"daylist":days,"language":languagedic[languagecookie]["home"],"navlang":languagedic[languagecookie]["nav"]}
        return render(request,self.template_name,args)

class ThanksPage(TemplateView):
    template_name= 'orange/thanks.html'

    def get(self,request):
        try:
            args={"url":request.headers["Referer"]}
        except Exception as e:
            args={"url":"byefriend"}


        return render(request,self.template_name,args)

class Welcomepage(TemplateView):
    template_name= 'orange/welcome.html'
    def get(self, request):

        languagecookie="de"
        try:
            languagecookie=request.COOKIES["language"]
        except:
            pass
        else:
            pass
        finally:
            pass

        args = {"from":"calander","navlang":languagedic[languagecookie]["nav"]}
        return render(request,self.template_name,args)

class Aboutpage(TemplateView):
    template_name= 'orange/about.html'
    def get(self, request):

        languagecookie="de"
        try:
            languagecookie=request.COOKIES["language"]
        except:
            pass
        else:
            pass
        finally:
            pass

        args = {"from":"about","navlang":languagedic[languagecookie]["nav"],"about":languagedic[languagecookie]["about"]}
        return render(request,self.template_name,args)

class Goalpage(TemplateView):
    template_name= 'orange/goal.html'
    def get(self, request):

        languagecookie="de"
        try:
            languagecookie=request.COOKIES["language"]
        except:
            pass
        else:
            pass
        finally:
            pass

        args = {"from":"about","navlang":languagedic[languagecookie]["nav"],"goal":languagedic[languagecookie]["goal"]}
        return render(request,self.template_name,args)

class Signin(TemplateView):

    def post(self,request):

        nameinput=request.POST.get('username')
        passinput=request.POST.get('password')
        thetype=request.POST.get('sub')
        next = request.POST.get('next', '/')


        searchtext="login sucessful"
        if thetype=="login":
            try:
                theuser=User.objects.get(email=nameinput.lower())
            except Exception as e:
                specific_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
                days = Day.objects.filter(date__gte=specific_date)[:7]
                languagecookie=request.COOKIES["language"]
                searchtext=languagedic[languagecookie]["alert"]["nouser1"]+nameinput+languagedic[languagecookie]["alert"]["nouser2"]
                args = {"legalnext":"/","daylist":days,"language":languagedic[languagecookie]["home"],"navlang":languagedic[languagecookie]["nav"],"signininfo":{"alert":"yes","text":searchtext}}
                return render(request,'orange/home.html',args)
            user = authenticate(request, email=nameinput.lower(), password=passinput)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                specific_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
                days = Day.objects.filter(date__gte=specific_date)[:7]
                languagecookie=request.COOKIES["language"]
                searchtext=languagedic[languagecookie]["alert"]["nopass"]+nameinput
                args = {"legalnext":"/","daylist":days,"language":languagedic[languagecookie]["home"],"navlang":languagedic[languagecookie]["nav"],"signininfo":{"alert":"yes","text":searchtext}}
                return render(request,'orange/home.html',args)

        if thetype=="signup":
            username2=nameinput
            password=passinput
            try:
                User.objects.create_user(username=username2.split("@")[0],email=username2.lower(),password=password)
                logyouin = authenticate(request, email=username2.lower(), password=password)
                login(request, logyouin)
                return HttpResponseRedirect(next)
            except Exception as e:
                specific_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
                days = Day.objects.filter(date__gte=specific_date)[:7]
                languagecookie=request.COOKIES["language"]
                searchtext=languagedic[languagecookie]["alert"]["taken1"]+username2.lower()+languagedic[languagecookie]["alert"]["taken2"]
                args = {"legalnext":"/","daylist":days,"language":languagedic[languagecookie]["home"],"navlang":languagedic[languagecookie]["nav"],"signininfo":{"alert":"yes","text":searchtext}}
                return render(request,'orange/home.html',args)

        if thetype=="edit":
            name= request.POST.get('name')
            pic= request.FILES.get('pic')
            blank= request.POST.get('blank')
            if blank=="delete":
                request.user.display_pic.delete()
            if pic:
                request.user.display_pic=pic
            request.user.username=name
            request.user.save()
            return HttpResponseRedirect(next)

        response=HttpResponse(searchtext)
        return response

class EventInfo(TemplateView):
    template_name = 'orange/event_info.html'

    def get(self, request, slug):
        event= get_object_or_404(Event,slug=self.kwargs.get('slug'))

        languagecookie="de"
        try:
            languagecookie=request.COOKIES["language"]
        except:
            pass
        else:
            pass
        finally:
            pass

        args = {'event':event,"language":languagedic[languagecookie]["event_info"],"navlang":languagedic[languagecookie]["nav"]}
        return render(request,self.template_name,args)

class OrganizationInfo(TemplateView):
    template_name = 'orange/org_info.html'

    def get(self, request, slug):
        org= get_object_or_404(Organization,slug=self.kwargs.get('slug'))

        languagecookie="de"
        try:
            languagecookie=request.COOKIES["language"]
        except:
            pass
        else:
            pass
        finally:
            pass

        args = {'org':org,"navlang":languagedic[languagecookie]["org_info"],"navlang":languagedic[languagecookie]["nav"]}
        return render(request,self.template_name,args)

class Calander(TemplateView):
    template_name = 'orange/calander.html'

    def get(self, request):

        daylist= Day.objects.all()
        daydic={}
        for day in daylist:
            endtime = str(day.date.day)+"-"+str(day.date.month)+"-"+str(day.date.year)
            daydic[endtime]={"date":endtime,"times":day.times,"closed":day.closed,"events":{}}
            for event in day.events.all():
                daydic[endtime]["events"][event.name]=[event.name,event.slug]
        theam=range(1,13)
        thepm=range(13,25)

        languagecookie="de"
        try:
            languagecookie=request.COOKIES["language"]
        except:
            pass
        else:
            pass
        finally:
            pass


        args = {"daylist":daydic,"theam":theam,"thepm":thepm,"from":"calander","language":languagedic[languagecookie]["calander"],"eventform":languagedic[languagecookie]["event_form"],"navlang":languagedic[languagecookie]["nav"]}

        if request.session.get('newevent'):
            args["signininfo"]={"alert":"yes","text":languagedic[languagecookie]["alert"]["eve1"]}
            del request.session['newevent']

        if request.session.get('eventinuse'):
            args["signininfo"]={"alert":"yes","text":languagedic[languagecookie]["alert"]["eve2"]}
            del request.session['eventinuse']

        return render(request,self.template_name,args)

class NewEvent(TemplateView):
    template_name = 'orange/calander.html'
    def post(self,request):
        nameinput=request.POST.get('name')
        descriptioninput=request.POST.get('description')
        descriptionshort=request.POST.get('descriptionshort')
        additionalinfo=request.POST.get('additionalinfo')
        org=request.POST.get('orgselect')
        picinput=request.FILES.get('pic')
        priceinput=request.POST.get('price')
        link=request.POST.get('link')
        linkto=request.POST.get('linkto')
        thefrom=request.POST.get('from')

        try:
            chosen_event=Event.objects.get(name=nameinput)
            if thefrom=="calander":
                if request.user != chosen_event.user:
                    request.session['eventinuse'] = True
                    return HttpResponseRedirect(thefrom)
            chosen_event.name = nameinput
            chosen_event.description=descriptioninput
            chosen_event.description_short=descriptionshort
            chosen_event.additional_info=additionalinfo
            if picinput:
                chosen_event.mainpic=picinput
            if org!="none":
                orgtoadd= get_object_or_404(Organization,name=org)
                chosen_event.org=orgtoadd
            chosen_event.price=priceinput
            chosen_event.link_to_external_site=link
            chosen_event.link_button_text=linkto

            chosen_event.save()
        except ObjectDoesNotExist:
            newthing=Event(
                name = nameinput,
                description=descriptioninput,
                description_short=descriptionshort,
                additional_info=additionalinfo,
                mainpic=picinput,
                price=priceinput,
                link_to_external_site=link,
                link_button_text=linkto
            )
            request.session['newevent'] = True
            if request.user:
                newthing.user=request.user
            if org!="none":
                orgtoadd= get_object_or_404(Organization,name=org)
                newthing.org=orgtoadd
            newthing.save()

        return HttpResponseRedirect(thefrom)

class SaveDay(TemplateView):
    template_name = 'orange/calander.html'
    def post(self,request):

        decodedword=json.loads(request.body.decode('ascii'))
        dateoption=decodedword["date"]
        eventoption=decodedword["event"]
        times=decodedword["times"]

        try:
            chosen_day=Day.objects.get(date=dateoption)
            event=Event.objects.get(name=eventoption)
            chosen_day.events.add(event)
            for hour in times:
                chosen_day.times[hour]=eventoption
            chosen_day.save()
        except ObjectDoesNotExist:
            chosen_day=Day(date=dateoption)
            chosen_day.save()
            event=Event.objects.get(name=eventoption)
            chosen_day.events.add(event)
            for hour in times:
                chosen_day.times[hour]=eventoption
            chosen_day.save()

        daylist= Day.objects.all()
        daydic={}
        for day in daylist:
            endtime = str(day.date.day)+"-"+str(day.date.month)+"-"+str(day.date.year)
            daydic[endtime]={"date":endtime,"times":day.times,"closed":day.closed,"events":[]}
            for event in day.events.all():
                daydic[endtime]["events"].append(event.name)

        response=JsonResponse(daydic)

        return response

class Profile(TemplateView):
    template_name = 'orange/profile.html'

    def get(self, request):

        eventdic={}
        orgdic={
            "orgs":[],
            "myorgs":[],
            "myadmins":[],
            "mypresidents":[]
        }
        emaillist=[]
        if request.user.is_authenticated:

            orglist= Organization.objects.all()

            for org in orglist:
                orgdic["orgs"].append({"name":org.name,"slug":org.slug})

                if request.user in org.members.all():
                    orgdic["myorgs"].append({"name":org.name,"slug":org.slug})

                if request.user in org.admins.all():
                    admindic={"name":org.name,"slug":org.slug,"requests":[]}
                    for guy in org.member_requests.all():
                        admindic["requests"].append(guy.email)
                    orgdic["myadmins"].append(admindic)

                    for event in org.event_set.all():
                        if event.user != request.user:
                            eventdic[event.slug]={
                                "name":event.name,
                                "slug":event.slug,
                                "description":event.description,
                                "description_short":event.description_short,
                                "additional_info":event.additional_info,
                                "price":event.price,
                                "link_to_external_site":event.link_to_external_site,
                                "link_button_text":event.link_button_text
                            }


                if request.user == org.president:
                    presdic={
                    "name":org.name,
                    "slug":org.slug,
                    "admins":[],
                    "normies":[]
                    }
                    for bigguy in org.members.all():
                        if bigguy in org.admins.all():
                            if bigguy != request.user:
                                presdic["admins"].append(bigguy.email)
                        else:
                            presdic["normies"].append(bigguy.email)
                    orgdic["mypresidents"].append(presdic)

            eventlist =request.user.eventowner.all()
            for event in eventlist:
                eventdic[event.slug]={
                    "name":event.name,
                    "slug":event.slug,
                    "description":event.description,
                    "description_short":event.description_short,
                    "additional_info":event.additional_info,
                    "price":event.price,
                    "link_to_external_site":event.link_to_external_site,
                    "link_button_text":event.link_button_text
                }

            if request.user.is_admin:
                for eve in Event.objects.all():
                    emaillist.append(eve.name)

        languagecookie="de"
        try:
            languagecookie=request.COOKIES["language"]
        except:
            pass
        else:
            pass
        finally:
            pass

        args = {"emaillist":emaillist,"orgdic":orgdic,"eventdic":eventdic,"from":"profile","language":languagedic[languagecookie]["profile"],"navlang":languagedic[languagecookie]["nav"],"eventform":languagedic[languagecookie]["event_form"]}
        return render(request,self.template_name,args)

class NewOrg(TemplateView):
    template_name = 'orange/profile.html'
    def post(self,request):
        nameinput=request.POST.get('name')
        descriptioninput=request.POST.get('description')
        picinput=request.FILES.get('pic')
        link=request.POST.get('link')
        linkto=request.POST.get('linkto')
        president=request.POST.get('president')

        newthing=Organization(
            name = nameinput,
            description=descriptioninput,
            mainpic=picinput,
            link_to_external_site=link,
            link_button_text=linkto
        )
        newthing.save()

        if president=="yes":
            newthing.president=request.user
        newthing.members.add(request.user)
        newthing.admins.add(request.user)
        newthing.save()


        return HttpResponseRedirect("/orange/profile")

class SendInfo(TemplateView):
    template_name = 'orange/profile.html'
    def post(self,request):

        decodedword=json.loads(request.body.decode('ascii'))
        typeoption=decodedword["type"]
        nameoption=decodedword["name"]
        person=decodedword["person"]

        returninfo={
            "message":"just checking",
            "check":""
        }

        if typeoption=="member_request":
            club=Organization.objects.get(name=nameoption)
            club.member_requests.add(request.user)
            returninfo["message"]="your request to join has been sent. no further action needed"
        if typeoption=="approvemember":
            club=Organization.objects.get(slug=nameoption)
            newbie=User.objects.get(email=person)
            club.members.add(newbie)
            club.member_requests.remove(newbie)
            returninfo["message"]=person+" has been add to"+club.name
        if typeoption=="declinemember":
            club=Organization.objects.get(slug=nameoption)
            newbie=User.objects.get(email=person)
            club.member_requests.remove(newbie)
            returninfo["message"]=person+" wont be bothering you anymore"
        if typeoption=="promotemember":
            club=Organization.objects.get(slug=nameoption)
            newbie=User.objects.get(email=person)
            club.admins.add(newbie)
            returninfo["message"]=person+" was promoted to administrator"
        if typeoption=="demotemember":
            club=Organization.objects.get(slug=nameoption)
            newbie=User.objects.get(email=person)
            club.admins.remove(newbie)
            returninfo["message"]=person+" was demoted"
        if typeoption=="kickmember":
            club=Organization.objects.get(slug=nameoption)
            newbie=User.objects.get(email=person)
            club.members.remove(newbie)
            returninfo["message"]=person+" was removed from "+club.name
        if typeoption=="leaveclub":
            club=Organization.objects.get(slug=nameoption)
            club.members.remove(request.user)
            club.admins.remove(request.user)
        if typeoption=="deleteevent":
            event=Event.objects.get(slug=nameoption)
            event.delete()

        if typeoption=="attendevent":
            event=Event.objects.get(slug=nameoption)
            event.tendies.add(request.user)
            returninfo["message"]="you were added to attendie list!"
            returninfo["check"]="success"

        if typeoption=="dontattendevent":
            event=Event.objects.get(slug=nameoption)
            event.tendies.remove(request.user)
            returninfo["message"]="Sorry you couldnt make it!"
            returninfo["check"]="success"



        response=JsonResponse(returninfo)
        return response

class UserPage(TemplateView):
    template_name = 'orange/userpage.html'

    def get(self,request,slug):

        theuser=User.objects.get(email=self.kwargs.get("slug"))

        languagecookie="de"
        try:
            languagecookie=request.COOKIES["language"]
        except:
            pass
        else:
            pass
        finally:
            pass

        args={"theuser":theuser,"navlang":languagedic[languagecookie]["nav"]}
        return render(request,self.template_name,args)

class SendEmail(TemplateView):
    template_name = 'orange/profile.html'
    def post(self,request):

        decodedword=json.loads(request.body.decode('ascii'))
        typeoption=decodedword["type"]
        nameoption=decodedword["name"]
        sub=decodedword["sub"]
        head=decodedword["head"]
        bod=decodedword["bod"]

        returninfo={
            "message":"just checking",
            "check":""
        }

        if typeoption=="all":
            text_content = render_to_string(
                "orange/email.txt",
                context={"message": bod,"fromtext":head},
            )

            # Secondly, render the HTML content.
            html_content = render_to_string(
                "orange/emailtemplate.html",
                context={"message": bod,"fromtext":head},
            )

            # Then, create a multipart email instance.
            msg = EmailMultiAlternatives(
                sub,
                text_content,
                "kuchtagary1@gmail.com",
                [request.user.email],
                headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
            )

            # Lastly, attach the HTML content to the email instance and send.
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # send_mail('homepage email',"Testing",settings.EMAIL_HOST_USER,['kuchtagary1@gmail.com'],fail_silently=False)

        if typeoption=="club":
            None

        if typeoption=="event":
            None




        response=JsonResponse(returninfo)
        return response

class EmailTemplate(TemplateView):
    template_name= 'orange/emailtemplate.html'
    def get(self, request):

        args = {"message":"hihi","fromtext":"the messege is from Gary"}
        return render(request,self.template_name,args)
