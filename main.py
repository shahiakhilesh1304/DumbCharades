import pygame
import random
import time
import sys
import math
import numpy as np

class WordDisplayApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Act Like You Feel")
        self.clock = pygame.time.Clock()
        self.is_fullscreen = False
        self.words = [
                                                ("Uttar Pradesh", "Agra: Taj Mahal and Kumbh Mela"),
                                                ("Uttar Pradesh", "Lucknow: Nawabi culture and Tunday Kababi"),
                                                ("Uttar Pradesh", "Gorakhpur: Famous Gorakhnath Temple"),
                                                ("Karnataka", "Bangalore: Richmond Circle and bustling city life"),
                                                ("Karnataka", "Mysore: Silk sarees and Mysore Palace"),
                                                ("Tamil Nadu", "Chennai: Temples of Madurai and Marina Beach"),
                                                ("Tamil Nadu", "Ooty: Scenic beauty and Nilgiri tea gardens"),
                                                ("Jammu and Kashmir", "Leh: Breathtaking landscapes and adventurous treks"),
                                                ("Jammu and Kashmir", "Jammu: Temples and Vaishno Devi pilgrimage"),
                                                ("Tamil Nadu", "Rameswaram: Sacred Ramanathaswamy Temple and Pamban Bridge"),
                                                ("Maharashtra", "Mumbai: Vada Pav and Bollywood"),
                                                ("Maharashtra", "Pune: Educational hub and Osho Ashram"),
                                                ("Rajasthan", "Jaipur: Desert safari and Hawa Mahal"),
                                                ("Rajasthan", "Jodhpur: Mehrangarh Fort and Blue City"),
                                                ("West Bengal", "Kolkata: Rosogolla and Howrah Bridge"),
                                                ("West Bengal", "Darjeeling: Tea gardens and Himalayan Railway"),
                                                ("Gujarat", "Ahmedabad: Dhokla and Kite flying festivals"),
                                                ("Gujarat", "Surat: Diamond cutting and Surati cuisine"),
                                                ("Uttarakhand", "Dehradun: Jim Corbett National Park and Rishikesh"),
                                                ("Uttarakhand", "Nainital: Naini Lake and Naina Devi Temple"),
                                                ("Kerala", "Kochi: Backwaters and Kathakali dance"),
                                                ("Kerala", "Thiruvananthapuram: Padmanabhaswamy Temple and Kovalam Beach"),
                                                ("Himachal Pradesh", "Shimla: Apple orchards and Rohtang Pass"),
                                                ("Himachal Pradesh", "Manali: Solang Valley and Hadimba Temple"),
                                                ("Madhya Pradesh", "Bhopal: Khajuraho temples and Bandhavgarh National Park"),
                                                ("Madhya Pradesh", "Indore: Street food and Lal Bagh Palace"),
                                                ("Assam", "Guwahati: Kamakhya Temple and Assam tea"),
                                                ("Assam", "Silchar: Barak Valley and Khasi culture"),
                                                ("Punjab", "Amritsar: Golden Temple and Patiala Peg"),
                                                ("Punjab", "Ludhiana: Industrial city and Punjabi cuisine"),
                                                ("Telangana", "Hyderabad: Charminar and Hyderabadi biryani"),
                                                ("Telangana", "Warangal: Kakatiya dynasty and Bhadrakali Temple"),
                                                ("Bihar", "Patna: Mahavir Mandir and Chhath Puja"),
                                                ("Bihar", "Gaya: Bodh Gaya and Vishnupad Temple"),
                                                ("Odisha", "Bhubaneswar: Lingaraj Temple and Udayagiri Caves"),
                                                ("Odisha", "Puri: Jagannath Temple and Konark Sun Temple"),
                                                ("Haryana", "Gurugram: Cyber Hub and Kingdom of Dreams"),
                                                ("Haryana", "Faridabad: Industrial city and Surajkund Crafts Mela"),
                                                ("Jharkhand", "Ranchi: Birsa Munda Stadium and Tribal culture"),
                                                ("Jharkhand", "Jamshedpur: Steel City and Jubilee Park"),
                                                ("Chhattisgarh", "Raipur: Bastar Dussehra and Chitrakoot Falls"),
                                                ("Chhattisgarh", "Bilaspur: Rice bowl of Chhattisgarh and Kanan Pendari Zoo"),
                                                ("Arunachal Pradesh", "Itanagar: Tawang Monastery and Ziro Music Festival"),
                                                ("Arunachal Pradesh", "Naharlagun: Ganga Lake and Polo Park"),
                                                ("Meghalaya", "Shillong: Living root bridges and Shillong Peak"),
                                                ("Meghalaya", "Tura: Garo Hills and Balpakram National Park"),
                                                ("Nagaland", "Kohima: Hornbill Festival and Naga tribes"),
                                                ("Nagaland", "Dimapur: Gateway to Nagaland and Diezephe Craft Village"),
                                                ("Manipur", "Imphal: Loktak Lake and Manipuri dance"),
                                                ("Manipur", "Thoubal: Floating islands and Phumdis"),
                                                ("Mizoram", "Aizawl: Blue Mountains and Chapchar Kut festival"),
                                                ("Mizoram", "Lunglei: Second largest city and Zobawk Sports Academy"),
                                                ("Tripura", "Agartala: Ujjayanta Palace and Tripuri cuisine"),
                                                ("Tripura", "Dharmanagar: Pineapple City and Rowa Wildlife Sanctuary"),
                                                ("Sikkim", "Gangtok: Gurudongmar Lake and Rumtek Monastery"),
                                                ("Sikkim", "Namchi: Siddheshwar Dham and Tendong Hill"),
                                                ("Goa", "Panaji: Feni and Dudhsagar Falls"),
                                                ("Goa", "Margao: Cultural hub and Colva Beach"),
                                                ("Uttar Pradesh", "Agra: Taj Mahal and Kumbh Mela"),
                                                ("Uttar Pradesh", "Lucknow: Nawabi culture and Tunday Kababi"),
                                                ("Uttar Pradesh", "Gorakhpur: Famous Gorakhnath Temple"),
                                                ("Karnataka", "Bangalore: Richmond Circle and bustling city life"),
                                                ("Karnataka", "Mysore: Silk sarees and Mysore Palace"),
                                                ("Tamil Nadu", "Chennai: Temples of Madurai and Marina Beach"),
                                                ("Tamil Nadu", "Ooty: Scenic beauty and Nilgiri tea gardens"),
                                                ("Jammu and Kashmir", "Leh: Breathtaking landscapes and adventurous treks"),
                                                ("Jammu and Kashmir", "Jammu: Temples and Vaishno Devi pilgrimage"),
                                                ("Tamil Nadu", "Rameswaram: Sacred Ramanathaswamy Temple and Pamban Bridge"),
                                                ("Maharashtra", "Mumbai: Vada Pav and Bollywood"),
                                                ("Maharashtra", "Pune: Educational hub and Osho Ashram"),
                                                ("Rajasthan", "Jaipur: Desert safari and Hawa Mahal"),
                                                ("Rajasthan", "Jodhpur: Mehrangarh Fort and Blue City"),
                                                ("West Bengal", "Kolkata: Rosogolla and Howrah Bridge"),
                                                ("West Bengal", "Darjeeling: Tea gardens and Himalayan Railway"),
                                                ("Gujarat", "Ahmedabad: Dhokla and Kite flying festivals"),
                                                ("Gujarat", "Surat: Diamond cutting and Surati cuisine"),
                                                ("Uttarakhand", "Dehradun: Jim Corbett National Park and Rishikesh"),
                                                ("Uttarakhand", "Nainital: Naini Lake and Naina Devi Temple"),
                                                ("Kerala", "Kochi: Backwaters and Kathakali dance"),
                                                ("Kerala", "Thiruvananthapuram: Padmanabhaswamy Temple and Kovalam Beach"),
                                                ("Himachal Pradesh", "Shimla: Apple orchards and Rohtang Pass"),
                                                ("Himachal Pradesh", "Manali: Solang Valley and Hadimba Temple"),
                                                ("Madhya Pradesh", "Bhopal: Khajuraho temples and Bandhavgarh National Park"),
                                                ("Madhya Pradesh", "Indore: Street food and Lal Bagh Palace"),
                                                ("Assam", "Guwahati: Kamakhya Temple and Assam tea"),
                                                ("Assam", "Silchar: Barak Valley and Khasi culture"),
                                                ("Punjab", "Amritsar: Golden Temple and Patiala Peg"),
                                                ("Punjab", "Ludhiana: Industrial city and Punjabi cuisine"),
                                                ("Telangana", "Hyderabad: Charminar and Hyderabadi biryani"),
                                                ("Telangana", "Warangal: Kakatiya dynasty and Bhadrakali Temple"),
                                                ("Bihar", "Patna: Mahavir Mandir and Chhath Puja"),
                                                ("Bihar", "Gaya: Bodh Gaya and Vishnupad Temple"),
                                                ("Odisha", "Bhubaneswar: Lingaraj Temple and Udayagiri Caves"),
                                                ("Odisha", "Puri: Jagannath Temple and Konark Sun Temple"),
                                                ("Haryana", "Gurugram: Cyber Hub and Kingdom of Dreams"),
                                                ("Haryana", "Faridabad: Industrial city and Surajkund Crafts Mela"),
                                                ("Jharkhand", "Ranchi: Birsa Munda Stadium and Tribal culture"),
                                                ("Jharkhand", "Jamshedpur: Steel City and Jubilee Park"),
                                                ("Chhattisgarh", "Raipur: Bastar Dussehra and Chitrakoot Falls"),
                                                ("Chhattisgarh", "Bilaspur: Rice bowl of Chhattisgarh and Kanan Pendari Zoo"),
                                                ("Arunachal Pradesh", "Itanagar: Tawang Monastery and Ziro Music Festival"),
                                                ("Arunachal Pradesh", "Naharlagun: Ganga Lake and Polo Park"),
                                                ("Meghalaya", "Shillong: Living root bridges and Shillong Peak"),
                                                ("Meghalaya", "Tura: Garo Hills and Balpakram National Park"),
                                                ("Nagaland", "Kohima: Hornbill Festival and Naga tribes"),
                                                ("Nagaland", "Dimapur: Gateway to Nagaland and Diezephe Craft Village"),
                                                ("Manipur", "Imphal: Loktak Lake and Manipuri dance"),
                                                ("Manipur", "Thoubal: Floating islands and Phumdis"),
                                                ("Mizoram", "Aizawl: Blue Mountains and Chapchar Kut festival"),
                                                ("Mizoram", "Lunglei: Second largest city and Zobawk Sports Academy"),
                                                ("Tripura", "Agartala: Ujjayanta Palace and Tripuri cuisine"),
                                                ("Tripura", "Dharmanagar: Pineapple City and Rowa Wildlife Sanctuary"),
                                                ("Sikkim", "Gangtok: Gurudongmar Lake and Rumtek Monastery"),
                                                ("Sikkim", "Namchi: Siddheshwar Dham and Tendong Hill"),
                                                ("Goa", "Panaji: Feni and Dudhsagar Falls"),
                                                ("Goa", "Margao: Cultural hub and Colva Beach")
                                            ]

        self.current_word = "Press 'Change Word'"
        self.running = False
        self.start_time = None
        self.word_button_rect = pygame.Rect(0, 0, 150, 50)  # Updated to be centered
        self.exit_button_rect = pygame.Rect(0, 0, 150, 50)  # Updated to be centered
        self.start_button_rect = pygame.Rect(0, 0, 150, 50)  # Updated to be centered
        self.font = pygame.font.Font(None, 24)
        self.buzzer_sound_played = False
        self.word_button_text = self.font.render("Change Word", True, (200, 200, 200))
        self.exit_button_text = self.font.render("Exit", True, (200, 200, 200))
        self.start_button_text = self.font.render("Start", True, (200, 200, 200))
        self.update_button_positions()  # Initial update to center buttons
        self.catched_words=[]
        self.hint=None

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((800, 600))
        self.update_button_positions()  # Update button positions when toggling fullscreen

    def update_button_positions(self):
        # Centering the buttons based on the screen size
        screen_width, screen_height = self.screen.get_size()
        self.word_button_rect.center = screen_width // 4, screen_height - 50
        self.exit_button_rect.center = screen_width * 3 // 4, screen_height - 50
        self.start_button_rect.center = screen_width // 2, screen_height - 50

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.toggle_fullscreen()

            self.display_screen()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_mouse_click(self, pos):
        if self.word_button_rect.collidepoint(pos):
            self.buzzer_sound_played = False
            self.change_word()
        elif self.exit_button_rect.collidepoint(pos):
            self.buzzer_sound_played = False
            self.running = False
        elif self.start_button_rect.collidepoint(pos):
            if self.start_time:  # Start the timer only if it's not already running
                self.start_timer()

    def display_screen(self):
        self.screen.fill((255, 255, 255))

        pygame.draw.rect(self.screen, (1, 1, 1), self.word_button_rect)
        self.screen.blit(self.word_button_text, self.word_button_text.get_rect(center=self.word_button_rect.center))

        pygame.draw.rect(self.screen, (0, 0, 0), self.exit_button_rect)
        self.screen.blit(self.exit_button_text, self.exit_button_text.get_rect(center=self.exit_button_rect.center))

        pygame.draw.rect(self.screen, (0, 0, 0), self.start_button_rect)
        self.screen.blit(self.start_button_text, self.start_button_text.get_rect(center=self.start_button_rect.center))

        self.display_word()

    def change_word(self):
        self._word = random.choice(self.words)
        city=self._word[1].split(":")[0]
        hint=self._word[1].split(":")[1]
        self.current_word = f"Guess: {self._word[0]} - {city}"
        self.hint=f"HINT: {hint}"
        self.start_time = time.time()
        print("Word changed:", f"{self.current_word}-{self.hint}")
        self.buzzer_sound_played = False

    def start_timer(self):
        self.start_time = time.time()
        # self.tikTokSound()


    def drawArc(self, surf, color, center, radius, width, start_angle, end_angle):
        rect = pygame.Rect(center[0] - radius, center[1] - radius, radius * 2, radius * 2)
        pygame.draw.arc(surf, color, rect, np.deg2rad(start_angle), np.deg2rad(end_angle), width)

    def display_word(self):
        font = pygame.font.Font(None, 48)
        text = font.render(self.current_word, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        if not self.start_time:
            self.current_word = "Press 'Change Word'"
        elif self.current_word and self.current_word != "Press 'Change Word'":
            text = font.render(self.current_word, True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(text, text_rect)
            text = font.render(self.hint, True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 1.2))
            self.screen.blit(text, text_rect)
            elapsed_time = int(time.time() - self.start_time)
            remaining_time = max(0, 60 - elapsed_time)
            center_x, center_y = self.screen.get_width() // 2, self.screen.get_height() // 6  # Center of the circle
            self.drawArc(self.screen, (255, 0, 0), (center_x, center_y), min(center_x, center_y) - 10, 10, 0,
                         360 * (remaining_time / 60))  # Adjusted to cover full circle
            if remaining_time == 20:
                self.tikTokSound("play")
            timer_text = self.font.render(f"{remaining_time}s", True, (0, 0, 0))
            text_rect = timer_text.get_rect(center=(center_x, center_y))  # Centering the text
            self.screen.blit(timer_text, text_rect)
            pygame.display.flip()
            if remaining_time == 0 and not self.buzzer_sound_played:
                self.tikTokSound("pause")
                self.buzz()
                self.buzzer_sound_played = True



    def buzz(self):
        print("Buzzer sound played!")
        pygame.mixer.init()
        pygame.mixer.music.load("buzzer.mp3")
        pygame.mixer.music.play()
        self.current_word = "Press 'Change Word'"
        self.hint= None
    def tikTokSound(self,tag):
        pygame.mixer.init()
        pygame.mixer.music.load("tiktok.mp3")
        if tag=="play":
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.pause()

def main():
    app = WordDisplayApp()
    app.run()

if __name__ == "__main__":
    main()
