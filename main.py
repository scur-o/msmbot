import pyautogui
import time
# ------------------ Buttons ------------------ #


print(pyautogui.position())
# ------------------ Bot ------------------ #
while True:
    if pyautogui.locateOnScreen('images/accept.png', confidence=0.7):
        pyautogui.click(pyautogui.locateOnScreen('images/accept.png', confidence=0.7))
        time.sleep(0.3)
    elif pyautogui.locateOnScreen('images/skip_dialogue.png', confidence=0.7):
        pyautogui.click(230, 254)
    elif pyautogui.locateOnScreen('images/confirm.png', confidence=0.7):
        pyautogui.click(pyautogui.locateOnScreen('images/confirm.png', confidence=0.7))
        time.sleep(0.3)
    elif pyautogui.locateOnScreen('images/complete.png', confidence=0.7):
        pyautogui.click(pyautogui.locateOnScreen('images/complete.png', confidence=0.6))
    elif pyautogui.locateOnScreen('images/complete2.png', confidence=0.7):
        pyautogui.click(pyautogui.locateOnScreen('images/complete2.png', confidence=0.6))
    elif pyautogui.locateOnScreen('images/quest_complete.png', confidence=0.7):
        pyautogui.click(pyautogui.locateOnScreen('images/claim_reward.png', confidence=0.7))
    elif pyautogui.locateOnScreen('images/auto_assign.png', confidence=0.7):
        pyautogui.click(pyautogui.locateOnScreen('images/auto_assign.png', confidence=0.7))
    # elif pyautogui.locateOnScreen('images/go_now.png', confidence=0.7):
    #     pyautogui.click(pyautogui.locateOnScreen('images/go_now.png', confidence=0.7))
    elif pyautogui.locateOnScreen('images/auto_quest_off.png', confidence=0.56):
        pyautogui.click(230, 254)
        time.sleep(3)
    elif pyautogui.locateOnScreen('images/auto_quest_on2.png', confidence=0.7):
        pyautogui.click(230, 254)
        time.sleep(3)
    elif pyautogui.locateOnScreen('images/available_to_start.png', confidence=0.7):
        pyautogui.click(425, 603)
    # elif pyautogui.locateOnScreen('images/last.png', confidence=0.7):
    #     pyautogui.click(pyautogui.locateOnScreen('images/last.png', confidence=0.7))
    # else:
    #     pyautogui.click(230, 254)
    #     time.sleep(1)








