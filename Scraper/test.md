# Security

- Exercises
    - Exercise 1 - 31/08
        - Block 1 - Security
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled.png)
            
            Confidentiality:
            
            - Data confidentiality:
                - Low impact: Student number should only be known by student and possibly faculty staff
                - Moderate impact: Personal information, eg. grades, contact info, messages on the account should only be available to relevant individuals
            - Privacy:
                - Low impact: Tracking modifiability in accordance with EU regulations
            
            Integrity:
            
            - Data integrity:
                - Moderate impact: Changes - and their responsible individuals - of grading and other sensitive modifiable data should be tracked to prevent corruption of data
            - System integrity:
                - Moderate impact: Only authorized personal can change grades or personal data
            
            Availability:
            
            - Low impact: Loss of access card - may impact student slightly but no adverse effects
            - Moderate impact: Downtime of website - reputational damage and loss of student and faculty efficiency
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%201.png)
            
            Confidentiality:
            
            - High impact: data package interception - depending on the contents of the data package the impact might be very great if confidential information is leaked
            
            Integrity:
            
            - Low Impact: Data packages being lost and never received
            
            Availability:
            
            - Low Impact: System downtime - there are other options to send data
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%202.png)
            
            a) Medical or criminal records
            
            b) Trade or bank related documents that might manipulate the market
            
            c) Military/defence systems 
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%203.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%204.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%205.png)
            
            | Impact/objective | Confidentiality | Availability | Integrity |
            | --- | --- | --- | --- |
            | a | Low: it’s public and accesible information either way | Low: Non critical info that could be gathered elsewhere | Moderate: Displaying false info could disrupt operations and affect the public |
            | b | High: Leaks can damage investigations and endanger involved personel | Low: Loss of availability may impede an investigation momentarily but nothing adverse | High: Modified data can affect a trial and result in death if eg. a murderer is let loose |
            | c | Moderate: data itself is not crucial but a leakage can severely damage the trustworthiness of the organization | Moderate: May hamper work and cause loss of revenue due to disruption | High: Tampering with information in a financial organisation can lead to major losses of revenue and theft due to replaced account numbers |
            | d | 1) High: severe damage of the markets
            2) Moderate: damage to reputation
            3) High: severe damage to markets and reputation | 1) Moderate: disruption and potential loss of revenue
            2) Low: non essential and can be accesed later 
            3) Moderate: disruption | 1) High: Hiring based on false info, security risks and integrity
            2) Low: can be rectified
            3) High:  |
            | e | 1) High: Monitoring of sensor data may expose military activity
            2) High: Might present a subgoal to further penetrate the security
            3) High: All information about military instalations are highly sensitive and high Impact due to higher risk of hostile targeting  | 1) High: disruption of power is critical for defence systems
            2) Low: may be accessed later
            3) High: Military systems are critical to be kept online at all times | 1) High: Tampered sensor data might result in power shortages/overloads of critical facilities
            2) High: May present a subgoal for further penetration such as Masquerading.
            3) High: |
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%206.png)
            
            a) The security design principle of **Fail-safe defaults** is violated.
             The code checks whether a user does NOT have access, however, instead it is much better to assume that no user has access as a standard and then check for access.
            
            b) 
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%207.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%208.png)
            
            multi-step authentication is in general a great way to increase layering, however, Psychological acceptability is at stake. Few students view their grades and data as crucial and would protest to too high security standards. As such, simple and quick authentication is best to meet the standards without antagonizing the users. I would propose the use of a Password and an SMS. Student cards is also an option but users always carry their phone, not necesarily their student card. Iris/fingerprint scanner would violate the Economy of mechanism principle as it is simply overkill
            
        - Block 2 - Group Theory
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%209.png)
            
            Associative: for all integers $\forall a,b,c \in G, a+(b+c) = (a+b)+c$
            
            Has an identity element 0: $\exist e \in G$ such that $\forall a \in G, a+e = a = e+a$, in this case it is 0
            
            Each element has an inverse: $\forall g \in \exist g^{-1} \in G$ such that $g+g^{-1} = e = g^{-1}+g$, in this case it is the negative version of any element
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2010.png)
            
            Closure: no matter which elements we operate on it will always result in a 16-bit binary string
            
            Associative: given 3 binary strings starting with 0000 0000 0000 and ending with: 0001, 0011, and 0111, noted a, b, and c respectively
            
            $(a\bigotimes b)\bigotimes c$ = $(0001\bigotimes 0011) \bigotimes 0111$ = $0010 \bigotimes 0111 = 0101$
            
            and 
            
            $a\bigotimes (b\bigotimes c$) = $0001\bigotimes (0011 \bigotimes 0111)$= $0001 \bigotimes 0100 = 0101$
            
            As such we have shown that it is associative as the order of operations doesn’t matter
            
            Identity element: 0000 0000 0000 0000 because any element XOR 0000 results in the same element.
            
            Inverse: any string is its own inverse, eg. $1001\bigotimes 1001 = 0000$
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2011.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2012.png)
            
            Associativity: (((1+2)%20)+5)%20 = 8 and (1+((2+5)%20))%20 = 8 
            
            Identity element: 0 
            
            Inverse: for a number n = 20-n 
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2013.png)
            
            The set of integers contains the value 0. As such the law of identity is broken. eg.
            
             $a*b \not = a$ as an example: $2*0 \not = 2$
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2014.png)
            
            Given the empty list there is no inverse element that can be concatenated to return to the empty list.
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2015.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2016.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2017.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2018.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2019.png)
            
        
    - Exercises 4 - 21/09
        
        1. Alice and Bob will be running Diffie-Hellman and has agreed on the group `(Z/241Z)*` with generator `g=7`.
        
        Alice = A | $x_a$=237 | $Y_a = a^{x_a} mod \space q = 7^{237} mod \space 241 = 7$
        
        Bob = B | $x_b = 9$ | $Y_b = a^{x_b} mod \space q = 7^{9} mod \space 241 = 79$
        
        1. If Alice picks the secret `a=237` and Bob picks the secret `b=9`, what will the secret be?
            
            Common secret key: $K = (Y_b) ^{x_a} mod \space q$ = $79^{7} mod \space 241 = 74$
            
        2. In the same group, with the same generator, Alberte and Benjamin runs Diffie-Hellman. If the adversary observes the messages `A=26` (from Alberte to Benjamin) and `B=85`(from Benjamin to Alberte), what is the shared secret `s`?
            
            q = 241; alpha = 7; $Y_A = 26; Y_B=85$
            
            Simply solve either equation by trying out different prime numbers until the equation is true: 
            $7^a mod \space 241 = 26$, a = 
            
            $7^a mod \space 241 = 84$, a =
            
        3. If the adversary observes instead the messages `A=44` and `B=201`, what is the shared secret `s`?
        q = 241; alpha = 7; $Y_A = 44; Y_B=201$
            
            $7^a mod \space 241 = 44$
            
            $7^a mod \space 241 = 201$
            
        
        2. From the Stalling and Brown book (problem): 21.12
        
        ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2020.png)
        
        $Y_a = \alpha ^{X_a} mod \space q = 5^{X_a} mod \space 23 = 10$, $X_a =$
        
        $5^a mod \space 23 = 8$, a =
         
        
        3. On the Kali VM, you'll find the gpg tool preinstalled. Use this tool in the following exercise. On a forum for ITU students of dubious virtue, you find [this file](https://learnit.itu.dk/pluginfile.php/238684/course/section/119957/sign.zip.gpg), ostensibly the answers to the multiple choice part of the SECURITY, BSC course final examination.
        
        Decrypt the file. Perhaps the passphrase is "appliedcrypto".
        
        The file contains a number of versions of the answer for a multiple-choice examination.
        
        Find out which version is signed by this [key](https://learnit.itu.dk/pluginfile.php/238684/course/section/119957/public_key.asc).
        
        Do you have reasons to believe at this point that the version signed with that key was really authored by Rosario?
        
        You will find these command helpful (try gpg --help for details. Or google.):
        
        gpg --decrypt filename
        
        gpg --verify signature-file contents-file
        
        gpg --import key-file
        
        gpg --recv-keys key-id
        
        4. Stallings & Brown, Chapter 2, Review questions 2.9, 2.11
        
        5. - Stallings & Brown, Chapter 2, Problems 2.5
        
    - Exercises 7 - 26/10
        
        ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2021.png)
        
        Access inheritance - 644 **grants read and write permission to the owner of the file, and read permission to the group and others so this would usually protects the file, however, since the directory is 730 whit priveleges for the group the write and execute, then they are inherited to all group members and therefore the file is not secure.**
        
        ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2022.png)
        
        a) 
        
        Access rights:
        
        Funding RG = age greater than 35
        
        Funding TG = age lower or equal to 35
        
        R1: can_access(u, f, e)
        
        $Age(u) > 35 \wedge funding(f)\in \{RG\}$
        
        $Age(u) \le 35 \wedge funding(f) \in \{RG, TG\}$
        
        Given the following 12 policy rules below, find the 7 potential conflicts.
        
        ```
        R1: Generally, a document classified at the secret level ought to be downgraded after 10 years.
        R2: Generally, a document classified at the confidential level ought to be downgraded after 5 years.
        
        R3: The downgrading type of any occasional mission plan must be “at a time” and this document has to be downgraded in a short time.
        R4: The downgrading type of any permanent mission plan must be “by order”.
        R5: The downgrading type of any mission report must be “at a time”.  For any other document,
        
        R6: if it is classified at the secret level, then it has to be downgraded, at the confidential level, after 10 years.
        R7: if it is classified at the confidential level, then it has to be downgraded, at the public level, after 5 years
        
        R8: A mission plan has to be downgraded “at a time”.
        R9: A mission report has to be downgraded “by order”.
        R10: A mission report which deals with a computer failure has to be downgraded “at a time”.
        R11: A mission plan which deals with a mission which has been cancelled has to be downgraded “by order”.
        R12: Any mission plan has to be downgraded, at the public level, the day after the end of the mission
        ```
        
        R1 and R3 - specific date and unspecific date for downgrading 
        
        R7 and R12 - the date for downgrading for mission plans are conflicting
        
        R2 and R6 - confidential ought to be downgraded after 5 years but R6 states 10 years 
        
        R1 and R6 ought to be and has to be
        
- Lecture notes
    - Lecture 31/08
        
        Types of adversaries:
        
        Activists: Political agenda, attacks for a political agenda
        
        Vandals: For fun and giggles
        
        Criminals: Main purpose is echonomical
        
        States: War and Putin being a dick
        
        Cyclic groups: 
        
    - Lecture 2 07/09
        
        ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2023.png)
        
        We are allowing the adversary control of the network but not of our machine. The adversary can basically change or block any form of communication on the network.
        
        This is fx. the case when using a standard TCP stack which is easy to attack.
        
        Physical layer: 
        
        Responsible for transmission of binary data across a physical link. 
        
        ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2024.png)
        
        IP Spoofing: 
        
        ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2025.png)
        
        This is, however, hard to do these days due to modern security measures. 
        
        TCP: helps to limit how many messages arrive to avoid overload and make sure the received packages are received, reordered to initial order and will make sure that not received packages are re-sent. 
        
        Firewalls: 
        
        Filters traffic through to a network based upon given rules.
        
    - Presentations 30/11
        
        
- Exam
    
    Slides compilation: 
    
    [combined.pdf](Security%20b108b7e21ff044ac83e3a6248fdd5159/combined.pdf)
    
    [ExamSetsCombined.pdf](Security%20b108b7e21ff044ac83e3a6248fdd5159/ExamSetsCombined.pdf)
    
    [Security Re-exam prep.docx](Security%20b108b7e21ff044ac83e3a6248fdd5159/Security_Re-exam_prep.docx)
    
    - Exam Questions
        - Principles
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2026.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2027.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2028.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2029.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2030.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2031.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2032.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2033.png)
            
        - Authentication and Access Control
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2034.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2035.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2036.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2037.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2038.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2039.png)
            
        - Network Security + Network Services
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2040.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2041.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2042.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2043.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2044.png)
            
        - System Security + Logging and log analysis
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2045.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2046.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2047.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2048.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2049.png)
            
        - Web-Application Security
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2050.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2051.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2052.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2053.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2054.png)
            
        - Cryptography
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2055.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2056.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2057.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2058.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2059.png)
            
        - Security Protocols
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2060.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2061.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2062.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2063.png)
            
        - Penetration testing
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2064.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2065.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2066.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2067.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2068.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2069.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2070.png)
            
        - Advanced Crypto
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2071.png)
            
        
        - MSC Computer networks
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2072.png)
            
            ![Untitled](Security%20b108b7e21ff044ac83e3a6248fdd5159/Untitled%2073.png)
            
    - Re exam
        
        Security Re-Exam prep
        
        # Security Principles/Goals and Authentication – ca. 12:00
        
        Security Goals(CIA):
        
        - **Confidentiality**
            - **Data confidentiality:** private or confidential information is not made available or disclosed to unauthorized individuals.
            - **Privacy**: individuals control or influence what information related to them may be collected and stored and by whom and to whom that information may be disclosed
            - **Attacks**:
                - Eavesdropping: Reading messages on the network
                - Man in the middle: attacker secretly relays and possibly alters the communications between two parties who believe that they are directly communicating with each other, as the attacker has inserted themselves between the two parties
            - **Integrity**
                - **Data integrity:** information and programs are changed only in a specified and authorized manner
                - **System Integrity** a system performs its intended function in an unimpaired manner, free from deliberate or inadvertent unauthorized manipulation of the system
                - **Attacks:**
                    - Masquerading:
                    - Message tampering
                    - Replaying:
                - **Availability:** systems work promptly, and service is not denied to authorized users
                    - **Attacks:**
                        - DOS
                        - Distributed DOS
        
        Principles:
        
        - **Economy of mechanism**: design of security measures embodied in both hardware and software should be as simple and small as possible to ease testing and verification to minimize weaknesses
        - **Fail-safe defaults**: access decisions should be based on permission rather than exclusion. No access as standard and then check for permissions – not vice versa.
        - **Complete mediation**: every access must be checked against the access control mechanism. Systems should not rely on access decisions retrieved from a cache
        - **Open design**: the design of a security mechanism should be open rather than secret. The algorithms can then be reviewed by many experts, and users can therefore have high confidence in them.
        - **Separation of privilege**: multiple privilege attributes are required to achieve access to a restricted resource eg. multifactor user authentication.
        - **Least privilege**: every process and every user of the system should operate using the least set of privileges necessary to perform the task
        - **Least common mechanism:** design should minimize the functions shared by different users, providing mutual security. Reduces interception risk and easy to verify security implications.
        - **Psychological acceptability**: security mechanisms should not interfere unduly with the work of users, and at the same time meet the needs of those who authorize access.
        - **Isolation**: limit the number of systems on which high risk data are stored and isolate them, either physically or logically
        - **Encapsulation**: a specific form of isolation based on object-oriented functionality. Protection is provided by encapsulating a collection of procedures and data objects in a domain of its own so that the internal structure of a data object is accessible only to the procedures of the protected subsystem.
        - **Modularity:** provide common security functions and services, such as cryptographic functions, as common modules that can be invoked by numerous protocols and applications**.**
        - **Layering**: use of multiple, overlapping protection approaches addressing the people, technology, and operational aspects of information systems. failure or circumvention of any individual protection approach will not leave the system unprotected.
        - **Least astonishment**: a program or user interface should always respond in the way that is least likely to astonish the user.
        - **No single point of failure**: if one part of the system fails, the other parts will not – avoid having a critical section that could compromise everything.
        
        Authentication and Access control:
        
        Definition: Verify a claim of identity.
        
        Factors of authentication:
        
        - Knowledge – something you know – password pin etc.
        - Possession – something you have – smartcard, token etc.
        - Inherence – something you are – biometrics eg. fingerprint
        
        Common type of authentication:
        
        - Passwords
            - Take a password and check against the ID and it’s registered password
            - Vulnerable:
                - Brute force + dictionary attacks + popular passwords
                - Password guessing
                - Snooping – watching over your shoulder
                - Spoofing – Fake websites trying to make you type your password
        
        How to ensure authentication:
        
        Multi-factor authentication – password plus one of the following:
        
        - Token-based authentication
            - Something you own – access card, Electronic key
            - Identifies object rather than user
            - Risks being lost
            - Requires infrastructure – can be costly
        - Biometric authentication
            - Something you are
            - Physiological:
                - Fingerprint or eyes
            - Behavioral:
                - Voice or patterns
            - Very secure – hard to fake/trick
            - Risk of false-negatives and positives
            - Very expensive to implement
        
        Storing keys safely – SALT + HMAC functions.
        
        SALT:
        
        salt serves three purposes:
        
        - prevents duplicate passwords from being visible in the password file
        - greatly increases the difficulty of offline dictionary attacks - number of possible passwords is increased with, b bits, a factor of 2^b
        - nearly impossible to find out whether a person with passwords on two or more systems has used the same password on all of them
        
        Steps in salting:
        
        1. Create salt by taking random number/related to current time
        2. Append salt to the password
        3. HASH the combination of the 2 passwords
        4. Make sure the hashing function is “slow” to make brute-force infeasible
        5. Store hashed salt-password with a plaintext version of the salt in the password file
        6. When needed, the salt can be used to reverse hash the salt-password and verify the password typed by the user
        
        # Symmetric & Assymmetric Cryptography – way too much ca. 10:40
        
        1. Overview - What is symmetric and asymmetric cryptography?
            1. Usage: Used to protect data confidentiality, integrity and availability on insecure networks
            2. It is various algorithms that utilize strings aka. keys to encrypt/decrypt messages and check authenticity
            3. Comparison:
                1. symmetric cryptography
                    1. Uses same key both for encryption and decryption
                        1. Key must be exchanged somehow beforehand
                    2. Examples:
                        1. Simple: Caesar’s cipher & Block cipher
                            1. Only protects confidentiality
                        2. Advanced additions: MAC Algorithm, Hash definitions
                            1. Ensures confidentiality, integrity and authenticity
                            2. Fx. useful for storing passwords very securely
                        3. asymmetric cryptography
                            1. Uses two different keys, private and public keys.
                                1. Public key is available to anyone
                                2. Private key is only known by the receiver
                                3. Requires a key exchange algorithm such as Diffie-Hellman
                            2. Examples
                                1. El-Gamal algorithm
                            3. Encryption basics:
                                1. Transforming a string into a different semantically equivalent one(encryption) that can be decrypted again
                                    1. Algorithms create a ciphertext that can be translated to message if one has the right key.
                                        1. Generate ciphertext: c = ℰ(m,k), for
                                            1. c = ciphertext, ℰ = encryption function, m = message, and k = key
                                        2. Decrypt message: m = D(c,k’)
                                            1. D = reverse encryption function, k’ = another(or same) key
                                        3. Correctness
                                            1. Applying the decryption to an encrypted message yields the original message: D(ℰ(m,k),k) = m
                                            2. Security: a different key will yield a different result:  ∀k’. k’ ≠ k ⟶ D(ℰ(m,k),k’) ≠ m
                                        4. Symmetric Cryptography
                                            1. Different types:
                                                1. Caesar’s cipher:
                                                    1. Simply have two wheels with letters that must be aligned correctly to decipher the message
                                                    2. Simple and can be brute forced by looking at frequencies of letters
                                                2. Perfect Secrecy – One-time Pad
                                                    1. Utilize XOR for encryption and decryption
                                                        1. Convert message to binary
                                                        2. XOR binary string with key binary-string
                                                        3. Decrypt by reusing XOR key on resulting string
                                                    2. Can only be used once, cause you can brute force the key
        - Block Cipher
            1. Divide plaintext into fixed-size blocks
            2. Generate a secret key to encrypt/decrypt
            3. Perform XOR on the plaintext blocks 1 or more times
            4. The result is the ciphertext
            5. Apply the reverse operations for the key on each block to decipher
        1. AES – an advanced block cipher
            1. Has the following extra steps:
                1. Byte substitution layer – S-box mix of bytes
                2. Diffusion layer – Shift rows and columns
                3. Key Addition layer – XOR the different Bytes
            2. Hash Functions
                1. takes an arbitrary block of data and returns a fixed-size bit string
                2. Hashes the value
            3. MAC – Message Authentication Codes
                1. Adds integrity and Authenticity
                2. Steps:
                    1. Select secret key -
                    2. Prepare message
                        1. Add padding to ensure it’s a multiple of the MAC algorithm block size
                    3. HASH Function
                        1. Combine message and secret key to generate the MAC
                        2. Apply hash function to the new message
                    4. MAC verification
                        1. Use same key and MAC algorithm to decrypt
                        2. Compare calculated MAC to the received MAC from the message
        - If same = authentic. Else it has been tampered with
        1. Asymmetric Cryptography
            1. The public key can be used to create a ciphertext by encrypting a plaintext.  The secret key can be used to decrypt the ciphertext back to plaintext.
            2. Key Exchange to allow for symmetric cryptography:
                1. Diffie-Helmann key exchange
                    1. secure under the Computational Diffie-Hellman assumption:
                        1. 
                    2. Steps, sender S, receiver R
                        1. S and R agree on a prime number ‘p’ and base ‘g’
                        2. Both generate random private keys, s and r
                        3. Both generate public keys as S = and R=
                        4. Each participant send their public key to the other
                        5. Each participant calculates a shared key using their private key and the other’s public key
                            1. Sender:
                            2. Receiver:
                        6. Shared key can now be used for encryption and decryption
                    3. Different types
                        1. RSA Encryption
                        2. El Gamal Encryption – built on the principle of Diffie hellman
                            1. Steps:
                                1. Encryption
                                    1. Sender, s, and Receiver, r, agrees on generator g, and prime, p
                                    2. Both generate a private and public key
        - Exchange public keys
        1. s represents the message, m, as an integer
        2. s calculates c1=g^k (mod p)
        3. s calculates c2 = m*h^k (mod p), where h is the public key of r
        - s sends the ciphertext as a touple (c1, c2) to r
        1. Decryption
            1. r receives ciphertext (c1, c2)
            2. r calculates k = c1^x (mod p), where x is r’s private key
        - r receives the message by calculating  m = c2 * (c1^x)^-1 (mod p)
        - Digital Signatures
            1. Adds integrity + authenticity
            2. Steps:
                1. Secret key to create signature
                2. Public/Verification key to verify signature
                3. Create signature: q = sign(m, sk)
                4. Verify signature: d = ver(q, m, vk)
            3. For El gamal
                1. Key generation
                    1. Choose a random secret key
                    2. Compute private key: pk = g^(sk) mod p
                2. Signature
                    1. Choose random integer k such that k is relatively prime to p-1
                    2. compute r=g^k mod p
        - compute s = (H(m)-sk ·r)k^(-1) mod (p-1),  if s=0, go to step 1
        1. output (r,s)
        2. Verification
            1. Check that 0<r<p and 0<s<p-1
            2. Check that
        - Output 1 if and only if all checks pass, output 0 otherwise
        
        # Secure Channels – Need more 9:23
        
        1. What are secure channels
            - a communication path between two parties that is protected against unauthorized access, interception, modification, or tampering
            - Purpose
                - used to maintain our security goals of Confidentiality, Integrity, and Availability
                - Protects against attacks
                    - Eavesdropping
                    - Data-tampering
                    - Man-in-the-middle attacks
        2. Types of secure channels – Explain them briefly
            - VPNs
                - Creates a secure connection to a network rather than a website
                - Uses authentication and encryption
                - Encrypts all communication between the two systems
            - SSL – Older version of TLS, with weaker algorithms
            - TLS
                - Handshake protocol steps
                    - Client sends “hello” – gives cryptographic algorithms and protocols that it supports
                    - Server hello – informs of selected algorithm and protocol + a random number(server nonce)
                    - Server sends public key
                    - Client generates own random number(client nonce) and uses it and the server nonce to create a **premaster secret**
                    - Client encrypts and sends premaster secret to server
                    - Server decrypts by using its private key and generates a session key for further communication
                    - Server sends session key and “finished” to client
                    - Client replies with “finished” when session key is received
                - Alert protocol
                    - Fatal alert – e.g. incorrect MAC or unexpected message
                    - Warning alerts – Certificate issues
                - Heartbeat protocol
                    - Pings the peer to keep connection open
                - HTTPS Steps ????????
                    - Establishes TCP connection
                    - Checks certificates
                    - TLS
        3. Role of public key infrastructure(PKI)
            - Digital certificates
                - contains information about the identity of the website or individual and the public key associated with their digital signature
                - used to validate the authenticity of the parties involved in the communication.
                - issued by trusted third-party organizations known as certificate authorities (CAs)
                - Online Certificate Status Protocol(OCSP)
                    - An Internet standard to validate another participant through a third party CA
                    - CRL lists are regularly checked and cached in case the CA isn’t available when needed and to reduce latency
                - Certificate Revocation List (CRL)
                    - lists of certificates not to be used
                    - Signed by the same CA who issued the certificates
                    - Browsers periodically access CA servers to fetch recent CRLs
                - How to identify a compromised CA ????????????
                    - Audit proofs
                - Root certification Authority
                    - Signs other CA’s certificates
                    - Signs its own certificate
                - Certificate transparency
                    - a mechanism for publicly logging all a CA’s SSL/TLS certificates
                    - to provide a way to detect and prevent the issuance of fraudulent or unauthorized SSL/TLS certificates
                    - 
        4. Threats to secure channels
            - DOS attacks
        
        # Penetration Testing - decent 09:50
        
        1. What is pentesting
            1. a type of security testing that involves identifying and exploiting vulnerabilities in a computer system or network in order to evaluate its security.
            2. The goal of pen testing is to simulate a real-world attack and determine the potential risks and impact of a successful attack.
        2. Types of testing
            1. Black box testing – no knowledge of the inner working
            2. White box testing – Full knowledge of the inner workings
            3. Grey box testing – Some knowledge of the system but not full access
        3. How is it carried out
            1. HTTP requests
                1. Injection attacks
                    1. SQL injection
                        1. Query “SELECT * FROM users”
                        2. Username = ‘something’ OR 1=1
                    2. Command injection
                2. Cross-site scripting attacks(XSS) – HTML injection
                    1. Malicious code is injected into a vulnerable web application
                    2. When someone connects to the server, the malicious code is passed to their browser
                3. Steps of pentesting
                    1. Information gathering
                        1. Gathering information
                            1. IP addresses, System architecture, OS, etc.
                        2. Black box audit - assess the system's security posture
                    2. Vulnerability analysis
                        1. Using collected data to find vulnerabilities
                    3. Initial access
                        1. Utilising weaknesses to gain access
                        2. Fx. Guessing passwords or SQL injections
        - Cross-site scripting
        1. Privilege Escalation
            1. Why?
                1. Read/Write anything
                2. Permanent backdoor
            2. How
                1. Kernel exploits
                2. Services running on root
            3. Maintain Access and cover tracks
                1. Install rootkit
                2. Deleting log files
        - Monitoring the system
            1. Network sniffers or port scanners to monitor traffic and detect vulnerabilities
        1. System hardening
            1. The process of securing a computer system by reducing its vulnerability to attacks
            2. The purpose is to make it hard for attackers to gain access or exploit weaknesses
            3. Steps
                1. Updating software – make sure latest security patches are installed
                2. Disabling unnecessary services – Reduces the attack surface and makes it harder to find and exploit vulnerabilities
        - Configuring user accounts and access controls
            1. 2-step authentication
            2. Strong password rules
            3. Limiting user access to minimum required rights
        1. Configuring firewalls and intrusion detection systems to avoid initial access
        2. Encrypting data – protects sensitive data
        3. Regular monitoring and testing – penetration testing regularly to find weaknesses
        
        Notes:
        
        Layers(NOT NECESSARY):
        
        - Physical layer:
            - Transmission of binary data across a physical link
            - Actual physical aspects such as messages running through cables
            - Infrastructure broadcasting messages.
            - Servers and databases
            - Vulnerable to:
                - Eavesdropping
                - Tampering
                - DOS
                - Message injection
            - Data-link layer:
                - Transmission of packets between hosts connected by a physical link
                - The data communication, aka what happens with the messages and how they’re handled
                - Vulnerable to:
                    - Tampering
                    - Message injection/MAC spoofing
                    - Eavesdropping
                - Network Layer
                    - IP protocols – how messages through the Data-link layer are received and sent between participants
                    - Vulnerable to:
                        - ARP Cache Spoofing: Redirecting traffic from an IP to another machine
                        - IP Spoofing: Faking IP to make an internet router send a response to the faked ID – can be used to send a lot of requests and the responses then flood a target server.
                        - DHCP Starvation:
                    - Transport layer
                        - Connection-oriented, reliable, streaming protocol – protocols for how packages of data are transmitted
                    - Application Layer
                        - ensures an application can effectively communicate with other applications on different computer systems and networks.
                        - specifies the shared communications protocols and interface methods used by hosts in a communications network.