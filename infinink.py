#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os
import socket
import logging
import epd2in13b_V3
import time
from PIL import Image,ImageDraw,ImageFont

try:
    # Initialise the e-ink display
    epd = epd2in13b_V3.EPD()
    epd.init()
    epd.Clear()
    time.sleep(1)

    # Create the two images to display
    HBlackImage = Image.new('1', (epd.height, epd.width), 255)
    HRedImage = Image.new('1', (epd.height, epd.width), 255)

    # Get a drawing context
    drawblack = ImageDraw.Draw(HBlackImage)
    drawred = ImageDraw.Draw(HRedImage)
    
    # Scale the bmp and calculate offset to center it
    TextBMP = Image.open('Infineon_grayscale_text.bmp')
    SwooshBMP = Image.open('Infineon_grayscale_swoosh.bmp')
    TextBMP = TextBMP.resize((epd.height, epd.width))
    SwooshBMP = SwooshBMP.resize((epd.height, epd.width))

    # Paste the bmp into the image
    HBlackImage.paste(TextBMP, (0, 0))
    HRedImage.paste(SwooshBMP, (0, 0))

    # Display the images on the e-ink display
    epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))
    time.sleep(2)

    #Power off the display
    epd.sleep()
    epd.Dev_exit()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13b_V3.epdconfig.module_exit()
    exit()

