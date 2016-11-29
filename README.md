# Beep "Berry" Boop

Make some *Beep Boop* with your Raspberry and your Piazzo-Beeper

## Who is Berry ?

Berry is a Python module which can be used to sing your Raspberry. With that, you can transform it into a BB-8¹ ! Or you can make some Christmas songs for your Christmas tree. The only thing that you'll need is a Piazzo-Beeper and some wire to connect it on your Raspberry


¹ Bearing and Lighter not included

## How to use it ?

First, you will need the `RPi.GPIO` library ! It is included with the Raspbian OS. Add the library into your project and voilà, you can use it ! For some examples, look at the file `beep.py` in the folder `Examples`. Basically, you'll need to create a BeepBoop object and give it the pin where the beeper is connected. Then you can use functions like `beep`, `note` or `song`.

## License

TL:DR -> MIT

You can do whatever you want as long as you include the original copyright and license notice in any copy of the software/source. For more information, look at the `LICENSE` file.
