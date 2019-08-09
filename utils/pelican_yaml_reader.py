from pelican import signals
from pelican.readers import BaseReader
import yaml
from datetime import datetime


# Cribbed from http://docs.getpelican.com/en/3.6.3/plugins.html


# Create a new reader class, inheriting from the pelican.reader.BaseReader
class YamlReader(BaseReader):
    enabled = True  # Yeah, you probably want that :-)

    # The list of file extensions you want this reader to match with.
    # If multiple readers were to use the same extension, the latest will
    # win (so the one you're defining here, most probably).
    file_extensions = ['yaml']

    # You need to have a read method, which takes a filename and returns
    # some content and the associated metadata.

    def process_date(self, date_info):

        return datetime(year=date_info['Year'],
                        month=date_info['Month'],
                        day=date_info['Day'])

    def read(self, filename):

        with open(filename) as handle:
            info = yaml.load(handle)
            info['date'] = self.process_date(info['pub_date'])
            info['template'] = 'paper'
            return '', info


def add_reader(readers):
    readers.reader_classes['yaml'] = YamlReader


# This is how pelican works.
def register():
    signals.readers_init.connect(add_reader)
