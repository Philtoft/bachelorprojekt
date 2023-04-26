### **How to build UI interface**

A layout defines the structure of the UI of an app such as in an activity.

All elements in a layout are build using a hierarchy of `View` and `ViewGroup` objects.

**View**: draws something on the screen → Buttons, Text, Image

**ViewGroup**: invisible container that defines the structure for views and other ViewGroups → LinearLayout, ConstraintLayout

- Two ways of building UI’s
    - Declare UI elements in XML
    - Instantiate layout elements at runtime
- Each layout must have a root element

**Loading XML resources**

- When app compiles → each XML layout is compiled into a `View` resource
- The layout of each activity should be loaded on the **onCreate()** lifecycle event in the **setContentView()** method 🔍

**Attributes**

- UI elements’s design are defined through attributes which are key-value properties
- Each View object can have an integer → but doesn’t have to
- Each element can be found through their ID in the Activity class through the findViewById method

There are two ways you can build UI interfaces for android app. The primary way is through building the XML files in the resources folder. Here you can define what elements shall be contained within the distinct files that can represent Activities and also Fragments. If there’s a TextField the content of the input field can be defined in the strings.xml file inside resources, where the value is defined and thus standardized instead of containing it in each activity and fragment file.

### **Lifecycle of app**

The Activity component of an app which displays a UI has different lifecycle methods. These methods can be overwritten and thus we can modify their behaviour and trigger our own custom methods as needed.

- Lifecycle of Android Activity
    - onCreate()
    - onStart()
    - onResume()
    - App is running with activity shown
    - onPause()
    - onStop()
    - onDestroy()

Fragments are resusable portions of an app’s UI. A fragment defines and manages its own layout and has its own lifecycle. Fragments must be hosted by an activity or another fragment. Fragments introduce **modularity** and **reusability** into the activity’s UI.

Fragments also have their own lifecycle which is dependent on the activity component’s lifecycle.

- Lifecycle of Android Fragment
    
    ![Untitled](2)%20User%20Interface%20Layout%20(4)(1%205)%202ae3f31480ea426c96089027fe2159d8/Untitled.png)
    

### **Comparison of features of UI components (advangates vs disadvantages)** 🔍

Using fragments makes reusability easy inside activities. Activities are good places to put global elements around your app’s UI such as a navigation drawer. Fragments however are better suited for defining and managing the UI of a single screen or portion of a screen.

### **Sharing data between UI components**

There are many ways to share data between UI components: shared preferences, intents, database locally or database remotely. For small amounts of data, intents are the best.

**Singleton object** ← not good

- **Intents**
    
    ```kotlin
    // MainActivity.kt
    Intent intent = new Intent(MainActivity.this, SecondScreen::class.java);
    
    // Attaching data to the intent
    // key-value pair
    intent.putExtra("name", "philip")
    intent.putExtra("age", 25)
    
    startActivity(intent); // will navigate to the screen
    
    // SecondScreen.kt
    Intent incomingIntent = getIntent(); // Intercepts any intent coming to the activity
    String incomingName = incomingIntent.getStringExtra("name");
    ```
    

Intents describe an operation to be performed. It can be used together with 

- **startActivity()** method where you can send data between activities.
- **BroadcastIntent**: to send it to any interested **BroadcastReceiver** component
- **Context.startService** and **Context.bindService** to communicate with a background service

An intent can facilitate runtime binding between the code in different applications

- Elements of an intent
    - Action → action to be performed: view, edit & main
    - Data →

There are diffferent ways of sharing data between UI components. There’s the obvious with regards to storing the necessary information in a global database. Another approach is to have a ViewModel that wraps around different Fragments. Through the ViewModel there’s an option to share data between the different fragments inside an activity

[PASSING DATA BETWEEN ACTIVITIES - Android Fundamentals](https://www.youtube.com/watch?v=IWXYV1dC2FQ)

### **Intent**

Slide 3

- A object the components can use to communicate with the OS
- Explicit intents
    - Used in the context of my app, where internal components are started
- Implicit intents
    - Start components in other apps (camera, calendar etc)

**ViewModel**

[ViewModel Explained - Android Architecture Component | Tutorial](https://www.youtube.com/watch?v=orH4K6qBzvE)

[ViewModel Overview  |  Android Developers](https://developer.android.com/topic/libraries/architecture/viewmodel)

A class designed to store and manage UI-related data in a lifecycle friendly way → it allows data to survive configuration changes such as screen rotation.

For simple data that needs to persist, we have use **onSaveInstanceState()** method and restore it in the **onCreate()** bundle. ← good only for small amounts of data that can be serialized. Not for large amounts of data. 

Another problem: UI controllers can have to make asynchronous calls… 🔍

**Sharing data between fragments**

### The use of App resources

[App resources overview  |  Android Developers](https://developer.android.com/guide/topics/resources/providing-resources)

Files and additional static content that my app’s code can use such as bitmaps, layout definitions, user interface strings etc.

Based on XML layout format

- Resources should be externalized from the code so that they can be maintained independently.
- They should also be grouped together so that they are easier to maintain.
- Externalized resources can be accessed in the code through their id which is being stored in the apps R class which is accessible in the source code
- Typical resource grouping
    
    MyProject
    
    - src → activity.kt
    - res
        - drawable → graphics
        - layout →
        - mipmap → icons
        - values → string, colors

**Slide 3**

- Color resources
    - Gets defined in: res/values/colors.xml
    - Specified in RGB
    - Inside resource tag, are the color tags
- String resources
    
    3 string types: 1) string, 2) string array & 3) quantity string
    
    Syntax based on XML
    
- Style resources
- Layout resources

### **Android Manifest file’s role** 🔍

The Manifest file is a file where the developer can define the different activities that should be available in the app aswell as which broadcast receivers it should listen to 🔍

**Slide 3:**

- Configuration file for app project
- Describes essential information about the app to the Android build tools, Android OS and Google Play
- Contains
    - Package name
    - Components → activities, services, broadcast receivers & content providers
    - Permissions → set permission to access content in the app
    - Requirements → requirements of the hardware and software

An app’s activity has a context

- Shared preferences: data persistency in an activi

### My project

- Sebastian
    - Activity is bound to ViewModel
    - Recycler:
        - More options for layouts → grid & staggered
        - Must have a ViewHolder

# Disposition

- App lifecycle
    - Rotation
- UI
    - Material Design
    - Sharing data
        - Shared preferences
            - You can create it and store it locally and access it through other activites → not good approach
            - Good for small amount of data
        - Intent
        - Singleton
    - list vs recycler
- Resources
- Manifest
- Own usage

# **Questions**

- Can an android View element exist without an ID
    
    No: some things shouldn’t be accessed and manipulated in the Kotlin code and thus doesn’t need an ID
    
- What are the different layout types that exist?
    - Linear Layout
    - Relative Layout
    - Web layout
    
    ![Untitled](2)%20User%20Interface%20Layout%20(4)(1%205)%202ae3f31480ea426c96089027fe2159d8/Untitled%201.png)
    
    With adapter:
    
    - List View
    - Grid View