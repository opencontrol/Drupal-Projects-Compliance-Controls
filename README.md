# Drupal Projects Compliance Controls

This repository contains compliance information for various Drupal projects commonly used to harden a Drupal instance to meet various NIST SP 800-53 described security controls.

This data adheres to the OpenControl schema for building compliance documentation and can be used to support your own authority to operate (ATO) review process. The documentation generated from this content can be used to assist your organization in authorizing Drupal. For more information, visit [http://open-control.org](http://open-control.org).

> This content is provided for informational purposes only and has not been vetted by any third-party security assessors. You are solely responsible for developing, implementing, and managing your applications and/or subscriptions running on your own platform in compliance with applicable laws, regulations, and contractual obligations. The documentation is provided "as-is" and without any warranty of any kind, whether express, implied or statutory, and Docker, Inc. expressly disclaims all warranties for non-infringement, merchantability or fitness for a particular purpose.

## Summary of projects and related controls

| Drupal Project          | 800-53 Control                           |
|-------------------------|------------------------------------------|
| [Automated Logout](https://www.drupal.org/project/autologout)      | [AC-12](https://nvd.nist.gov/800-53/Rev4/control/AC-12) Session Termination              |
| [Ejector Seat](https://www.drupal.org/project/ejectorseat)         | [AC-12](https://nvd.nist.gov/800-53/Rev4/control/AC-12) Session Termination              |
| [Flood-control](https://www.drupal.org/project/flood_control)      | [SC-5](https://nvd.nist.gov/800-53/Rev4/control/SC-5) Denial Of Service Protection       |
| [GovReady](https://www.drupal.org/project/govready)                | [AC-2 (f)](https://nvd.nist.gov/800-53/Rev4/control/AC-2) Account Management; [MA-1](https://nvd.nist.gov/800-53/Rev4/control/MA-1) System Maintenance Policy and Procedures; [MA-2](https://nvd.nist.gov/800-53/Rev4/control/MA-2) Controlled Maintenance; [MA-6](https://nvd.nist.gov/800-53/Rev4/control/MA-6) Timely Maintenance |
| [Password Policy](https://www.drupal.org/project/password_policy)  | [AC-3](https://nvd.nist.gov/800-53/Rev4/control/AC-3) Access Enforcement |
| [Paranoia](https://www.drupal.org/project/paranoia)                | [AC-6(1)](https://nvd.nist.gov/800-53/Rev4/control/AC-6) Least Privilege - Authorize Access To Security Functions |
| [Security Kit](https://www.drupal.org/project/seckit)              | [SC-4](https://nvd.nist.gov/800-53/Rev4/control/SC-4) Information in Shared Resources; [SC-8](https://nvd.nist.gov/800-53/Rev4/control/SC-8) Transmission Confidentiality and Integrity; [SC-11](https://nvd.nist.gov/800-53/Rev4/control/SC-11) Trusted Path; [SC-23](https://nvd.nist.gov/800-53/Rev4/control/SC-23) Session Authenticity; |
| [Security Review](https://www.drupal.org/project/security_review)  | [AC-4](https://nvd.nist.gov/800-53/Rev4/control/AC-4) Information Flow Enforcement; [AC-6](https://nvd.nist.gov/800-53/Rev4/control/AC-6) Least Privilege; [CM-6](https://nvd.nist.gov/800-53/Rev4/control/CM-6) Configuration Settings; [CM-7](https://nvd.nist.gov/800-53/Rev4/control/CM-7) Least Functionality) |
| [Session Limit](https://www.drupal.org/project/session_limit)      | [AC-12](https://nvd.nist.gov/800-53/Rev4/control/AC-12) Session Termination              |
| [TFA](https://www.drupal.org/project/tfa)                          | [AC-2](https://nvd.nist.gov/800-53/Rev4/control/AC-2) Account Management; AC-6 Least Privilege;
| [Watchdog](https://www.drupal.org/project/ejectorseat) / [dblog](https://www.drupal.org/docs/8/core/modules/dblog/overview)  | [AU-2](https://nvd.nist.gov/800-53/Rev4/control/AU-2) Audit Events; [AU-3](https://nvd.nist.gov/800-53/Rev4/control/AU-3) Content Of Audit Records; [AU-7](https://nvd.nist.gov/800-53/Rev4/control/AU-7) Audit Reduction And Report Generation; [AU-8](https://nvd.nist.gov/800-53/Rev4/control/AU-8) Time Stamps; [AU-9](https://nvd.nist.gov/800-53/Rev4/control/AU-9) Protection Of Audit Information; [AU-14](https://nvd.nist.gov/800-53/Rev4/control/AU-14) Session Audit;  |


## How to use

### Docs with generated and paste text

The `docs/` directory contains generated documents from which you can copy text.

* [BASIC.md](docs/BASIC.md) - A basic listing of controls supported by Drupal projects tracked in this repository

### Scripts to generate documents

The `scripts/` directory contains ready-to-run python scripts to generate various documents from Jinja2 templates in the `scripts/templates/` directory.

### Using in OpenControl files

You can include this repository as a dependency by adding the appropriate lines from the below snippet to your `opencontrol.yaml` file:

```
dependencies:
  systems:
    - url: https://github.com/opencontrol/Drupal-Projects-Compliance-Controls
      revision: master
```


