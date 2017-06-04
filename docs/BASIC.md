# Various NIST 800-53 Controls Provided by Drupal Plugins

## Controls

### AC-12 - SESSION TERMINATION

The Automated Logout plugin provides Drupal site administrators the ability to log users out after a specified time of inactivity. 

The Session Limit plugin enables Drupal administrators to set limits on the number of simultaneous sessions for each user. 

### SC-5 - DENIAL OF SERVICE PROTECTION

The Flood Control plugin provides Drupal administrators with an interface to configure flood controls variable sin Drupal 7, such as the limiter for login attempts. 

### SI-7 - SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY

The Two-factor Authentication (TFA) Drupal plugin supports the integrity of software and information by reducing the risk of attackers gaining access to the system via theft of username and passwords and preventing ordinary users escalating privileges.

### AC-6 (1) - AUTHORIZE ACCESS TO SECURITY FUNCTIONS

The Paranoia plugin supports least privilege by blocking any location within the Drupal interface the plugin finds where a user can evaluate (e.g., run) PHP code. This limits the ability of an individual gaining elevated permission. 

### AC-6 - LEAST PRIVILEGE

The Two-factor Authentication (TFA) Drupal plugin supports least privilege by upgrading Drupal's standard username and password login to two-factor authentication via a various two-factor authentication. 

### AC-2 - ACCOUNT MANAGEMENT

The Two-factor Authentication (TFA) Drupal plugin improves account management by upgrading Drupal's standard username and password login to two-factor authentication via a various two-factor authentication. 


## Updating this document
This document was generated using [OpenControl](http://open-control.org) and [ComplianceLib](https://github.com/GovReady/compliancelib-python). 

To request modifications, please make a pull request or open a [new issue](https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls/issues) at the source repository [https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls](https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls). Script generating this document is [script/doc_basic.py](https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls/blob/master/scripts/doc_basic.py).