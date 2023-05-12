from pyVoIP.VoIP import VoIPPhone, InvalidStateError, CallState
import time
import wave

def answer(call):
    try:
        f = wave.open('noandrey.wav', 'rb')
        frames = f.getnframes()
        data = f.readframes(frames)
        f.close()

        call.answer()
        call.write_audio(data)

        while call.state == CallState.ANSWERED:
            dtmf = call.get_dtmf()
            if dtmf == "1":
                # Do something
                call.hangup()
            elif dtmf == "2":
                # Do something else
                call.hangup()
            time.sleep(0.1)
    except InvalidStateError:
        pass
    except:
        call.hangup()

if __name__ == '__main__':
    phone = VoIPPhone(server="192.168.88.19", port=int("5060"), username="1111", password="6cce551bb0828b587304ce07837111bf", myIP="10.10.20.67", callCallback=answer)
    phone.start()
    input('Press enter to disable the phone')
    phone.stop()


