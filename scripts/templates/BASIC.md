# Various NIST 800-53 Controls Provided by Drupal Plugins

## Controls
{% for control in controls.keys() %}
### {{ controls[control].id }} - {{ controls[control].title }}
{% for text in controls[control].texts %}
{{ text }}
{% endfor %}{% endfor %}

## Updating this document
This document was generated using [OpenControl](http://open-control.org) and [ComplianceLib](https://github.com/GovReady/compliancelib-python). 

To request modifications, please make a pull request or open a [new issue](https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls/issues) at the source repository [https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls](https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls). Script generating this document is [script/doc_basic.py](https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls/blob/master/scripts/doc_basic.py).
