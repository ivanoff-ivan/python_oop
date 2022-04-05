from document_managment.project.category import Category
from document_managment.project.document import Document
from document_managment.project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def find_object(objects_list, object_id):
        current_object = [obj for obj in objects_list if obj.id == object_id]
        return current_object[0]

    def edit_category(self, category_id, new_name):
        current_category = self.find_object(self.categories, category_id)
        current_category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        current_topic = self.find_object(self.topics, topic_id)
        current_topic.topic = new_topic
        current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        current_document = self.find_object(self.documents, document_id)
        current_document.file_name = new_file_name

    def delete_category(self, category_id):
        current_category = self.find_object(self.categories, category_id)
        self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = self.find_object(self.topics, topic_id)
        self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_document = self.find_object(self.documents, document_id)
        self.documents.remove(current_document)

    def get_document(self, document_id):
        current_document = self.find_object(self.documents, document_id)
        return current_document

    def __repr__(self):
        docs = ""
        for i in range(len(self.documents)):
            docs += str(self.documents[i]) + "\n"
        return docs[:-1]


from document_managment.project.category import Category
from document_managment.project.document import Document
from document_managment.project.storage import Storage
from document_managment.project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
