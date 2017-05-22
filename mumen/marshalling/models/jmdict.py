# pylint: skip-file
# ./jmdict.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ebbf774871f192c2de1fec8148b93246a5155d8e
# Generated 2017-05-15 09:45:40.433307 by PyXB version 1.2.5 using Python 3.6.1.final.0
# Namespace http://edrdg.org/

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    'urn:uuid:7e102fcc-3942-11e7-ae40-80e650171a40')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    'http://edrdg.org/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])


def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://edrdg.org/}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpedrdg_org_CTD_ANON_httpedrdg_orgentry',
                                                      True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 14, 1), )

    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name(): __entry
    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://edrdg.org/}ent_seq uses Python identifier ent_seq
    __ent_seq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'ent_seq'), 'ent_seq', '__httpedrdg_org_CTD_ANON__httpedrdg_orgent_seq', False, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 25, 1), )

    ent_seq = property(__ent_seq.value, __ent_seq.set, None, None)

    # Element {http://edrdg.org/}k_ele uses Python identifier k_ele
    __k_ele = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'k_ele'), 'k_ele', '__httpedrdg_org_CTD_ANON__httpedrdg_orgk_ele',
                                                      True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 30, 1), )

    k_ele = property(__k_ele.value, __k_ele.set, None, None)

    # Element {http://edrdg.org/}r_ele uses Python identifier r_ele
    __r_ele = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'r_ele'), 'r_ele', '__httpedrdg_org_CTD_ANON__httpedrdg_orgr_ele',
                                                      True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 55, 1), )

    r_ele = property(__r_ele.value, __r_ele.set, None, None)

    # Element {http://edrdg.org/}sense uses Python identifier sense
    __sense = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sense'), 'sense', '__httpedrdg_org_CTD_ANON__httpedrdg_orgsense',
                                                      True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 92, 1), )

    sense = property(__sense.value, __sense.set, None, None)

    _ElementMap.update({
        __ent_seq.name(): __ent_seq,
        __k_ele.name(): __k_ele,
        __r_ele.name(): __r_ele,
        __sense.name(): __sense
    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type MIXED
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 26, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 31, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://edrdg.org/}keb uses Python identifier keb
    __keb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'keb'), 'keb', '__httpedrdg_org_CTD_ANON_3_httpedrdg_orgkeb',
                                                    False, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 40, 1), )

    keb = property(__keb.value, __keb.set, None, None)

    # Element {http://edrdg.org/}ke_inf uses Python identifier ke_inf
    __ke_inf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ke_inf'), 'ke_inf', '__httpedrdg_org_CTD_ANON_3_httpedrdg_orgke_inf',
                                                       True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 45, 1), )

    ke_inf = property(__ke_inf.value, __ke_inf.set, None, None)

    # Element {http://edrdg.org/}ke_pri uses Python identifier ke_pri
    __ke_pri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ke_pri'), 'ke_pri', '__httpedrdg_org_CTD_ANON_3_httpedrdg_orgke_pri',
                                                       True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 50, 1), )

    ke_pri = property(__ke_pri.value, __ke_pri.set, None, None)

    _ElementMap.update({
        __keb.name(): __keb,
        __ke_inf.name(): __ke_inf,
        __ke_pri.name(): __ke_pri
    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type MIXED
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 41, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type MIXED
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 46, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type MIXED
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 51, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 56, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://edrdg.org/}reb uses Python identifier reb
    __reb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reb'), 'reb', '__httpedrdg_org_CTD_ANON_7_httpedrdg_orgreb',
                                                    False, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 67, 1), )

    reb = property(__reb.value, __reb.set, None, None)

    # Element {http://edrdg.org/}re_nokanji uses Python identifier re_nokanji
    __re_nokanji = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 're_nokanji'), 're_nokanji', '__httpedrdg_org_CTD_ANON_7_httpedrdg_orgre_nokanji', False, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 72, 1), )

    re_nokanji = property(__re_nokanji.value, __re_nokanji.set, None, None)

    # Element {http://edrdg.org/}re_restr uses Python identifier re_restr
    __re_restr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 're_restr'), 're_restr', '__httpedrdg_org_CTD_ANON_7_httpedrdg_orgre_restr', True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 77, 1), )

    re_restr = property(__re_restr.value, __re_restr.set, None, None)

    # Element {http://edrdg.org/}re_inf uses Python identifier re_inf
    __re_inf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 're_inf'), 're_inf', '__httpedrdg_org_CTD_ANON_7_httpedrdg_orgre_inf',
                                                       True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 82, 1), )

    re_inf = property(__re_inf.value, __re_inf.set, None, None)

    # Element {http://edrdg.org/}re_pri uses Python identifier re_pri
    __re_pri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 're_pri'), 're_pri', '__httpedrdg_org_CTD_ANON_7_httpedrdg_orgre_pri',
                                                       True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 87, 1), )

    re_pri = property(__re_pri.value, __re_pri.set, None, None)

    _ElementMap.update({
        __reb.name(): __reb,
        __re_nokanji.name(): __re_nokanji,
        __re_restr.name(): __re_restr,
        __re_inf.name(): __re_inf,
        __re_pri.name(): __re_pri
    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type MIXED
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 68, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type MIXED
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 73, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type MIXED
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 78, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type MIXED
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 83, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type MIXED
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 88, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 93, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://edrdg.org/}stagk uses Python identifier stagk
    __stagk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stagk'), 'stagk', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orgstagk',
                                                      True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 110, 1), )

    stagk = property(__stagk.value, __stagk.set, None, None)

    # Element {http://edrdg.org/}stagr uses Python identifier stagr
    __stagr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stagr'), 'stagr', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orgstagr',
                                                      True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 115, 1), )

    stagr = property(__stagr.value, __stagr.set, None, None)

    # Element {http://edrdg.org/}xref uses Python identifier xref
    __xref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xref'), 'xref', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orgxref',
                                                     True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 120, 1), )

    xref = property(__xref.value, __xref.set, None, None)

    # Element {http://edrdg.org/}ant uses Python identifier ant
    __ant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ant'), 'ant', '__httpedrdg_org_CTD_ANON_13_httpedrdg_organt',
                                                    True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 125, 1), )

    ant = property(__ant.value, __ant.set, None, None)

    # Element {http://edrdg.org/}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pos'), 'pos', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orgpos',
                                                    True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 130, 1), )

    pos = property(__pos.value, __pos.set, None, None)

    # Element {http://edrdg.org/}field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'field'), 'field', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orgfield',
                                                      True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 135, 1), )

    field = property(__field.value, __field.set, None, None)

    # Element {http://edrdg.org/}misc uses Python identifier misc
    __misc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'misc'), 'misc', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orgmisc',
                                                     True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 140, 1), )

    misc = property(__misc.value, __misc.set, None, None)

    # Element {http://edrdg.org/}lsource uses Python identifier lsource
    __lsource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'lsource'), 'lsource', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orglsource', True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 145, 1), )

    lsource = property(__lsource.value, __lsource.set, None, None)

    # Element {http://edrdg.org/}dial uses Python identifier dial
    __dial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dial'), 'dial', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orgdial',
                                                     True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 151, 1), )

    dial = property(__dial.value, __dial.set, None, None)

    # Element {http://edrdg.org/}gloss uses Python identifier gloss
    __gloss = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gloss'), 'gloss', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orggloss',
                                                      True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 156, 1), )

    gloss = property(__gloss.value, __gloss.set, None, None)

    # Element {http://edrdg.org/}s_inf uses Python identifier s_inf
    __s_inf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 's_inf'), 's_inf', '__httpedrdg_org_CTD_ANON_13_httpedrdg_orgs_inf',
                                                      True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 170, 1), )

    s_inf = property(__s_inf.value, __s_inf.set, None, None)

    _ElementMap.update({
        __stagk.name(): __stagk,
        __stagr.name(): __stagr,
        __xref.name(): __xref,
        __ant.name(): __ant,
        __pos.name(): __pos,
        __field.name(): __field,
        __misc.name(): __misc,
        __lsource.name(): __lsource,
        __dial.name(): __dial,
        __gloss.name(): __gloss,
        __s_inf.name(): __s_inf
    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type MIXED
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 111, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type MIXED
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 116, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type MIXED
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 121, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type [anonymous] with content type MIXED
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 126, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type MIXED
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 131, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type MIXED
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 136, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type [anonymous] with content type MIXED
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 141, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type [anonymous] with content type MIXED
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 146, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute ls_wasei uses Python identifier ls_wasei
    __ls_wasei = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(
        None, 'ls_wasei'), 'ls_wasei', '__httpedrdg_org_CTD_ANON_21_ls_wasei', pyxb.binding.datatypes.string)
    __ls_wasei._DeclarationLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 147, 3)
    __ls_wasei._UseLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 147, 3)

    ls_wasei = property(__ls_wasei.value, __ls_wasei.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __ls_wasei.name(): __ls_wasei
    })


_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type MIXED
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 152, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type [anonymous] with content type MIXED
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 157, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://edrdg.org/}pri uses Python identifier pri
    __pri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pri'), 'pri', '__httpedrdg_org_CTD_ANON_23_httpedrdg_orgpri',
                                                    True, pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 165, 1), )

    pri = property(__pri.value, __pri.set, None, None)

    # Attribute g_gend uses Python identifier g_gend
    __g_gend = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(
        None, 'g_gend'), 'g_gend', '__httpedrdg_org_CTD_ANON_23_g_gend', pyxb.binding.datatypes.string)
    __g_gend._DeclarationLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 161, 3)
    __g_gend._UseLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 161, 3)

    g_gend = property(__g_gend.value, __g_gend.set, None, None)

    _ElementMap.update({
        __pri.name(): __pri
    })
    _AttributeMap.update({
        __g_gend.name(): __g_gend
    })


_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


# Complex type [anonymous] with content type MIXED
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 166, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_24 = CTD_ANON_24


# Complex type [anonymous] with content type MIXED
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 171, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


_module_typeBindings.CTD_ANON_25 = CTD_ANON_25


JMdict = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JMdict'), CTD_ANON, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 6, 1))
Namespace.addCategoryObject(
    'elementBinding', JMdict.name().localName(), JMdict)

entry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), CTD_ANON_, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 14, 1))
Namespace.addCategoryObject('elementBinding', entry.name().localName(), entry)

ent_seq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ent_seq'), CTD_ANON_2, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 25, 1))
Namespace.addCategoryObject(
    'elementBinding', ent_seq.name().localName(), ent_seq)

k_ele = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'k_ele'), CTD_ANON_3, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 30, 1))
Namespace.addCategoryObject('elementBinding', k_ele.name().localName(), k_ele)

keb = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'keb'), CTD_ANON_4, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 40, 1))
Namespace.addCategoryObject('elementBinding', keb.name().localName(), keb)

ke_inf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ke_inf'), CTD_ANON_5, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 45, 1))
Namespace.addCategoryObject(
    'elementBinding', ke_inf.name().localName(), ke_inf)

ke_pri = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ke_pri'), CTD_ANON_6, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 50, 1))
Namespace.addCategoryObject(
    'elementBinding', ke_pri.name().localName(), ke_pri)

r_ele = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'r_ele'), CTD_ANON_7, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 55, 1))
Namespace.addCategoryObject('elementBinding', r_ele.name().localName(), r_ele)

reb = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reb'), CTD_ANON_8, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 67, 1))
Namespace.addCategoryObject('elementBinding', reb.name().localName(), reb)

re_nokanji = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 're_nokanji'), CTD_ANON_9,
                                        location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 72, 1))
Namespace.addCategoryObject(
    'elementBinding', re_nokanji.name().localName(), re_nokanji)

re_restr = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 're_restr'), CTD_ANON_10,
                                      location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 77, 1))
Namespace.addCategoryObject(
    'elementBinding', re_restr.name().localName(), re_restr)

re_inf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 're_inf'), CTD_ANON_11, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 82, 1))
Namespace.addCategoryObject(
    'elementBinding', re_inf.name().localName(), re_inf)

re_pri = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 're_pri'), CTD_ANON_12, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 87, 1))
Namespace.addCategoryObject(
    'elementBinding', re_pri.name().localName(), re_pri)

sense = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sense'), CTD_ANON_13, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 92, 1))
Namespace.addCategoryObject('elementBinding', sense.name().localName(), sense)

stagk = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stagk'), CTD_ANON_14, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 110, 1))
Namespace.addCategoryObject('elementBinding', stagk.name().localName(), stagk)

stagr = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stagr'), CTD_ANON_15, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 115, 1))
Namespace.addCategoryObject('elementBinding', stagr.name().localName(), stagr)

xref = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xref'), CTD_ANON_16, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 120, 1))
Namespace.addCategoryObject('elementBinding', xref.name().localName(), xref)

ant = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ant'), CTD_ANON_17, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 125, 1))
Namespace.addCategoryObject('elementBinding', ant.name().localName(), ant)

pos = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pos'), CTD_ANON_18, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 130, 1))
Namespace.addCategoryObject('elementBinding', pos.name().localName(), pos)

field = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'field'), CTD_ANON_19, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 135, 1))
Namespace.addCategoryObject('elementBinding', field.name().localName(), field)

misc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'misc'), CTD_ANON_20, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 140, 1))
Namespace.addCategoryObject('elementBinding', misc.name().localName(), misc)

lsource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lsource'), CTD_ANON_21, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 145, 1))
Namespace.addCategoryObject(
    'elementBinding', lsource.name().localName(), lsource)

dial = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dial'), CTD_ANON_22, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 151, 1))
Namespace.addCategoryObject('elementBinding', dial.name().localName(), dial)

gloss = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gloss'), CTD_ANON_23, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 156, 1))
Namespace.addCategoryObject('elementBinding', gloss.name().localName(), gloss)

pri = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pri'), CTD_ANON_24, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 165, 1))
Namespace.addCategoryObject('elementBinding', pri.name().localName(), pri)

s_inf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 's_inf'), CTD_ANON_25, location=pyxb.utils.utility.Location(
    '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 170, 1))
Namespace.addCategoryObject('elementBinding', s_inf.name().localName(), s_inf)


CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), CTD_ANON_, scope=CTD_ANON,
                                                location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 14, 1)))


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 9, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'entry')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 9, 4))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON._Automaton = _BuildAutomaton()


CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ent_seq'), CTD_ANON_2, scope=CTD_ANON_,
                                                 location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 25, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'k_ele'), CTD_ANON_3, scope=CTD_ANON_,
                                                 location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 30, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'r_ele'), CTD_ANON_7, scope=CTD_ANON_,
                                                 location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 55, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sense'), CTD_ANON_13, scope=CTD_ANON_,
                                                 location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 92, 1)))


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 18, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ent_seq')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'k_ele')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 18, 4))
    st_1 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'r_ele')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 19, 4))
    st_2 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'sense')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 20, 4))
    st_3 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_._Automaton = _BuildAutomaton_()


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_2._Automaton = _BuildAutomaton_2()


CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'keb'), CTD_ANON_4, scope=CTD_ANON_3,
                                                  location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 40, 1)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ke_inf'), CTD_ANON_5, scope=CTD_ANON_3,
                                                  location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 45, 1)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ke_pri'), CTD_ANON_6, scope=CTD_ANON_3,
                                                  location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 50, 1)))


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 34, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 35, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'keb')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 33, 4))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ke_inf')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 34, 4))
    st_1 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ke_pri')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 35, 4))
    st_2 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_3._Automaton = _BuildAutomaton_3()


def _BuildAutomaton_4():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_4._Automaton = _BuildAutomaton_4()


def _BuildAutomaton_5():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_5._Automaton = _BuildAutomaton_5()


def _BuildAutomaton_6():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_6._Automaton = _BuildAutomaton_6()


CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reb'), CTD_ANON_8, scope=CTD_ANON_7,
                                                  location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 67, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 're_nokanji'), CTD_ANON_9, scope=CTD_ANON_7,
                                                  location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 72, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 're_restr'), CTD_ANON_10, scope=CTD_ANON_7,
                                                  location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 77, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 're_inf'), CTD_ANON_11, scope=CTD_ANON_7,
                                                  location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 82, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 're_pri'), CTD_ANON_12, scope=CTD_ANON_7,
                                                  location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 87, 1)))


def _BuildAutomaton_7():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 59, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 60, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 61, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 62, 4))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'reb')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 58, 4))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 're_nokanji')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 59, 4))
    st_1 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 're_restr')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 60, 4))
    st_2 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 're_inf')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 61, 4))
    st_3 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 're_pri')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 62, 4))
    st_4 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_7._Automaton = _BuildAutomaton_7()


def _BuildAutomaton_8():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_8._Automaton = _BuildAutomaton_8()


def _BuildAutomaton_9():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_9._Automaton = _BuildAutomaton_9()


def _BuildAutomaton_10():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_10._Automaton = _BuildAutomaton_10()


def _BuildAutomaton_11():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_11._Automaton = _BuildAutomaton_11()


def _BuildAutomaton_12():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_12._Automaton = _BuildAutomaton_12()


CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stagk'), CTD_ANON_14, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 110, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stagr'), CTD_ANON_15, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 115, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xref'), CTD_ANON_16, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 120, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ant'), CTD_ANON_17, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 125, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pos'), CTD_ANON_18, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 130, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'field'), CTD_ANON_19, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 135, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'misc'), CTD_ANON_20, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 140, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lsource'), CTD_ANON_21, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 145, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dial'), CTD_ANON_22, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 151, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gloss'), CTD_ANON_23, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 156, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 's_inf'), CTD_ANON_25, scope=CTD_ANON_13,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 170, 1)))


def _BuildAutomaton_13():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 95, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 96, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 97, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 98, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 99, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 100, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 101, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 102, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 103, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 104, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 105, 4))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'stagk')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 95, 4))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'stagr')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 96, 4))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'pos')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 97, 4))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'xref')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 98, 4))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ant')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 99, 4))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'field')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 100, 4))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'misc')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 101, 4))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 's_inf')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 102, 4))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'lsource')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 103, 4))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'dial')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 104, 4))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'gloss')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 105, 4))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_13._Automaton = _BuildAutomaton_13()


def _BuildAutomaton_14():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_14._Automaton = _BuildAutomaton_14()


def _BuildAutomaton_15():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_15._Automaton = _BuildAutomaton_15()


def _BuildAutomaton_16():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_16._Automaton = _BuildAutomaton_16()


def _BuildAutomaton_17():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_17._Automaton = _BuildAutomaton_17()


def _BuildAutomaton_18():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_18._Automaton = _BuildAutomaton_18()


def _BuildAutomaton_19():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_19._Automaton = _BuildAutomaton_19()


def _BuildAutomaton_20():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_20._Automaton = _BuildAutomaton_20()


def _BuildAutomaton_21():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_21._Automaton = _BuildAutomaton_21()


def _BuildAutomaton_22():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_22._Automaton = _BuildAutomaton_22()


CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pri'), CTD_ANON_24, scope=CTD_ANON_23,
                                                   location=pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 165, 1)))


def _BuildAutomaton_23():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 158, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'pri')), pyxb.utils.utility.Location('/Users/AKB/GitHub/mumen/data/dictionaries/jmdict/jmdict.xsd', 159, 4))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_23._Automaton = _BuildAutomaton_23()


def _BuildAutomaton_24():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_24._Automaton = _BuildAutomaton_24()


def _BuildAutomaton_25():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_25._Automaton = _BuildAutomaton_25()
