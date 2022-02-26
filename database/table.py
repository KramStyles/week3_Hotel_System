
class Table:
    def __init__(self, *fields):
        self.data = {}
        self.cursor = 0
        self.fields = fields

    def insert(self, **params):
        # Requirements:
        #   - Add a record entry to the self.data dictionary

        #   - BUT ::::
        #   - Validate that params is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Ensure to generate a record id for the new record using the cursor attribute. Note: ids must always start from 1
        #   - Ensure to use generated id as key for insert and also inject into the actual record to be inserted with the key => _id
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a dictionary representing the record that has just been successfully inserted

        # Remove the pass statement below and add your implementation there ...
        pass

    def select(self, **conditions):
        # Requirements:
        #   - Filter and return records that has values matching those in the conditions argument
        #   - BUT ::::
        #   - Validate that conditions is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a list of dictionaries representing records that matched entires in the conditions argument

        # Remove the pass statement below and add your implementation there ...
        pass
