class Table:
    def __init__(self, *fields):
        self.data = {}
        self.cursor = 0
        self.fields = fields

    def validate(self, **params):
        try:
            if not isinstance(params, dict):
                print("We are expecting a proper dictionary")
            elif not params:
                return f"You need to fill in the correct parameters {self.fields}"
            elif sorted(tuple(params.keys())) != sorted(self.fields):
                for keys in params.keys():
                    if keys not in self.fields and keys != '_id':
                        return f"The keys don't match. Check your input ({self.fields})"
                    else:
                        return 'ok'
            else:
                return 'ok'
        except Exception as err:
            return err


    def insert(self, **params):
        # Requirements:
        #   - Add a record entry to the self.data dictionary
        if self.validate(**params) == 'ok':
            self.cursor += 1
            params['_id'] = self.cursor
            self.data[self.cursor] = params
            return params
        else:
            return self.validate(**params)

    def select(self, **conditions):
        if self.validate(**conditions) == 'ok':
            for query in conditions:
                answers = [self.data[x] for x in self.data if
                           query in self.data[x] and conditions[query] == self.data[x][query]]
            return answers
        else: return self.validate(**conditions)
