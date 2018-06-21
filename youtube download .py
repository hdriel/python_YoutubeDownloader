import pyperclip
import subprocess as sp
import os

def printInfo(data_list):
    ## create Regular Expression
    import re
    import pprint

    play_regex          = re.compile(r'\[youtube:playlist\] playlist ([\w ]+): Downloading [\d]+ videos')
    down_regex          = re.compile(r'\[download\] Downloading video [\d]+ of [\d]+')
    info_regex          = re.compile(r'\[download\] [\d]+% of ([\d]+.[\d]*\w\w\w) in \d\d:\d\d')
    name_regex          = re.compile(r'\[download\] Destination: ([\w: -/\\.—]+)')

    ## get data
    text                = '\n'.join(data_list)
    matches_down        = down_regex.findall(text)
    matches_size        = info_regex.findall(text)
    matches_name        = name_regex.findall(text)
    matches_play        = play_regex.findall(text)
        
    if(len(matches_size) == 0 and len(matches_name) == 0):
        print('Seems you have allready downloaded thes videos!')
        os.system("pause")
        exit(0)
        
    if(len(matches_size) != len(matches_name)):            
        print('cannot download data!')
        print('see following data I get:')
        print('data_list\n\t')
        pprint.pprint(text)
        print('matches_down\n\t', matches_down)
        print('matches_size\n\t', matches_size)
        print('matches_name\n\t', matches_name)
        print('matches_play\n\t', matches_play)
        os.system("pause")
        exit(0)

    if(len(matches_name) > 0) : name_first = matches_name[0]
    else : name_first = ''
    
    ## order relevant data for printing to user
    if(len(matches_name) == 1 or len(matches_down) == 1 or len(matches_size) == 1):
        res = 'Download One Video+ \n' + ('-')*100 + '\n'
        if(len(name_first) > 0 and 'NA' in name_first.split('\\')):
            idx  = name_first.rfind('NA')
            path = name_first[:idx]
        else:
            idx  = -1
            path = ''
    elif(len(matches_play) > 0 and len(name_first) > 0):
        playlist_name = matches_play[0]
        res  = 'Playlist: ' + playlist_name + '\n' + ('-')*100 + '\n'
        idx  = name_first.find(playlist_name)
        idx  = idx + len(playlist_name)
        path = name_first[:idx]
    else:
        res  = ''
        idx  = 0
        path = ''
        
            
    N = len(matches_down)
    if N == 0: N = len(matches_size)
    if N == 0: N = len(matches_name)
    if N == 0: N = len(matches_play)

    print(res)
    for i in range(len(matches_size)):
        res = ''
        if(i < len(matches_down)): res += matches_down[i] + ' | '
        if(i < len(matches_size)): res += ' ('+ matches_size[i]+') '
        if(i < len(matches_name)):
            matches_name[i] = matches_name[i].replace('—', '-')
            res += matches_name[i][idx+1:]
        #res += '\n'
        print(res)

    res = ''
    print()
    if(len(path) == 0 and len(matches_name) > 0) : path = matches_name[0][:matches_name[0].rfind('\\')+1]
    res += ('-')*100 + '\n\nPlaced in folder: ' + path # + '\n'
    print(res)
    
    ## print to user the information
    if(len(path)>0):
        path = path.replace('\\x97', '—')
        print('\nOpens a folder that contains the files\n\n\n'); os.startfile(path)



def getYoutubeScript(url = None, path = None):
    ## can get path from the clipboard , after you copy the youtube url link
    def isPlaylist(url):
        return url.find('list') >= 0
    
    ## define url line
    if(url is None): playlist_url = pyperclip.paste()
    else:            playlist_url = url
    if(len(playlist_url) == 0  or playlist_url.startswith('https') == False):
        print('You need first copy the youtube url , and then run this script!\n(Should start with \'https\'...)')
        os.system("pause")
        exit(0)
    if len(playlist_url) > 0: url = playlist_url.replace("&" , '"&"')
    else:
        print('You need insert url of playlist in youtube to download it!');
        os.system("pause");
        exit(0)
    
    ## define path download
    default_path = r"'~/Desktop"
    if(path is not None): path = "'" + path
    else: path = default_path
    
    if len(path) > 0:        
        if(isPlaylist(url)): path = path + r"/Youtube Downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'"
        else:                path = path + r"/Youtube Downloads/%(title)s.%(ext)s'"
        path = r'-o ' + path
    youtube_dl = r'youtube-dl ' + path + ' '
    
    ## composite script from path and url
    script = youtube_dl + url
    return script


def runInPowerShell(url = None, path = None, path_PowerShell = None):    
    ## get power shell path and name program
    if(path_PowerShell is None):
        path_PowerShell = 'C:\Windows\System32\WindowsPowerShell\v1.0'
    path_PowerShell     = path_PowerShell.replace('\\', '\\')
    path_PowerShell     = path_PowerShell.replace('\v', '\\v')
    program_PowerShell  = 'powershell.exe'
    direct              = os.path.join(path_PowerShell,program_PowerShell)
    script              = getYoutubeScript(url, path = os.path.abspath(''))
    
    ## add command to run in cmd
    cmd_args = []
    cmd_args.append(direct) # run the program 'powershell.exe'
    cmd_args.append(script) # run the youtube_dl_script
    
    ## run on PS windows without printing data on it
    try:
        print('Please wait until the program will finished\nThen you see the result, or Error showed up if this happened...\n')
        print('Runs the following command in Powershell:\n\n  ', script, end = '\n\n')
        output = sp.check_output(cmd_args).decode('utf-8', errors="backslashreplace").split('\n') # run the cmd, and get the output after finished
        print('...\n')
        printInfo(output)
    except Exception as e:
        print('There is some error in runnig in powershell the following command:\n')
        print('Error: ' , e)
    os.system("pause")    

runInPowerShell()





