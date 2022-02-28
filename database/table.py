class Table:
    def __init__(self, *fields):
        self.data = []
        self.cursor = 0
        self.fields = fields

    def validate(self, **params):
        if not isinstance(params, dict): print("We are expecting a proper dictionary")
        elif not params: print("We are not expecting an empty dictionary")
        elif sorted(tuple(params.keys())) != sorted(self.fields):
            for keys in params.keys():
                if keys not in self.fields:
                    print("The keys don't match. Check your input")
                    return False
                else: return True
        else: return True

    def insert(self, **params):
        # Requirements:
        #   - Add a record entry to the self.data dictionary
        if self.validate(**params):
            if '_id' not in self.fields:
                self.fields = list(self.fields)
                self.fields.append('_id')
            params['_id'] = len(self.data)+1
            self.data.append((params))


        #   - BUT ::::
        #   - Validate that params is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Ensure to generate a record id for the new record using the cursor attribute. Note: ids must always start
        #   from 1
        #   - Ensure to use generated id as key for insert and also inject into the actual record to be inserted with
        #   the key => _id
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a dictionary representing the record that has just been successfully inserted

        # Remove the pass statement below and add your implementation there ...

    def select(self, **conditions):
        if self.validate(**conditions):
            answers = []  # In case answer is empty
            for query in conditions:
                answers = [details for details in self.data if query in details and conditions[query] == details[query]]
            return answers


        # Requirements:
        #   - Filter and return records that has values matching those in the conditions argument
        #   - BUT ::::
        #   - Validate that conditions is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a list of dictionaries representing records that matched entires in the conditions argument

        # Remove the pass statement below and add your implementation there ...
        pass


if __name__ == '__main__':
    tb = Table('name', 'age', 'sex')
    tb.insert(name="Marky", sex="m", age="20")
    print(tb.fields, tb.data)

