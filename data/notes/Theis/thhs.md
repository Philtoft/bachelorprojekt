# Lecture 1: Introduction

---

**Computer Security:** Measures and controls that ensure confidentiality, integrity,
and availability of information system assets including hardware, software, firm-
ware, and information being processed, stored, and communicated.

- **Confidentiality:** This term covers two related concepts:
    - **Data confidentiality:** Assures that private or confidential information is
    not made available or disclosed to unauthorized individuals.
    - **Privacy:** Assures that individuals control or influence what information
    related to them may be collected and stored and by whom and to whom that
    information may be disclosed.
- **Integrity:** This term covers two related concepts:
    - **Data integrity:** Assures that information and programs are changed only in a specified and authorized manner.
    - **System integrity:** Assures that a system performs its intended function in
    an unimpaired manner, free from deliberate or inadvertent unauthorized
    manipulation of the system.
- **Authenticity:** The property of being genuine and being able to be verified and
trusted; confidence in the validity of a transmission, a message, or message
originator. This means verifying that users are who they say they are and that each input arriving at the system came from a trusted source.
- **Availability:** Assures that systems work promptly and service is not denied to
authorized users.
- **Accountability:** The security goal that generates the requirement for actions
of an entity to be traced uniquely to that entity. This supports nonrepudiation,
deterrence, fault isolation, intrusion detection and prevention, and after-action
recovery and legal action. Because truly secure systems are not yet an achiev-
able goal, we must be able to trace a security breach to a responsible party.
Systems must keep records of their activities to permit later forensic analysis
to trace security breaches or to aid in transaction disputes.

- **Active attack:** An attempt to alter system resources or affect their operation.
- **Passive attack:** An attempt to learn or make use of information from the system that does not affect system resources. We can also classify attacks based on the origin of the attack:
- **Inside attack:** Initiated by an entity inside the security perimeter (an“insider”). The insider is authorized to access system resources but uses them in a way not approved by those who granted the authorization.
- **Outside attack:** Initiated from outside theperimeter, by an unauthorized or illegitimate user of the system (an “outsider”). On the Internet, potential outside attackers range from amateur pranksters to organized criminals, international terrorists, and hostile governments.

![Untitled](Lecture%201%20Introduction%20c3cf2517f633400799d101c1eb585112/Untitled.png)

### Fundamental security design principles

- Economy of mechanism
    - Simple and small
    - Easier to test and verify
- Fail-safe defaults
    - Permission rather than exclusion
    - System starts in safe and returns to safe state in case of failure
    - Firewall port allowed list
- Complete mediation
    - Access control at retrieval of data
    - Careful of cached access
- Open design
    - Encryption algorithms should be public and prone to feedback
    - Security should not depend on algorithm being secret
- Separation of privilege
    - Multifactor authentication
- No single point of failure
    - Key technique: separation of duty
- Least privilege
    - Only has the least amount of privileges necessary to perform a task
- Least common mechanism
    - Minimise the functions shared by different users
- Minimum exposure
    - Minimise the attack surface a system presents to the adversary
    - Reduce external interfaces
    - Limit information and window of opportunity
- Psychological acceptability
    - Design usable security mechanisms”
    - Help the user to make the right choice
- Isolation
    - Public access systems should be isolated from critical resources or information
    - Security mechanisms should be isolated in the sense of preventing access to those mechanisms. For example, logical access control may provide a means of isolating cryptographic software from other parts of the host system and for protecting cryptographic software from tampering and the keys from replacement or disclosure.
- Encapsulation
    - Subset of isolation
    - Wrapped data and procedures in system that provides protected access points
- Modularity
    - development of security functions as separate, protected modules, and to the use of a modular architecture for mechanism design and implementation.
- Layering
    - use of multiple, overlapping protection approaches addressing the people, technology, and operational aspects of information systems
    - The failure of one approach does not compromise entire system as others are still working
- Least astonishment
    - a program or user interface should always respond in the way that is least likely to astonish the user

### Attack surfaces

- **Network attack surface:** This category refers to vulnerabilities over an enterprise
network, wide-area network, or the Internet. Included in this category are net-
work protocol vulnerabilities, such as those used for a denial-of-service attack,
disruption of communications links, and various forms of intruder attacks.
- **Software attack surface:** This refers to vulnerabilities in application, utility,
or operating system code. A particular focus in this category is Web server
software.
- **Human attack surface:** This category refers to vulnerabilities created by person-
nel or outsiders, such as social engineering, human error, and trusted insiders.

### Group theory

![Untitled](Lecture%201%20Introduction%20c3cf2517f633400799d101c1eb585112/Untitled%201.png)

### Exercises:

1.1: There is an access card to ensure confidentiality and a password that goes with it.

Data integrity is kept because people can have the same name but have different student numbers.

Least priviledge principle ensures integrity because a student can only change their own information.

Availability, have network with ddos security. All systems should be up and running

- card-reader
- website
- server

1.4: 

1. Low confidentiality because no private information
    
    Low-high availability because it all depends on which information is available, the weather we can live without, but if the stock market goes down. 
    
    Moderate-high integrity because people can mess with the public data shown. Defamation, private information, 
    
2. High confidentiality, well it’s extremely sensitive data
    
    Low-moderate, you will need a log kept because data is not changing much, and this is a good tradeoff. 
    
    High integrity, changing names of suspects, agents and such
    
3. High confidentiality, the adversary knows everything about the infrastructure of the organisation and will know when to the possible human attack surface
    
    

1.5: flip boolean and logic

IT-department: It should not be adopted because, however it is better than having nothing, and we are proposing a modified policy because of:

- Economy of mechanism, 7 options are a lot
- Single point of failure, SMS and call, iris and fingerprint
- Least astonishment
- Minimum exposure, minimise attack surface

**Group Theory**

1.1: Closure, associativity, Identity-element, inverse, (communicative for Abelian)

1.2: Closure: It is always a 16-bit string

Associativity: (1111 XOR 1011) XOR 1001 = 1111 XOR (1011 XOR 1001)

Identity-element: 0000 0000 0000 0000

Inverse: XOR by itself

1.3: Closure: always wraps around

Associativity: Yes, it is addition

Identity-element: 0

Inverse: 20-x = 0, so the inverse element is the result of that equation

2.1: No inverse, limited to integers, so no rational numbers to return to the identity element

2.2: No inverse, cannot remove when concatenating.