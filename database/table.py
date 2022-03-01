class Table:
    def __init__(self, *fields):
        self.data = {}
        self.cursor = 0
        self.fields = fields

    def validate(self, **params):
        if not isinstance(params, dict): print("We are expecting a proper dictionary")
        elif not params: return f"You need to fill in the correct parameters {self.fields}"
        elif sorted(tuple(params.keys())) != sorted(self.fields):
            for keys in params.keys():
                if keys not in self.fields:
                    return f"The keys don't match. Check your input ({self.fields})"
                    # return False
                else: return True
        else: return True

    def insert(self, **params):
        # Requirements:
        #   - Add a record entry to the self.data dictionary
        if self.validate(**params):
            # if '_id' not in self.fields:
            #     self.fields = list(self.fields)
            #     self.fields.append('_id')
            # params['_id'] = len(self.data)+1
            # self.data.append((params))
            self.cursor += 1
            params['_id'] = self.cursor
            self.data[self.cursor] = params
            return params

    def insert2(self, **params):

        if type(params) != dict or params == {}:
            return print("Empty arguments are not allowed")
        elif [key for key in params.keys() if key not in self.fields]:
            return print("Keys don't match expected fields")
        else:
            self.cursor += 1
            params['_id'] = self.cursor
            self.data2[self.cursor] = params
            return params

        #   - BUT ::::
        #   - Validate that params is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Ensure to generate a record id for the new record using the cursor attribute. Note: ids must always start
        #   from 1
        #   - Ensure to use generated id as key for insert and also inject into the actual record to be inserted with
        #   the key => _id
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a dictionary representing the record that has just been successfully inserted


    def select(self, **conditions):
        if self.validate(**conditions):
            for query in conditions:
                answers = [self.data[x] for x in self.data if
                           query in self.data[x] and conditions[query] == self.data[x][query]]
            return answers
        return []


    def select2(self, **conditions):
        if type(conditions) != dict or conditions == {}:
            return print("Empty arguments are not allowed")
        elif [key for key in conditions.keys() if key not in self.fields]:
            return print("Keys don't match expected fields")
        else:
            pass
            # lst = []
            # for num in self.data:
            #     count = 0
            #     for key in conditions.keys():
            #         if conditions[key] == self.data[num][key]:
            #             count += 1
            #     if count == len(query.keys()):
            #         lst.append(rooms[num])
        # Requirements:
        #   - Filter and return records that has values matching those in the conditions argument
        #   - BUT ::::
        #   - Validate that conditions is a (1) dictionary (2) non-empty (3) Keys are in self.fields list
        #   - Manually or allow python to raise appropriate exceptions when there are errors
        #   - Return a list of dictionaries representing records that matched entires in the conditions argument

        # Remove the pass statement below and add your implementation there ...
        pass

