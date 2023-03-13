Python code that will record all the keystrokes and will send them to discord webhook once the keystroke limit hit 500.

It will also check if whatsApp app is running or not, and if it is running (even in the backgroud) it will take screenshot after every 10 seconds and send them to discord webhook and if whatsapp is not running it will just wait and keep on checking after every 5 seconds if whatsapp is working or not.

This code will auto add itself to startup folder, so even if you restart your laptop it will work in the background

Make sure to Replace Discord webhook on line 37 and line 66 with your actual discord webhook (Put your webook between " ")

You have to run your IDE as administrator to run this code otherwise it will print error of permission denied. If you don't want to do that then change the location on line 62 and 39. Choose any other drive

You can increase the character limit after which it should send keystrokes to discord webhook, change it on line 30 (default is 500)