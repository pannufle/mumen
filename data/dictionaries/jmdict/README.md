# DOWNLOAD JMDict
Download and extract in the folder ```data/jmdict/dicts/``` the JMDict dictionaries from:
http://edrdg.org/jmdict/edict_doc.html

The DTD file was downloaded from [here](http://edrdg.org/jmdict/jmdict_dtd_h.html)

The XSD schema file was generated via the [W3C dtd2xsd.pl](https://www.w3.org/2000/04/schema_hack/) script via:
```
perl dtd2xsd.pl jmdict.dtd > jmdict.xsd
```
and replacing `xmlns='http://www.w3.org/2000/10/XMLSchema'` by `xmlns='http://www.w3.org/2001/XMLSchema'`

The PyXB `jmdict.py` marshalling/unmarshalling model is then generated via:
```
pyxbgen -u jmdict.xsd -m jmdict
``
