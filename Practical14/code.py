import xml.dom.minidom as minidom
import xml.sax
import time

# 1. DOM
def find_max_is_a_dom(filename):
    start = time.time()
    dom = minidom.parse(filename)
    terms = dom.getElementsByTagName('term')
    ontology_info = {
        'molecular_function': {'max_is_a': 0, 'id': '', 'name': ''},
        'biological_process': {'max_is_a': 0, 'id': '', 'name': ''},
        'cellular_component': {'max_is_a': 0, 'id': '', 'name': ''}
    }
    for term in terms:
        ns = term.getElementsByTagName('namespace')[0].firstChild.data.strip()
        is_a_count = len(term.getElementsByTagName('is_a'))
        term_id = term.getElementsByTagName('id')[0].firstChild.data.strip()
        name = term.getElementsByTagName('name')[0].firstChild.data.strip()
        if ns in ontology_info and is_a_count > ontology_info[ns]['max_is_a']:
            ontology_info[ns]['max_is_a'] = is_a_count
            ontology_info[ns]['id'] = term_id
            ontology_info[ns]['name'] = name
    time_elapsed = time.time() - start
    return ontology_info, time_elapsed

# 2. SAX
class GoHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.in_term = False
        self.in_name = False
        self.in_namespace = False
        self.in_id = False

        self.current_is_a = 0
        self.current_namespace = ""
        self.current_id = ""
        self.current_name = ""

        self.ontology_info = {
            'molecular_function': {'max_is_a': 0, 'id': '', 'name': ''},
            'biological_process': {'max_is_a': 0, 'id': '', 'name': ''},
            'cellular_component': {'max_is_a': 0, 'id': '', 'name': ''}
        }

    def startElement(self, name, attrs):
        if name == 'term':
            self.in_term = True
            self.current_is_a = 0
            self.current_namespace = ""
            self.current_id = ""
            self.current_name = ""
        elif self.in_term and name == 'is_a':
            self.current_is_a += 1
        elif self.in_term and name == 'namespace':
            self.in_namespace = True
            self.acc_namespace = ""
        elif self.in_term and name == 'id':
            self.in_id = True
            self.acc_id = ""
        elif self.in_term and name == 'name':
            self.in_name = True
            self.acc_name = ""

    def endElement(self, name):
        if name == 'term':
            if self.current_namespace in self.ontology_info:
                info = self.ontology_info[self.current_namespace]
                if self.current_is_a > info['max_is_a']:
                    info['max_is_a'] = self.current_is_a
                    info['id'] = self.current_id
                    info['name'] = self.current_name
            self.in_term = False
        elif name == 'namespace':
            self.in_namespace = False
            if hasattr(self, 'acc_namespace'):
                self.current_namespace = self.acc_namespace.strip()
        elif name == 'id':
            self.in_id = False
            if hasattr(self, 'acc_id'):
                self.current_id = self.acc_id.strip()
        elif name == 'name':
            self.in_name = False
            if hasattr(self, 'acc_name'):
                self.current_name = self.acc_name.strip()

    def characters(self, content):
        if self.in_namespace:
            self.acc_namespace += content
        if self.in_id:
            self.acc_id += content
        if self.in_name:
            self.acc_name += content

def find_max_is_a_sax(filename):
    start = time.time()
    handler = GoHandler()
    xml.sax.parse(filename, handler)
    time_elapsed = time.time() - start
    return handler.ontology_info, time_elapsed


filename = r"C:\Users\admin\Desktop\go_obo.xml"   


dom_result, dom_time = find_max_is_a_dom(filename)
print("DOM results:")
for ont in dom_result:
    print(f"{ont}: id={dom_result[ont]['id']} name={dom_result[ont]['name']} is_a_count={dom_result[ont]['max_is_a']}")
print(f"DOM extraction time: {dom_time:.4f} seconds\n")


sax_result, sax_time = find_max_is_a_sax(filename)
print("SAX results:")
for ont in sax_result:
    print(f"{ont}: id={sax_result[ont]['id']} name={sax_result[ont]['name']} is_a_count={sax_result[ont]['max_is_a']}")
print(f"SAX extraction time: {sax_time:.4f} seconds\n")


if dom_time < sax_time:
    print("# DOM API was faster.")
else:
    print("# SAX API was faster.")


# SAX API was faster.
