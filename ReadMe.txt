1) The folder scanner GUI consists of all the files required to run the GUI.
2) The subfolder windows consists of all the different screens and their respective python codes that are used in the GUI.
3) The GUI can be started either using the vbscript file, "abc" or directly using the pyhton code, "GUInoCMD".
	a) If you start the GUI using the "GUI.py" file a cmd window will also pop up that would track the current state of the code.
	b) The "GUInoCMD.pyw" is the same file but it prevents the cmd window from starting.
4) The GUI consists of a total of 6 screens:
	a) Homepage
	b) Mock Payment Gateway
	c) Instructions
	d) Scanning window
	e) Feedback and print
	f) Thank you screen
5) To quit the GUI at any instance close the window using the cross button.
6) The complete GUI has been made on PyQt to enable the automation process to work along in the backend of the GUI.

# Homepage

1) The homepage consists of a heading inserted in QLabel named title1.
2) An image has been added to improve the look of the GUI. It has been inserted in the QLabel named Im1.
3) A QPushButton with text "Enter" named btn1 has been used to link the homepage to the payment gateway. It closes the current homepage and opens the payment gateway.

# Payment Gateway

1) The gateway page consists of a heading inserted in QLabel named title2.
2) An image has been inserted in QLabel named Im2, where a payment gateway could be inserted in the future.
3) Two QPushButtons namely btn2 and btn3 with text "Proceed to pay" and "Cancel" respectively have been inserted in the form. btn2 links the gateway screen to the instructons screen while btn3 links it back to the homepage. On opening the new window using the buttons the current window is closed.  

# Instructions

1) The instructions window consists of a heading inserted in QLabel named title3.
2) A set of instructions has been added in a text named text1.
3) A check box named check1 ensures that the user has read and understood the above stated set of instructions.
4) Two QPushButtons namely btn4 and btn5 with text "Proceed" and "Cancel" respectively have been nserted in the form. btn4 links the instructions page to the scanning window while btn5 links the page back to the homepage. In order for the btn4 to work the check box, check1 has to be ticked or selected.

# Scanning window

1) This window consists of a heading in QLabel named title4.
2) The scanning window remains active for 10 seconds which is given to the user to adjust himself in a comfortable and proper position for scan.
3) It consists of two images in QLabel namely Im3 and Im4.

# Scanning

1) Once the scanning window closes, the touch screen is disabled. Skanect pops up and the scanning process begins using pyautogui.
2) Pyautogui uses image recognition to find the positions to click at in skanect. For this, it uses the various image files in the scanning GUI folder.
3) Once the scanning process is complete, a model of the scan is shown to the user and the feedback and print window pops up.

# Feedback and print

1) The feedback and print window consists of a heading in QLabel named title5.
2) A text message asking for feedback is present in QLabel named l1.
3) Radio buttons associated with the feedback print the rating in a text document named feedback.
4) Radio buttons are named r1, r2, r3, r4 and r5  for 1, 2, 3, 4 and 5 respectively.
5) The window consists of 3 QPushButtons named btn6, btn7 and btn8. btn6 links the page to the thank you page, btn7 links the page back to the instructions page and btn8 links the current window back to the homepage.

# Thank you screen

1) The thank you window consists of text "Thank you, visit again! named title6 in a QLabel.
2) The text "Our Team" is inserted in a QLabel named title7.
3) The text "The scan has been sent for printing. Please collect it from x room in y minutes" has been inserted in a label named l2.
4) The "Finish" QPushButton named btn9 links the thank you screen back to the homepage.