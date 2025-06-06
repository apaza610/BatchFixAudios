# edita audio track para 1 solo video (Originalmente era batch para varios)

import os, sys, ffmpeg

# print("enter the tutorial folder path: ")
# PATHTUTORIAL = input()

if sys.platform == 'win32':
    print("pipe-test.py, running on windows")
    TONAME = '\\\\.\\pipe\\ToSrvPipe'
    FROMNAME = '\\\\.\\pipe\\FromSrvPipe'
    EOL = '\r\n\0'
else:
    print("pipe-test.py, running on linux or mac")
    TONAME = '/tmp/audacity_script_pipe.to.' + str(os.getuid())
    FROMNAME = '/tmp/audacity_script_pipe.from.' + str(os.getuid())
    EOL = '\n'

print("Write to  \"" + TONAME +"\"")
if not os.path.exists(TONAME):
    print(" ..does not exist.  Ensure Audacity is running with mod-script-pipe.")
    sys.exit()

print("Read from \"" + FROMNAME +"\"")
if not os.path.exists(FROMNAME):
    print(" ..does not exist.  Ensure Audacity is running with mod-script-pipe.")
    sys.exit()

print("-- Both pipes exist.  Good.")

TOFILE = open(TONAME, 'w')
print("-- File to write to has been opened")
FROMFILE = open(FROMNAME, 'rt')
print("-- File to read from has now been opened too\r\n")

def send_command(command):
    """Send a single command."""
    print("Send: >>> \n"+command)
    TOFILE.write(command + EOL)
    TOFILE.flush()

def get_response():
    """Return the command response."""
    result = ''
    line = ''
    while True:
        result += line
        line = FROMFILE.readline()
        if line == '\n' and len(result) > 0:
            break
    return result

def do_command(command):
    """Send one command, and return the response."""
    send_command(command)
    response = get_response()
    print("Rcvd: <<< \n" + response)
    return response

def aplicar_efectos(mp4file):
    mp3Nuevo = mp4file.replace(".mp4","NEW.mp3")
    do_command('Import2: Filename=' + mp4file)
    do_command('SelectAll:')
    do_command('Normalize:')
    do_command('Limiter: thresh=-5')
    do_command('Compressor: Threshold=-20')
    do_command('Amplify: Amplification=5.0')
    do_command('Normalize:')
    # do_command('Noise:')
    do_command('Export2: Filename=' + mp3Nuevo)
    do_command('RemoveTracks:')
    # do_command('SetPreference: Name=GUI/Theme Value=classic Reload=1')

    mp3file = mp4file.replace(".mp4","NEW.mp3")
    mp4temp = mp4file.replace(".mp4","OLD.mp4")
    mivideo = ffmpeg.input(mp4file)
    miaudio = ffmpeg.input(mp3file)
    salida = ffmpeg.output(miaudio, mivideo.video, mp4temp, shortest=None, vcodec='copy').run()
    os.remove(mp4file)
    os.remove(mp3file)
    os.rename(mp4temp,mp4file)

# lMP4s = []
# def catch_mp4s():
#     for root,dirs,files in os.walk(PATHTUTORIAL):       #D:\\borrar\\MiTutorial
#         for filename in files:
#             if os.path.splitext(filename)[1] == '.mp4':
#                 elpath = os.path.join(root,filename)
#                 if " " in elpath:
#                     print("------Error: nombres no pueden contener espacios------")
#                     break
#                 lMP4s.append(elpath)
#                 aplicar_efectos(elpath)
# catch_mp4s()
