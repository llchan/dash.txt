#!/usr/bin/env python

import re
import bottle as btl

DIVIDER_RE = re.compile(r'^===+$')
CHECKBOX_RE = re.compile(r'^\s*\[([^\]]*)\]\s*(\S.*)$')

@btl.route('/')
def dash():
    with open(btl.request.app.path) as f:
        raw = f.read()
    lines = raw.splitlines()
    divider_idx = [i for i, l in enumerate(lines) if DIVIDER_RE.match(l)]
    categories = [lines[i - 1] for i in divider_idx]
    data = []
    for i in range(len(divider_idx)):
        cat = categories[i]
        if i >= len(divider_idx) - 1:
            rows = lines[(divider_idx[i] + 1):]
        else:
            rows = lines[(divider_idx[i] + 1):(divider_idx[i+1] - 1)]
        items = []
        for r in rows:
            if r.strip() == '':
                continue
            match = CHECKBOX_RE.match(r)
            done = False
            if not match:
                continue
            if match.group(1).strip() != '':
                done = True
            items.append((done, match.group(2)))
        data.append((categories[i], items))
    return btl.template('dash.tpl', data=data)

@btl.route('/static/<filepath:path>')
def static(filepath):
    return btl.static_file(filepath, root='./static/')

def main(path, host='localhost', port=8080):
    app = btl.default_app()
    app.path = path
    btl.run(app=app, host=host, port=port, reloader=True)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=8080)

    args = parser.parse_args()
    main(**vars(args))
