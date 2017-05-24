#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )

    import apiai


# demo agent acess token: e5dc21cab6df451c866bf5efacb40178

CLIENT_ACCESS_TOKEN = 'ACCESS_TOKEN'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    while True:
        print(u"> ", end=u"")
        user_message = input()

        if user_message == u"exit":
            break

        request = ai.text_request()
        request.query = user_message

        raw_response = request.getresponse().read().decode("utf-8")
        response = json.loads(raw_response)

        result = response['result']
        print("result: " + str(result))
        action = result.get('action')
        print("action: " + str(action))

        action_incomplete = result.get('actionIncomplete', False)

        print(u"< %s" % response['result']['fulfillment']['speech'])

        if action is not None:
            if action == u"input.welcome":
                print("action")
                parameters = result['parameters']

                text = parameters.get('text')
                message_type = parameters.get('message_type')
                parent = parameters.get('parent')

                print(
                    'text: %s, message_type: %s, parent: %s' %
                    (
                        text if text else "null",
                        message_type if message_type else "null",
                        parent if parent else "null"
                    )
                )

                if not action_incomplete:
                    print(u"...Sending Message...")
                    break


if __name__ == '__main__':
    main()
