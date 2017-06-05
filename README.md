# Drupal Projects Compliance Controls

This repository contains compliance information for various Drupal projects commonly used to harden a Drupal instance to meet various NIST SP 800-53 described security controls.

This data adheres to the OpenControl schema for building compliance documentation and can be used to support your own authority to operate (ATO) review process. The documentation generated from this content can be used to assist your organization in authorizing Drupal. For more information, visit [http://open-control.org](http://open-control.org).

> This content is provided for informational purposes only and has not been vetted by any third-party security assessors. You are solely responsible for developing, implementing, and managing your applications and/or subscriptions running on your own platform in compliance with applicable laws, regulations, and contractual obligations. The documentation is provided "as-is" and without any warranty of any kind, whether express, implied or statutory, and Docker, Inc. expressly disclaims all warranties for non-infringement, merchantability or fitness for a particular purpose.

## Summary of projects and related controls

| Drupal Project          | 800-53 Control                          |
|-------------------------|-----------------------------------------|
|Automated Logout         | AC-12 Session Termination               |
|Flood-control            | SC-5 Denial Of Service Protection       |
|Session Limit            | AC-12  Session Termination              |
|TFA                      | AC-2 Account Management; AC-6 Least Privilege; (SI-7) Software, Firmware, And Information Integrity - b/c preventing user to escalate privilege   |
|Paranoia                 | AC-6(1) Least Privilege - Authorize Access To Security Functions |
|Watchdog                 | AU-2 Audit Events; AU-3 Content Of Audit Records; AU-7 Audit Reduction And Report Generation; AU-8 Time Stamps; AU-9 Protection Of Audit Information; AU-14 Session Audit;  |
|Ejector Seat             | AC-12 Session Termination?              |
|GovReady                 | ?CDM, patching                          |

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
    - url: https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls
      revision: master
```


