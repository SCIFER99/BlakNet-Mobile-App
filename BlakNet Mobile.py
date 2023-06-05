# By: Tim Tarver

# BlakNet Mobile Application

# Insert all needed import statements
# for BlakNet Mobile Application


import pandas as pd
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


# Below this comment will be imports statements
# for PayPal and Stripe payment system development


# Creating multiple screens for scrolling purposes
# and control the screen manager from the .kv files

Builder.load_string("""
<BlakNetInterface>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size    
            source: "moneybags8.jfif"    
                    
    Widget:
        Label:
            markup: True
            text: "[b]Welcome to BlakNet Mobile![/b]"
            color: 0, 0, 0, 1
            pos: 340, 440
            size: 100, 200
            font_size: 40

        Label:
            markup: True
            text: "[b]Where one-stop shopping Blak happens![/b]"
            color: 238, 64, 64
            pos: 340, 440
            font_size: 20
        
        Button:
            pos: 230, 150
            size: 300, 200
            multiline: False
            text: "Customers"
            background_color: 0, 0, 0, 1
            on_press: root.manager.current = 'signup'
            on_press: app.root.current = 'Page 1'
            
                

""")
Builder.load_string("""
# GUI for the login window

<LoginWindow>:
    email : email
    pwd : pwd
    
    RelativeLayout:
        size: root.width, root.height
        Label:
            text : "EMAIL: "
            size_hint : 0.2, 0.1
            pos_hint : {"x":0.25, "top":0.9}
        TextInput:
            id : email
            multiline :False
            size_hint : 0.3, 0.1
            pos_hint : {"x" : 0.45, "top" : 0.9}
        Label:
            text : "PASSWORD: "
            size_hint : 0.2, 0.1
            pos_hint : {"x" : 0.25, "top" : 0.7}
        TextInput:
            id : pwd
            multiline :False
            size_hint : 0.3, 0.1
            pos_hint : {"x" : 0.45, "top" : 0.7}
        
        Button:
            text : "LOGIN"
            size_hint : 0.3, 0.1
            pos_hint : {"x" : 0.39, "top" : 0.5}
            on_release: 
                root.validate()
                root.manager.transition.direction = "up"
                app.root.current = 'Page 1'
                
                                                
    GridLayout:
        Button:
            text: "Back"
            on_press: root.manager.current = 'signup'
                        
""")

Builder.load_string("""

<SignupWindow>:
    name2 : name2
    email : email
    pwd : pwd
    Label:
        text: "Create your Blak Account"
        pos: 5, 270
        font_size: 30
               
    RelativeLayout:
        Label:
            text : "NAME: "
            size_hint : 0.2, 0.1
            pos_hint : {"x":0.25, "top":0.9}
        TextInput:
            id : name2
            multiline : False
            size_hint : 0.3, 0.1
            pos_hint : {"x" : 0.45, "top" : 0.9}
        Label:
            text : "EMAIL: "
            size_hint : 0.2, 0.1
            pos_hint : {"x" : 0.25, "top" : 0.7}
        TextInput:
            id : email
            multiline : False
            size_hint : 0.3, 0.1
            pos_hint : {"x" : 0.45, "top" : 0.7}
        Label:
            text : "PASSWORD: "
            size_hint : 0.2, 0.1
            pos_hint : {"x" : 0.25, "top" : 0.5}
        TextInput:
            id : pwd
            multiline : False
            size_hint : 0.3, 0.1
            pos_hint : {"x" : 0.45, "top" : 0.5}
        Button:
            text : "Submit"
            size_hint : 0.3, 0.1
            pos_hint : {"x" : 0.39, "top" : 0.28}
            on_press :
                root.sign_up_button()
                root.manager.transition.direction = "right"
            on_press: root.manager.current = 'login'    
                                        
        Button:
            text: "Current User? Click to Login"
            pos_hint: {"x": 0.39, "top": 0.15}
            size_hint: 0.3, 0.1
            on_press: root.manager.current = 'login'    
                    
""")

# GUI to show validation result
Builder.load_string("""
<LogDataWindow>:
    info : info
    FloatLayout:
        Label:
            id : info
            size_hint : 0.8, 0.2
            pos_hint : {"x" : 0.15, "top" : 0.8}
            text : "Account Created Successfully!"
        Button:
            text : "Login"
            size_hint : 0.4, 0.1
            pos_hint : {"x" : 0.33, "top" : 0.55}
            on_release: 
                app.root.current = 'login'
                root.manager.transition.direction = "down"
        Button:
            text : "Create new account"
            size_hint : 0.4, 0.1
            pos_hint : {"x" : 0.33, "top" : 0.4}
            on_release: 
                app.root.current = 'signup'
                root.manager.transition.direction = "down"
""")

Builder.load_string("""
<P>:
    Label:
        text: "Email Address Already Exists."
        size_hint: 0.2, 0.1 
        pos_hint: {"x": 0.3, "top": 0.8}   
""")

Builder.load_string("""
<Q>:
    Label:
        text: "Not a Valid Email."
        size_hint: 0.2, 0.1
        pos_hint: {"x": 0.3, "top": 0.8}
""")

Builder.load_string("""
<R>:
    Label:
        text: "Account Created Successfully!"
        size_hint: 0.2, 0.1
        pos_hint: {"x": 0.3, "top": 0.8}
""")

Builder.load_string("""
<S>:
    Label:
        text: "Shop to ya Drop!"
        size_hint: 0.2, 0.1
        pos_hint: {"x": 0.3, "top": 0.8}
""")
# Subscription Page Development

Builder.load_string("""
<SubscriptionPage>:
    
    GridLayout:
        Button:
            text: "Log Out of BlakNet"
            size: 200, 60
            on_press: root.manager.current = 'Login Page' 
""")

Builder.load_string("""

<PageOne>:
    
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "industry.jfif"
    
    Widget:
        Label:
            markup: True
            text: "[b] Industries [/b]"
            color: 1, 0, 0, 1
            pos: 340, 470
            size: 100, 200
            font_size: 50

    GridLayout:
        Button:
            text: "Culinary Arts"
            pos: 300, 440
            size: 200, 100
            background_color: 1, 0, 0, 1
            on_press: root.manager.current = 'Page 6'
            
             
        Button:
            text: "Health Care"
            pos: 80, 440
            size: 200, 100
            background_color: 0, 0, 1, 1
            on_press: root.manager.current = 'Page 5'

    
        Button:
            text: "Finance"
            pos: 80, 325
            size: 200, 100
            background_color: 0, 1, 0, 1
            on_press: root.manager.current = 'Page 8'


    
        Button:
            text: "Fitness"
            pos: 520, 440
            size: 200, 100
            background_color: 0.2, 0.4, 0.6, 1
            on_press: root.manager.current = 'Page 7'

     
        Button:
            text: "Entertainment"
            size: 200, 100    
            pos: 300, 325
            background_color: 1, 1, 0, 1
            on_press: root.manager.current = 'Page 9'
    
          
        Button:
            text: "Clothing Lines"
            size: 200, 100
            pos: 520, 325
            background_color: 0, 0, 1, 1
            on_press: root.manager.current = 'Page 10'
            
      
        Button:
            text: "Food & Beverages"
            size: 200, 100
            pos: 80, 210    
            background_color: 0, 1, 1, 1
            on_press: root.manager.current = 'Page 11'
         
        Button:
            text: "Professional Services"
            size: 200, 100
            pos: 300, 210
            background_color: 1, 0, 0, 1
            on_press: root.manager.current = 'Page 2'    
        
        Button:
            text: "Barbers/Beauty"
            size: 200, 100
            pos: 520, 210
            background_color: 1, 0, 1, 1
            on_press: root.manager.current = 'Page 3'
           
        Button:
            text: "Sports/Recreation"
            size: 200, 100
            pos: 520, 95
            background_color: 0, 0, 2, 1    
            
        Button: 
            text: "Non-Profit Organizations"
            size: 200, 100
            pos: 300, 95
            background_color: 1, 2, 0, 1
            on_press: root.manager.current = 'Page 13'
            
        Button:
            text: "Information Technology"
            size: 200, 100
            pos: 80, 95
            background_color: 2, 1, 0, 1  
            on_press: root.manager.current = 'Page 12'  
                
        Button:
            text: "Log Out"
            size: 60, 100
            on_press: root.manager.current = 'Login Page'   
""")

Builder.load_string("""
<PageTwo>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size    
            source: "professional.png"    
            
    GridLayout:
        Button:
            text: "Business Consultants"
            size: 200, 100
            pos: 80, 440
            background_color: 1, 0, 0, 1
            
        Button:
            text: "Computer Repair Stores"
            size: 200, 100
            pos: 300, 440
            background_color: 1, 1, 0, 1    
            
        Button:
            text: "Real Estate"
            size: 200, 100
            pos: 520, 440
            background_color: 1.5, 1, 0, 1.5    
            
        Button:
            text: "Interior Designers"
            size: 200, 100
            pos: 80, 325
            background_color: 2.5, 1, 0, 2.5    
            
        Button:
            text: "Construction Workers"
            size: 200, 100
            pos: 300, 325
            background_color: 2.5, 0.05, 0, 2.5    
            
        Button:
            text: "HVAC Installation Services"
            size: 200, 100
            pos: 520, 325
            background_color: 1, 0.9, 1.6, 1    
            
        Button:
            text: "Cleaning Services"
            size: 200, 100
            pos: 80, 210
            background_color: 0.1, 0.1, 1.6, 1.5    
            
        Button:
            text: "Mental Health Services"
            size: 200, 100
            pos: 300, 210
            background_color: 0, 0, 1, 1
            
        Button:
            text: "Lawn Care Services"
            size: 200, 100
            pos: 300, 210
            background_color: 1, 0, 1, 1        
        
        Button:
            text: "Legal Services"
            size: 200, 100
            pos: 520, 210
            background_color: 0, 1, 1, 1     
        
        Button:
            text: 'Back'
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'Page 1'   
                
        Button:
            text: 'Log Out'
            size: 60, 100
            pos: 740, 0
            on_press: root.manager.current = 'Login Page'     
""")

Builder.load_string("""
<PageThree>:       
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size    
            source: "salons.jfif"    
            
    GridLayout:
        Button:
            text: "Hair Salons"
            size: 200, 100
            pos: 80, 440
            background_color: 1, 0, 1, 1
            
        Button:
            text: "Nail Salons"
            size: 200, 100
            pos: 300, 440
            background_color: 1, 1, 0, 1   
            
        Button:
            text: "Barbershops"
            size: 200, 100
            pos: 520, 440
            background_color: 2, 1, 0, 2  
            on_press: root.manager.current = 'Page 4'  
            
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'       
                
""")

Builder.load_string("""
<PageFour>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "barbershops.jfif"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] Barbershop Directory [/b]"
                color: 0, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                root.manager.current = 'Circular Progress Bar'
                import webbrowser
                webbrowser.open('https://booksy.com/en-us/11667_aplus-hair-therapy-barbershop-llc_barber-shop_16100_daytona-beach?do=invite&_branch_match_id=1162827021268132556&utm_medium=merchant_customer_invite&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXT07J0UvKz88urtRLzs%2FVdzb0zQ9wK8rzzU0CAPz9epMiAAAA')    
                            
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')        
                               
                                                                                                               
                       
""")

Builder.load_string("""
<PageFive>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "healthcare.jpg"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] HealthCare Directory [/b]"
                color: 0, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                import webbrowser
                webbrowser.open('')    
    
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')            
        
""")

Builder.load_string("""
<PageSix>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "culinaryarts.jfif"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] Culinary Arts Directory [/b]"
                color: 0, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                import webbrowser
                webbrowser.open('')    
    
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')    
""")

Builder.load_string("""
<PageSeven>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "fitness.jfif"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] Fitness Directory [/b]"
                color: 0, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                import webbrowser
                webbrowser.open('')    
    
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')    
                
""")

Builder.load_string("""
<PageEight>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "finance.jfif"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] Finance Directory [/b]"
                color: 0, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                import webbrowser
                webbrowser.open('')    
    
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')    
    
""")

Builder.load_string("""
<PageNine>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "blackentertainment.png"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] Entertainment Directory [/b]"
                color: 1, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                import webbrowser
                webbrowser.open('')    
    
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')    
                
""")

Builder.load_string("""
<PageTen>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "blak.jfif"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] Clothing Line Directory [/b]"
                color: 1, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                import webbrowser
                webbrowser.open('')    
    
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')    
    
""")

Builder.load_string("""
<PageEleven>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "food.jfif"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] Food & Beverage Directory [/b]"
                color: 0, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                import webbrowser
                webbrowser.open('')    
    
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')    
    
""")

Builder.load_string("""
<PageTwelve>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "informationtech.jfif"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] Information Technology Directory [/b]"
                color: 1, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                import webbrowser
                webbrowser.open('')    
    
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')    

""")

Builder.load_string("""
<PageThirteen>:

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
            source: "nonprofit.jfif"
         
    GridLayout:
               
        Widget:
            Label:
                markup: True
                text: "[b] Non-Profit Directory [/b]"
                color: 1, 0, 0, 1
                pos: 340, 450
                size: 100, 200
                font_size: 50
    
        Button:
            text: "Back"
            size: 60, 100
            on_press: 
                root.manager.transition.direction = 'left'    
                root.manager.current = 'Page 1'
        
        Button: 
            text: "Log Out"
            size: 60, 100
            pos:  740, 0
            on_press: root.manager.current = 'Login Page'  
    
        Button:
            text: "Daytona Beach, Florida"
            size: 200, 50
            pos: 520, 440 
            background_color: 2, 1, 0, 2
            on_press: 
                import webbrowser
                webbrowser.open('')    
    
        Button:
            text: "Orlando, Florida"
            size: 200, 50
            pos: 295, 440
            background_color: 1, 0, 0, 2        
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "West Palm Beach, Florida"
            size: 200, 50
            pos: 70, 440
            background_color: 1, 1, 0, 2    
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Fort Lauderdale, Florida"
            size: 200, 50
            pos: 70, 375
            background_color: 1, 0, 1, 2
            on_press: 
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Miami, Florida"
            size: 200, 50
            pos: 295, 375
            background_color: 1.2, 1.2, 2.1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Belle Glade, Florida"
            size: 200, 50
            pos: 520, 375
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')
    
        Button:
            text: "Rawveera Beach, Florida"
            size: 200, 50
            pos: 70, 315
            background_color: 0, 1, 2, 3
            on_press:
                import webbrowser
                webbrowser.open('')                                
    
        Button:
            text: "Deerfield, Florida"
            size: 200, 50
            pos: 295, 315
            background_color: 0, 1, 0, 3
            on_press: 
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Boynton Beach, Florida"
            size: 200, 50
            pos: 295, 255
            background_color: 0, 2, 4, 6
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Jacksonville, Florida"
            size: 200, 50
            pos: 520, 315
            background_color: 0, 1.5, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Tampa, Florida"
            size: 200, 50
            pos: 70, 255
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Houston, Texas"
            size: 200, 50
            pos: 520, 255
            background_color: 0, 0, 1, 2
            on_press:
                import webbrowser
                webbrowser.open('')       
                
        Button:
            text: "Macon, Georgia"
            size: 200, 50
            pos: 70, 195
            background_color: 0.5, 0.5, 0.5, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Atlanta, Georgia"
            size: 200, 50
            pos: 295, 195
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Lithonia, Georgia"  
            size: 200, 50
            pos: 70, 135
            background_color: 1, 0, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Augusta, Georgia"
            size: 200, 50
            pos: 295, 135
            background_color: 1, 1, 0, 1
            on_press:
                import webbrowser
                webbrowser.open('')
        
        Button:
            text: "Stone Mountain, Georgia"
            size: 200, 50
            pos: 520, 195
            background_color: 1, 0, 0, 1
            on_press: 
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Redan, Georgia"
            size: 200, 50
            pos:  520, 135
            background_color: 3, 2, 1, 1
            on_press:
                import webbrowser
                webbrowser.open('')
                
        Button:
            text: "Decatur, Georgia"
            size: 200, 50
            pos: 70, 75
            background_color: 1, 2, 3, 1
            on_press:
                import webbrowser
                webbrowser.open('')    
    
""")


# BlakNet Mobile App Interface Creation

class BlakNetInterface(Screen):
    pass


# The function below will send business owners and
# customers to the subscription page.


class SubscriptionPage(Screen):
    pass


class PageOne(Screen):
    pass


class PageTwo(Screen):
    pass


class PageThree(Screen):
    pass


class PageFour(Screen):
    pass


class PageFive(Screen):
    pass


class PageSix(Screen):
    pass


class PageSeven(Screen):
    pass


class PageEight(Screen):
    pass


class PageNine(Screen):
    pass


class PageTen(Screen):
    pass


class PageEleven(Screen):
    pass


class PageTwelve(Screen):
    pass


class PageThirteen(Screen):
    pass


class PageFourteen(Screen):
    pass


class PageFifteen(Screen):
    pass


class PageSixteen(Screen):
    pass


class PageSeventeen(Screen):
    pass


class PageEighteen(Screen):
    pass


class PageNineteen(Screen):
    pass


class PageTwenty(Screen):
    pass


class PageTwentyOne(Screen):
    pass


class BlakNetRelativeLayout(RelativeLayout):
    pass


class BlakNetScrollView(ScrollView):
    pass


class BlakNetStackLayout(StackLayout):
    pass


class BlakNetFloatLayout(FloatLayout):
    pass


class BlakNetAnchorLayout(AnchorLayout):
    pass


class BlakNetGridLayout(GridLayout):
    pass


class BlakNetBoxLayout(BoxLayout):
    pass


class BlakNetPageLayout(PageLayout):
    pass


# Store all user data here


class PopupWindow(Widget):

    @staticmethod
    def button():
        pop_fun()


class P(RelativeLayout):
    pass


class Q(RelativeLayout):
    pass


class R(RelativeLayout):
    pass


class S(RelativeLayout):
    pass


def pop_fun():
    show = P()
    window = Popup(title='popup', content=show,
                   size_hint=(None, None), size=(300, 300))
    window.open()


def account_creation():
    show0 = R()
    window0 = Popup(title='popup', content=show0,
                    size_hint=(None, None), size=(300, 300))
    window0.open()


def wrong_email():
    show1 = Q()
    window1 = Popup(title='popup', content=show1,
                    size_hint=(None, None), size=(300, 300))
    window1.open()


def login_successful():
    show2 = S()
    window2 = Popup(title='popup', content=show2,
                    size_hint=(None, None), size=(300, 300))
    window2.open()


class LoginWindow(Screen):
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def validate(self):

        # validating if the email already exists
        if self.email.text not in users['Email'].unique():
            # pop_up()
            login_successful()
        else:

            # switching the current screen to display validation result
            screen_manager.current = 'logdata'

            # reset TextInput widget
            self.email.text = ""
            self.pwd.text = ""


class SignupWindow(Screen):
    name2 = ObjectProperty(None)
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def sign_up_button(self):

        # creating a DataFrame of the info
        user = pd.DataFrame([[self.name2.text, self.email.text, self.pwd.text]],
                            columns=['Name', 'Email', 'Password'])
        if self.email.text != "":
            if self.email.text not in users['Email'].unique():
                # if email does not exist already then append to the csv file
                # change current screen to log in the user now
                user.to_csv('loginInfo.csv', mode='a', header=False, index=False)
                account_creation()
                screen_manager.current = 'login'
                self.name2.text = ""
                self.email.text = ""
                self.pwd.text = ""
            else:
                pop_fun()
        else:
            wrong_email()


class LogDataWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


screen_manager = WindowManager()
screen_manager.add_widget(LoginWindow(name='login'))
screen_manager.add_widget(SignupWindow(name='signup'))
screen_manager.add_widget(LogDataWindow(name='logdata'))
users = pd.read_csv('loginInfo.csv')


# BlakNet Mobile Application Development

class BlakNet(App):

    def build(self):
        screen_manager1 = ScreenManager(transition=SwapTransition())
        screen_manager1.add_widget(BlakNetInterface(name='Login Page'))
        screen_manager1.add_widget((SubscriptionPage(name='Subscription Page')))
        screen_manager1.add_widget(LoginWindow(name='login'))
        screen_manager1.add_widget(SignupWindow(name='signup'))
        screen_manager1.add_widget(LogDataWindow(name='logdata'))
        screen_manager1.add_widget(PageOne(name='Page 1'))
        screen_manager1.add_widget(PageTwo(name='Page 2'))
        screen_manager1.add_widget(PageThree(name='Page 3'))
        screen_manager1.add_widget(PageFour(name='Page 4'))
        screen_manager1.add_widget(PageFive(name='Page 5'))
        screen_manager1.add_widget(PageSix(name='Page 6'))
        screen_manager1.add_widget(PageSeven(name='Page 7'))
        screen_manager1.add_widget(PageEight(name='Page 8'))
        screen_manager1.add_widget(PageNine(name='Page 9'))
        screen_manager1.add_widget(PageTen(name='Page 10'))
        screen_manager1.add_widget(PageEleven(name='Page 11'))
        screen_manager1.add_widget(PageTwelve(name='Page 12'))
        screen_manager1.add_widget(PageThirteen(name='Page 13'))
        screen_manager1.add_widget(PageFourteen(name='Page 14'))
        screen_manager1.add_widget(PageFifteen(name='Page 15'))
        screen_manager1.add_widget(PageSixteen(name='Page 16'))
        screen_manager1.add_widget(PageSeventeen(name='Page 17'))
        screen_manager1.add_widget(PageEighteen(name='Page 18'))
        screen_manager1.add_widget(PageNineteen(name='Page 19'))
        screen_manager1.add_widget(PageTwenty(name='Page 20'))
        screen_manager1.add_widget(PageTwentyOne(name='Page 21'))
        return screen_manager1


if __name__ == "__main__":
    BlakNet().run()
