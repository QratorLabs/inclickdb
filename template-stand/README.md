### Graphite -> Clickhouse template demo

Based on [Automated demo](https://github.com/QratorLabs/inclickdb/blob/master/demo/README.md).

Is using [fork](https://github.com/mary3000/carbon-clickhouse) of carbon-clickhouse with the changes in this [pull-request](https://github.com/lomik/carbon-clickhouse/pull/32).  
New feature: graphite templates from [influxdb](https://docs.influxdata.com/influxdb/v1.7/supported_protocols/graphite/).  
You can specify filters and templates for tag matching in `carbon-clichkouse.conf` in `[convert_to_tagged]` section.  
Example:  
```
[convert_to_tagged]
 enabled = true
 separator = "_"
 templates = [
     "generated.* .measurement.cpu  metric=idle",
     "* host.measurement* template_match=none",
 ]
```