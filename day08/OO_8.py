class Body:
    dict = {}

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __getitem__(self, key):
        return self.dict[key]

    def __len__(self):
        return len(self.dict)

    def __str__(self):
        # for key in self.dict.keys():
        #     for value in self.dict[key]:
        #         print(key, value)
        return dict

if __name__ == '__main__':
    body = Body()
    print(dict)
    body['height'] = 180
    body['weight'] = 60
    print(dict)
    print(body['height'], body['weight'], len(body))
