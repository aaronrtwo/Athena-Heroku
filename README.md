# Normal Athena + Info

If you want to use normal Athena go to this link: https://github.com/EthanC/Athena

Athena is a utility which generates the current Fortnite Item Shop into a stylized image and shares it on Twitter.

As seen on [@FNMasterCom](https://twitter.com/FNMasterCom/status/1197666123078160386?s=20)...

<p align="center">
    <img src="https://i.imgur.com/YXoesjJ.png" width="650px" draggable="false">
</p>

## Requirements

- [Python 3.7](https://www.python.org/downloads/)
- [Requests](http://docs.python-requests.org/en/master/user/install/)
- [coloredlogs](https://pypi.org/project/coloredlogs/)
- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)
- [python-twitter](https://github.com/bear/python-twitter#installing)

A [Fortnite-API API Key](https://fortnite-api.com/profile) is required to obtain the Item Shop data, [Twitter API credentials](https://developer.twitter.com/en/apps) are required to Tweet the image.

## Usage

Open `configuration_example.json` in your preferred text editor, fill the configurable values. Once finished, save and rename the file to `configuration.json`.

- `delayStart`: Set to `0` to begin the process immediately
- `language`: Set the language for the Item Shop data ([Supported Languages](https://fortnite-api.com/documentation))
- `supportACreator`: Leave blank to omit the Support-A-Creator tag section of the Tweet
- `twitter`: Set `enabled` to `false` if you wish for `itemshop.png` to not be Tweeted

Edit the images found in `assets/images/` to your liking, avoid changing image dimensions for optimal results.

Athena is designed to be ran using a scheduler, such as [cron](https://en.wikipedia.org/wiki/Cron).

```
python itemshop.py
```

## Credits

- Item Shop data provided by [Fortnite-API](https://fortnite-api.com/)
- Burbank font property of [Adobe](https://fonts.adobe.com/fonts/burbank)
- Luckiest Guy font property of [Google](https://fonts.google.com/specimen/Luckiest+Guy)

# Heroku Athena

I have made this a super simple process of setting up.

1. You will need to signup to Heroku (if you are already signed up to heroku skip this step)
2. You will need to Fork this project if on mobile, if on PC download the zip and make it your own project
3. Next you will need to hook up this project to Heroku

And your all set!
If you want to setup the configuration.json go follow this tutorial: https://www.youtube.com/watch?v=n-178e7HWFs&ab_channel=Fevers
if you want to make the itemshop and send it to twitter press the button "More", then type in this command: python itemshop.py. And it will send it towards your twitter. I will not provide any help.
