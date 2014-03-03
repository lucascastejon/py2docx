# coding: utf-8


class Block(object):

    def __init__(self, align=None):
        self.content = ""
        self.align = align
        self.href_list_elem = []
        self.xml_string = '<w:p>' + \
                          '<w:pPr>' + \
                          '{properties}' + \
                          '</w:pPr>' + \
                          '{content}' + \
                          '</w:p>'
        self.xml_props = []
        self._set_properties()

    def _get_xml(self):
        return self.xml_string.format(content=self.content)

    def _set_properties(self):
        self._set_align()
        self.xml_string = self.xml_string.replace('{properties}',
                                                  ''.join(self.xml_props))

    def _set_align(self):
        if self.align and \
           self.align in ['left',
                          'right',
                          'center',
                          'justify']:

            xml = '<w:jc w:val="{align}"/>'
            self.xml_props.append(xml.format(align=self.align))

    def append(self, elem):
        self.content += elem._get_xml()
