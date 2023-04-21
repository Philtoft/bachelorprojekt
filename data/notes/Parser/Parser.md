Theory
Software engineering
Software engineering Includes:
Modeling activity
Deals with complexity through modeling. (models are built of the system as well as the application domain)
Problem-solving activity
Search is driven by experimentation, and rely on empirical methods to evaluate the benefits of different alternatives.
Knowledge acquisition activity
Collect data, organize it into information and formalize it into knowledge.
Rational driven activity
Captures the context in which decisions were made, and the rationale behind said decisions.

Requirement engineering
Used in a plan-driven process like waterfall


Requirement Elicitation
Identifies and discovers the requirements from the client (using elicitation techniques mentioned later on like interview, prototyping and ethnography)
Requirement Analysis
Transforms the data taken from the elicitation phase to useful information and requirements to the system.
Requirement Specification Document the requirements Requirement Validation
Go back to the customer and check if its what they wanted. Check for contradicting requirements.

Greenfield engineering
From scratch. Makes it hard to get the requirements from the user, because they might not know what they want.
Re-Engineering
Improving and adding functionality with more detailed requirements from the clients.

Project phases

Requirement elicitation
This process results in a documented definition of the system that can be understood by the client/ customer/ user.
Focus on describing the purpose of the system. Focuses on the application domain.
Techniques
Interviewing
Ethnography, watch the user while they use the previous system in their own environment.
Software developers know little about the application domain, and the user is too engulfed in their domain, and can forget vital details.
Prototyping (show them to the client)
These can be technical or user interface prototypes
Functional Requirements
Describe the functionality that the system needs, as given by the client and observed from the user.
Non functional Requirements
Describe the other requirements that the user probably won’t understand. Will effect the whole software system.
Categories:
Usability
-
Reliability
Performance
Supportability
Use Case
Contains an actor, flow of events and post conditions
User Story
Contains user, role, goal and acceptance criteria Similarities to use cases?
Describe one way to use the system, that is centered around a goal.
Written from the perspective of the user
Uses natural language.
Differences?
Use stories deliberately leaves out important details, meant to elicit conversations by asking questions.
Use cases are more detailed and have up-front requirement specifications

Analysis
This process results in a documented analysis model, that the developers can unambiguously interpret. Also includes technical specifications.
Focuses on the solution domain.
Analysis model
Model of the system that shows that it is complete, correct, consistent and verifiable.
It structures formalizing requirements and leads to revision of said requirements.
Contains
Functional model
Analysis object model
Dynamic model


Design

Implementation Test
Design Patterns

Solid Principles
Single Responsibility
A class should have one and only one reason to change. Meaning a class should have one responsibility and therefore only one reason to change.
What is a reason for change? A responsibility. fx.
This can be done by using a command design pattern to fx. Seperate a buttons functionality to the user interface.


Open/Close
You should be able to extend a classes behavior without modifying it (be able to add new inherited classes without modifying the class that is dependent on it / calls it).
Fx.
IoCContainer in our project. Here any class dependent on the container will know that they need an abstract class A, but they don’t need to know which concrete subclass of A they are using.
Thereby making it possible to extend the functionality of the client class, by using different subclasses of A, and not modifying the client class.

Liskovs substitution
Derived classes must be substitutable for their base classes (functionality of a class should not change between the inherited class and its subclasses).
Fx.


Interface Segregation
Interfaces should not have methods that aren't used by the client (make fine grained interfaces that are client specific).
Dependency Inversion
Higher level modules should not depend on lower level concrete classes, but instead on abstractions (interfaces). So when the lower level modules change details, the higher level modules don't have to follow.

This principle can be seen every time the systems implements an interface and uses said interface to connect to component with another aspect of the system.


Architectural Design

Design goals
Describe the qualities of the system that developers should optimize (prioritization).
Derived from nonfunctional requirements.
Performance, dependability, cost, maintenance, end user criteria.
Fx. Reliability, fault tolerance, security, modifiability


Architectural Styles

Repository
Used for datadriven systems.
Subsystems access and modify a single data structure called the central repository. This maintains all the data. The subsystems don't need to know each other.
Problem: the central repository can become a bottleneck, for performance and modifications. And coupling between subsystems and repository is high
Model/View/Controller
Model, maintain domain knowledge (doesn't depend on V or C) changes made via a subscribe/notify protocol.
View, displays it to the user
Able to have multiple views using the same information (same model)
Controller, manage the sequence of interactions with the user. (manages the information flow)
(Use observer design pattern to remove direct dependency between Model and View objects). Works well for interactive systems, Especially when multiple views of the same model are needed. Used for maintaining consistency across distributed data.

Client/Server
Server provides services to instances of other subsystems called clients (responsible for interacting with users).
Request for a service usually done via a remote procedure call mechanism / common object broker (HTTP, CORBA).

Peer-to-peer
Generalization of client/server, where subsystems can be both client and server (request and provide services).
Have possibility of deadlocks
Fx. Database that both accepts requests from the application and notifies to the application whenever certain data is changed.


Three-tier
Organizes subsystems into three layers:
Interface layer, all boundary objects dealing with the user (windows, forms, webpages etc)
Application logic layer, all control and entity objects (creating processes, rule checking, notifications etc)
Storage layer, realizes the storage, retrieval and query of persistent objects. Can be shared by several different applications operating on the same data.
Decoupling between interface and application logic layer enables modification and change in the interface layer without dealing with the application logic layer.
Four-tier
Here interface layer is split into:
Presentation Client
Located on the user machines
Presentation Server
Located on one / more servers.
Enables multiple presentation clients to use the same presentation server.


Pipe and filter
Filters are subsystem that process data received from a set of inputs and send results to other subsystems via a set of outputs.
Pipes are the associations between subsystems.
Each filter knows only of the data received from the pipe, no the filter that produced them. Filters are executed concurrently (synchronization is possible via the pipes).
Suited for systems that apply transformations to streams of data without intervention by users. (not good for system with complex interactions)


UML diagrams (e.g., Class diagram)

UML is a family of graphical notation that help describe and design software systems particularly systems built using object oriented programming.

UML notation was created by The Three Amigos in 1995. They made UML to have a universal way of depicting code in diagrams, because programming languages are not on a high enough level of abstraction to facilitate discussions about design.

UML can be used as sketch, blueprint or as a programming language.





Class diagram
Abstraction specifying attributes and behavior of a set of objects
Attribute visibility: + public, - private, # protected
Abstract classes: Class name or <<abstract>> Class name
Interface: <<interface>> Class name




Deployment diagram
Structure diagram
Used to depict where various elements of a system are located
For instance, a distributed system based on a client/server architecture.

Use Case Diagram
Behavior diagram. Captures requirements, abstract scenarios. Comprised of two parts: use case diagram and use case text.
Text syntax: Name of use case, participating actors, flow of events, entry condition, exit condition, exceptions, quality requirements




Activity Diagram
Behavior diagram.
Models the dynamic behavior of a subsystem
Also known as flowcharts





State Machine Diagram
Behavior diagram
Specifies the dynamic behavior of a single object
They model the sequence of states an object goes through at runtime in reaction to external events
They have an initial and final state


Or





Sequence Diagram
Behavior interaction diagram
Has actors, lifelines, activations and objects






Communication diagram
Behavior interaction diagram
Focus more on relationships of objects than sequence diagrams
They are more “informal” and used for sketching





Object diagram
Structure diagram
Describes relationship between different objects
Instances instead of classes
Links instead of associations




Component diagram
Structure diagram
Shows components and their required interfaces/ports





Package diagram
Structural diagram


Software processes
Plan-driven processes
processes where all of the process activities are planned in advance and progress is measured this plan. (waterfall)
Iterative or incremental process
planning is incremental and it is easier to change the process to reflect changing customer requirements. Here small projects are continuously integrated into the whole. All the phases of the software process is covered iteratively or different prototypes and versions of the system. (vs. the monolithic approach.)
Agile processes
the development of "shappable" software takes precedence over planning and documentation. Here you specifically follow the rules listed in the agile manifesto. (SCRUM, XP etc)


Waterfall
Most known plan-driven process, with the following phases:
Feasibility (is it reasonable to do the project.)
User requirements
Analysis (plan)
System design
Program design
Coding
Testing
Operation
In every phase it is possible to go backwards, get more requirements from the user if you have holes in your model during analysis.
Each phase produces a documents, freezes it and change management process is used afterwards (very much document-driven process)
Strength:
Easily manageable process (manager's can have a good oversight)
If you know all the requirements form the beginning
Easy to split the work.
Weaknesses:
Inflexible partitioning of the project into distinct stages
Feedback on the system can be very expensive if changes need to be made. (like turning a ferry instead of a canoe)
Difficult to respond to changing customer requirements later on in the process.
Hard when changes have to be made during the development process.
Agile methods
Agile Methods, subset of iterative methods.
Fx. Scrum, extreme programming (XP)
Strengths:
Rapid a flexible response to change
Simplicity, lightness (no documentation needed), teams should be small, should discuss instead of documenting. The team should be self-sufficient (design, analyse, code, test etc. In the same team)
Weakness:
No hand over, since it all is done in one team.
The customer should be very close to the development, so they can give quick feedback.
Focus on delivering something useful, no on the process-compliancy activities.