from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import pytz


def task1(request):
    context = {}
    return render(request, 'task1.html', context)

def task2(request):
    context = {}
    return render(request, 'task2.html', context)

def task3(request):
    context = {}
    return render(request, 'task3.html', context)

def last5games(request):

    if request.method == 'GET':

        json = { 
            'baseball':[]
        }   


        myEvents = ["myEvent0 1:00am", "myEvent1 10:30am", "myEvent2 12:00pm", "myEvent3 1:30pm", "myEvent4 5:00 pm"];
        teams = ["San Francisco Giants", "Los Angeles Dodgers", "Colorado Rockies", "San Diego Padres", "Arizona Diamondbacks"];

        sfggames = []
        sfgstart = []
        sfgend = []
        ladgames = []
        ladstart = []
        ladend = []
        sdgames = []
        sdstart = []
        sdend = []
        colgames = []
        colstart = []
        colend = []

        arigames = []
        aristart = []
        ariend = []

        allgames = []
        allstarttimes = []
        allendtimes = []

        sfg = ({'game':'4/28 vs Nationals @3:30 pm'})#, {'start' : '14:30'}, {'end' : '17:30'})

        sfggames.append(sfg)
        sfg = ({'game':'4/29 vs Rockies @5:00 pm'})#, {'start' : '16:00'}, {'end' : '19:37'})
        sfggames.append(sfg)
        sfg = ({'game':'4/30 vs Red Sox @6:00 am'})#, {'start' : '6:00'}, {'end' : '9:42'})
        sfggames.append(sfg)
        sfg = ({'game':'5/1 vs Dodgers @5:00 pm'})#, {'start' : '16:00'}, {'end' : '19:07'})
        sfggames.append(sfg)
        sfg = ({'game':'5/2 vs Marlins @10:00 am'})#, {'start' : '10:00'}, {'end' : '13:33'})
        sfggames.append(sfg)

        allgames.append(sfggames)

        lad = ({'game':'4/28 vs Reds @1:00 pm'})#, {'start' : '13:00'}, {'end' : '16:21'})
        start = ({'start' : '13:00'})
        end = ({'end' : '16:21'})
        ladgames.append(lad)
        ladstart.append(start)
        ladend.append(end)
        lad = ({'game':'4/29 vs Yankees @5:00 pm'})#, {'start' : '16:00'}, {'end' : '19:22'})
        start = ({'start' : '16:00'})
        end = ({'end' : '19:22'})
        ladgames.append(lad)
        ladstart.append(start)
        ladend.append(end)
        lad = ({'game':'4/30 vs Athletics @7:00 am'})#, {'start' : '7:00'}, {'end' : '10:57'})
        start = ({'start' : '7:00'})
        end = ({'end' : '10:57'})
        ladgames.append(lad)
        ladstart.append(start)
        ladend.append(end)
        lad = ({'game':'5/1 vs Giants @5:00 pm'})#, {'start' : '16:00'}, {'end' : '19:07'})
        start = ({'start' : '16:00'})
        end = ({'end' : '19:07'})
        ladgames.append(lad)
        ladstart.append(start)
        ladend.append(end)
        lad = ({'game':'5/2 vs Rays @12:00 pm'})#, {'start' : '12:00'}, {'end' : '15:11'})
        start = ({'start' : '12:00'})
        end = ({'end' : '15:11'})
        ladgames.append(lad)
        ladstart.append(start)
        ladend.append(end)

        allgames.append(ladgames)
        allstarttimes.append(ladstart)
        allendtimes.append(ladend)

        sd = ({'game':'4/28 vs Marlins @9:00 pm'})#, {'start' : '21:00'}, {'end' : '23:37'})
        sdgames.append(sd)
        sd = ({'game':'4/29 vs Astros @9:00 am'})#, {'start' : '9:00'}, {'end' : '12:55'})
        sdgames.append(sd)
        sd = ({'game':'4/30 vs Rangers @11:00 am'})#, {'start' : '11:00'}, {'end' : '14:12'})
        sdgames.append(sd)
        sd = ({'game':'5/1 vs Phillies @2:00 pm'})#, {'start' : '14:00'}, {'end' : '17:32'})
        sdgames.append(sd)
        sd = ({'game':'5/2 vs Cubs @4:00 pm'})#, {'start' : '16:00'}, {'end' : '19:21'})
        sdgames.append(sd)

        allgames.append(sdgames)

        col = ({'game':'4/28 vs Cubs @1:00 pm'})#, {'start' : '13:00'}, {'end' : '16:20'})
        colgames.append(col)
        col = ({'game':'4/29 vs Phillies @5:00 am'})#, {'start' : '5:00'}, {'end' : '8:47'})
        colgames.append(col)
        col = ({'game':'4/30 vs Blue Jays @10:00 am'})#, {'start' : '10:00'}, {'end' : '13:44'})
        colgames.append(col)
        col = ({'game':'5/1 vs White Sox @3:00 pm'})#, {'start' : '15:00'}, {'end' : '18:09'})
        colgames.append(col)
        col = ({'game':'5/2 vs Pirates @5:00 pm'})#, {'start' : '17:00'}, {'end' : '19:56'})
        colgames.append(col)

        allgames.append(colgames)

        ari = ({'game':'4/28 vs Pirates @2:00 pm'})#, {'start' : '14:00'}, {'end' : '17:11'})
        arigames.append(ari)
        ari = ({'game':'4/29 vs Cardinals @8:00 am'})#, {'start' : '8:00'}, {'end' : '11:21'})
        arigames.append(ari)
        ari = ({'game':'4/30 vs Mets @10:30 am'})#, {'start' : '10:30'}, {'end' : '12:54'})
        arigames.append(ari)
        ari = ({'game':'5/1 vs Braves @1:00 pm'})#, {'start' : '13:00'}, {'end' : '16:07'})
        arigames.append(ari)
        ari = ({'game':'5/2 vs Brewers @9:00 pm'})#, {'start' : '21:00'}, {'end' : '23:37'})
        arigames.append(ari)

        allgames.append(arigames)
#games[0] = ['hello', 'darkness']
#        games[1] = ['my, old']
#        games[2] = ['bye, old']
#        games[3] = ['try, old']
#        games[4] = ['lie, old']
        for i in range(len(teams)):
          json['baseball'].append({
              'event' : myEvents[i],
	      'team' : teams[i],
	      'games' : allgames[i],
	      'id' : ({
		  'one' : 'this is the first one',
		  'two': 'this is the second one'
		  })
          })
        return JsonResponse(json)
        # pylint: disable=no-member
        """cal_lists = service.calendarList().list().execute()
        tz = pytz.timezone('America/Los_Angeles')
        today = datetime.now(tz).date()
        for entry in cal_lists['items']:
            json['calendarLists'].append({
                'name': entry['summary'].split('@')[0],
                'primary': 'primary' in entry and entry['primary'],
                # pylint: disable=no-member
                'events': (
                    service
                    .events()
                    .list(
                        calendarId=entry['id'],
                        timeMin=tz.localize(datetime.combine(today, time.min), is_dst=None).isoformat(),
                        timeMax=tz.localize(datetime.combine(today, time.max), is_dst=None).isoformat(),
                        showDeleted=False,
                        singleEvents=True,
                        orderBy='startTime',
                        maxResults=10
                    )   
                    .execute()
                )   
            })  
    """
    return HttpResponseBadRequest('Invalid Method')


def todaysgames(request):

    if request.method == 'GET':

        json = { 
            'baseball':[]
        }   


        myEvents = ["myEvent0 1:00am", "myEvent1 10:30am", "myEvent2 12:00pm", "myEvent3 1:30pm", "myEvent4 5:00 pm"];
        divisions = ["NL East", "NL West", "NL Central", "AL East", "AL West"]
#divisions = ["NL East", "NL West", "NL Central", "AL East", "AL West", "AL Central"];

        nlegames = []
        nlestart = []
        nleend= []

        nlwgames = []
        nlwstart = []
        nlwend= []

        nlcgames = []
        nlcstart = []
        nlcend= []

        alegames = []
        alestart = []
        aleend= []

        alwgames = []
        alwstart = []
        alwend= []

        alcgames = []
        alcstart = []
        alcend= []

        allgames = []
        allstarts = []
        allends = []

        nle = ({'game':'Diamonbacks vs Nationals @3:30 pm - 5:30 pm'})#, {'start' : '14:30'}, {'end' : '17:30'})
        nlestart.append({'start' : '15:30'})
        nleend.append({'end' : '17:30'})
        nlegames.append(nle)

        nle = ({'game':'Mets vs Rockies @5:00 pm - 7:37 pm'})#, {'start' : '16:00'}, {'end' : '19:37'})
        nlestart.append({'start' : '17:00'})
        nleend.append({'end' : '19:37'})
        nlegames.append(nle)

        nle = ({'game':'Braves vs Red Sox @6:00 am - 9:42 am'})#, {'start' : '6:00'}, {'end' : '9:42'})
        nlestart.append({'start' : '6:00'})
        nleend.append({'end' : '9:42'})
        nlegames.append(nle)

        nle = ({'game':'Phillies vs Dodgers @5:00 pm - 7:07 pm'})#, {'start' : '16:00'}, {'end' : '19:07'})
        nlestart.append({'start' : '17:00'})
        nleend.append({'end' : '19:07'})
        nlegames.append(nle)

        nle = ({'game':'Padres vs Marlins @10:00 am - 1:33 pm'})#, {'start' : '10:00'}, {'end' : '13:33'})
        nlestart.append({'start' : '10:00'})
        nleend.append({'end' : '13:33'})
        nlegames.append(nle)

        allgames.append(nlegames)
        allstarts.append(nlestart)
        allends.append(nleend)

        nlw = ({'game':'Giants vs Reds @1:00 pm - 4:21 pm'})#, {'start' : '13:00'}, {'end' : '16:21'})
        nlwstart.append({'start' : '13:00'})
        nlwend.append({'end' : '16:21'})
        nlwgames.append(nlw)

        nlw = ({'game':'Phillies vs Dodgers @5:00 pm - 7:07 pm'})#, {'start' : '16:00'}, {'end' : '19:07'})
        nlwstart.append({'start' : '17:00'})
        nlwend.append({'end' : '19:07'})
        nlwgames.append(nlw)

        nlw = ({'game':'Diamonbacks vs Nationals @3:30 pm - 5:30 pm'})#, {'start' : '14:30'}, {'end' : '17:30'})
        nlwstart.append({'start' : '15:30'})
        nlwend.append({'end' : '17:30'})
        nlwgames.append(nlw)

        nlw = ({'game':'Mets vs Rockies @5:00 pm - 7:37 pm'})#, {'start' : '16:00'}, {'end' : '19:37'})
        nlwstart.append({'start' : '17:00'})
        nlwend.append({'end' : '19:37'})
        nlwgames.append(nlw)

        nlw = ({'game':'Padres vs Marlins @10:00 am - 1:33 pm'})#, {'start' : '10:00'}, {'end' : '13:33'})
        nlwstart.append({'start' : '10:00'})
        nlwend.append({'end' : '13:33'})
        nlwgames.append(nlw)

        allgames.append(nlwgames)
        allstarts.append(nlwstart)
        allends.append(nlwend)

        nlc = ({'game':'Giants vs Reds @1:00 pm - 4:21 pm'})#, {'start' : '13:00'}, {'end' : '16:21'})
        nlcstart.append({'start' : '13:00'})
        nlcend.append({'end' : '16:21'})
        nlcgames.append(nlc)

        nlc = ({'game':'Brewers vs Astros @9:00 am - 12:55 pm'})#, {'start' : '9:00'}, {'end' : '12:55'})
        nlcstart.append({'start' : '9:00'})
        nlcend.append({'end' : '12:55'})
        nlcgames.append(nlc)

        nlc = ({'game':'Cubs vs Rangers @11:00 am - 2:12 pm'})#, {'start' : '11:00'}, {'end' : '14:12'})
        nlcstart.append({'start' : '11:00'})
        nlcend.append({'end' : '14:12'})
        nlcgames.append(nlc)

        nlc = ({'game':'Pirates vs Orioles @2:00 pm - 5:32 pm'})#, {'start' : '14:00'}, {'end' : '17:32'})
        nlcstart.append({'start' : '14:00'})
        nlcend.append({'end' : '17:32'})
        nlcgames.append(nlc)

        nlc = ({'game':'Cardinals vs Mariners @4:00 pm - 7:21 pm'})#, {'start' : '16:00'}, {'end' : '19:21'})
        nlcstart.append({'start' : '16:00'})
        nlcend.append({'end' : '19:21'})
        nlcgames.append(nlc)

        allgames.append(nlcgames)
        allstarts.append(nlcstart)
        allends.append(nlcend)

        ale = ({'game':'Yankees vs White Sox @1:00 pm - 4:20 pm'})#, {'start' : '13:00'}, {'end' : '16:20'})
        alestart.append({'start' : '13:00'})
        aleend.append({'end' : '16:20'})
        alegames.append(ale)

        ale = ({'game':'Braves vs Red Sox @6:00 am - 9:42 am'})#, {'start' : '6:00'}, {'end' : '9:42'})
        alestart.append({'start' : '6:00'})
        aleend.append({'end' : '9:42'})
        alegames.append(ale)

        ale = ({'game':'Twins vs Blue Jays @10:00 am - 1:44 pm'})#, {'start' : '10:00'}, {'end' : '13:44'})
        alestart.append({'start' : '10:00'})
        aleend.append({'end' : '13:44'})
        alegames.append(ale)

        ale = ({'game':'Pirates vs Orioles @2:00 pm - 5:32 pm'})#, {'start' : '14:00'}, {'end' : '17:32'})
        alestart.append({'start' : '14:00'})
        aleend.append({'end' : '17:32'})
        alegames.append(ale)

        ale = ({'game':'Rays vs Indians @5:00 pm - 7:56 pm'})#, {'start' : '17:00'}, {'end' : '19:56'})
        alestart.append({'start' : '17:00'})
        aleend.append({'end' : '19:56'})
        alegames.append(ale)

        allgames.append(alegames)
        allstarts.append(alestart)
        allends.append(aleend)

        alw = ({'game':'Cardinals vs Mariners @4:00 pm - 7:21 pm'})#, {'start' : '16:00'}, {'end' : '19:21'})
        alwstart.append({'start' : '16:00'})
        alwend.append({'end' : '19:21'})
        alwgames.append(alw)

        alw = ({'game':'Brewers vs Astros @9:00 am - 12:55 pm'})#, {'start' : '9:00'}, {'end' : '12:55'})
        alwstart.append({'start' : '9:00'})
        alwend.append({'end' : '12:55'})
        alwgames.append(alw)

        alw = ({'game':'Athletics vs Tigers @10:30 am - 12:54 pm'})#, {'start' : '10:30'}, {'end' : '12:54'})
        alwstart.append({'start' : '10:30'})
        alwend.append({'end' : '12:54'})
        alwgames.append(alw)

        alw = ({'game':'Cubs vs Rangers @11:00 am - 2:12 pm'})#, {'start' : '11:00'}, {'end' : '14:12'})
        alwstart.append({'start' : '11:00'})
        alwend.append({'end' : '14:12'})
        alwgames.append(alw)

        alw = ({'game':'Angels vs Royals @9:00 pm - 11:37 pm'})#, {'start' : '21:00'}, {'end' : '23:37'})
        alwstart.append({'start' : '21:00'})
        alwend.append({'end' : '23:37'})
        alwgames.append(alw)

        allgames.append(alwgames)
        allstarts.append(alwstart)
        allends.append(alwend)

        for i in range(len(divisions)):
          json['baseball'].append({
              'event' : myEvents[i],
	      'team' : divisions[i],
	      'games' : allgames[i],
	      'starttimes' : allstarts[i],
	      'endtimes' : allends[i],
	      'id' : ({
		  'one' : 'this is the first one',
		  'two': 'this is the second one'
		  })
          })
        return JsonResponse(json)
    return HttpResponseBadRequest('Invalid Method')



# Create your views here.
