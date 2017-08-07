# Various NIST 800-53 Controls Provided by Drupal Projects

## Controls

### AC-12 - SESSION TERMINATION

The Drupal project "Automated Logout" provides Drupal site administrators the ability to log users out after a specified time of inactivity. 

The Drupal project "Ejector Seat" provides Javascript Ajax code that periodically checks to see if users are still logged in. If it is determined the user is not logged in, the client side code reloads the current page so the user sees as would an anonymous user. 

The Drupal project "Session Limit" enables Drupal administrators to set limits on the number of simultaneous sessions for each user. 

### AU-14 - SESSION AUDIT

The Drupal Logging API, informally known as Watchdog, supports the integrity of software and information by reducing the risk of attackers gaining access to the system via theft of username and passwords and preventing ordinary users escalating privileges. 

### AU-3 - CONTENT OF AUDIT RECORDS

The Drupal Logging API, informally known as Watchdog, supports least privilege by upgrading Drupal's standard username and password login to two-factor authentication via a various two-factor authentication. 

### AC-4 - INFORMATION FLOW ENFORCEMENT

The Drupal project "Security Review" contributes to information flow enforcement at the application layer by checking access control to information views to protect against information disclosure. For a complete list of features see [Project Security Review documentation](https://www.drupal.org/project/security_review). 

### AC-6 (1) - AUTHORIZE ACCESS TO SECURITY FUNCTIONS

The Drupal project "Paranoia" supports least privilege by blocking any location within the Drupal interface the project finds where a user can evaluate (e.g., run) PHP code. This limits the ability of an individual gaining elevated permission. 

### SC-5 - DENIAL OF SERVICE PROTECTION

The Drupal project "Flood Control" provides Drupal administrators with an interface to configure flood controls variable sin Drupal 7, such as the limiter for login attempts. 

### AU-2 - AUDIT EVENTS

The Drupal Logging API, informally known as Watchdog, improves account management by upgrading Drupal's standard username and password login to two-factor authentication via a various two-factor authentication. 

### AU-9 - PROTECTION OF AUDIT INFORMATION

The Drupal Logging API, informally known as Watchdog, supports the integrity of software and information by reducing the risk of attackers gaining access to the system via theft of username and passwords and preventing ordinary users escalating privileges. 

### CM-6 - CONFIGURATION SETTINGS

The Drupal project "Security Review" contributes to minitoring and controlling changes to configuration settings at the application layer by checking Drupal configuration settings for errors that can make the site less secure or disclosure information. For a complete list of features see [Project Security Review documentation](https://www.drupal.org/project/security_review). 

### SC-23 - SESSION AUTHENTICITY

The Drupal project "Security Kit" contributes significantly to session authenticity at the application layer at the application layer by preventing cross-site request forgeries and scripting, click-jacking, incorrect HTTP headers. Security Kit implements HTTP Strict Transport Security (HSTS) response header that prevent man-in-the-middle attacks.  For a complete list of features see [Project Security Kit documentation](https://www.drupal.org/project/seckit). 

### SC-11 - TRUSTED PATH

The Drupal project "Security Kit" improves trusted path in sessions with end-users at the application layer by implementing HTTP Strict Transport Security (HSTS) response header that prevent man-in-the-middle attacks. For a complete list of features see [Project Security Kit documentation](https://www.drupal.org/project/seckit). 

### MA-1 - SYSTEM MAINTENANCE POLICY AND PROCEDURES

The Drupal project "GovReady Dashboard" provides a Drupal Administration dashboard that aggregates, documents and dissiminates to administrators essential information regarding maintenance of Drupal application, security updates, and plugin updates. 

### AU-8 - TIME STAMPS

The Drupal Logging API, informally known as Watchdog, supports the integrity of software and information by reducing the risk of attackers gaining access to the system via theft of username and passwords and preventing ordinary users escalating privileges. 

### SC-4 - INFORMATION IN SHARED RESOURCES

The Drupal project "Security Kit" helps control information in shared resources at the application layer by preventing unauthorized and unintended information transfers that can occur from cross-site request forgeries and scripting, click-jacking, and other incorrect HTTP headers.  For a complete list of features see [Project Security Kit documentation](https://www.drupal.org/project/seckit). 

### AC-3 - ACCESS ENFORCEMENT

The Drupal project "Password Policy" allows administrators to define and enforce user password policies.  Limitations - "Password policies only apply to passwords set via user forms in the web interface. Passwords changed by other means (Drush, web services, etc.) may not be subject to password policy constraints. Please see the following issue if you would like to contribute to removing this limitation: #2451159: Password policy doesn't work when updating the user" ([Project Password Policy](https://www.drupal.org/project/password_policy))

### AC-6 - LEAST PRIVILEGE

The Drupal project, "Two-factor Authentication (TFA)" supports least privilege by upgrading Drupal's standard username and password login to two-factor authentication via a various two-factor authentication. 

The Drupal project "Security Review" helps ensure least privilege at the application layer  is followed by checking proper Drupal admininstration permissions; checking file system permissions to protect against executing arbitrary files; prevention of dangerous HTML tags to prevent cross-site scripting; and limit file upload extentions. For a complete list of features see [Project Security Review documentation](https://www.drupal.org/project/security_review). 

### CM-7 - LEAST FUNCTIONALITY

The Drupal project "Security Review" contributes to configuration for least functionality at the application layer by checking Drupal configuration settings for arbitrary PHP execution, private files are properly secure, safe error reporting is set, and Drupal administration permissions are not misconfigured. For a complete list of features see [Project Security Review documentation](https://www.drupal.org/project/security_review). 

### MA-2 - CONTROLLED MAINTENANCE

The Drupal project "GovReady Dashboard" provides a Drupal Administration dashboard that allows maintenance activities to be scheduled, documented as maintenance records, and reviewed by system administrators. 

### AC-2 - ACCOUNT MANAGEMENT

The Drupal project, "Two-factor Authentication (TFA)" improves account management by upgrading Drupal's standard username and password login to two-factor authentication via a various two-factor authentication. 

### SC-8 - TRANSMISSION CONFIDENTIALITY AND INTEGRITY

The Drupal project "Security Kit" controls transmission confidentiality and integrity at the application layer by preventing cross-site request forgeries and scripting, click-jacking, incorrect HTTP headers. Security Kit implements HTTP Strict Transport Security (HSTS) response header that prevent man-in-the-middle attacks. For a complete list of features see [Project Security Kit documentation](https://www.drupal.org/project/seckit). 

### AU-7 - AUDIT REDUCTION AND REPORT GENERATION

The Drupal Logging API, informally known as Watchdog, supports the integrity of software and information by reducing the risk of attackers gaining access to the system via theft of username and passwords and preventing ordinary users escalating privileges. 


## Updating this document
This document was generated using [OpenControl](http://open-control.org) and [ComplianceLib](https://github.com/GovReady/compliancelib-python). 

To request modifications, please make a pull request or open a [new issue](https://github.com/opencontrol/Drupal-Projects-Compliance-Controls/issues) at the source repository [https://github.com/opencontrol/Drupal-Projects-Compliance-Controls](https://github.com/opencontrol/Drupal-Projects-Compliance-Controls). Script generating this document is [script/doc_basic.py](https://github.com/opencontrol/Drupal-Projects-Compliance-Controls/blob/master/scripts/doc_basic.py).