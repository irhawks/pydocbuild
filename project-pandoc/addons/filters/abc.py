#!/usr/bin/env python3

"""
Pandoc filter to process code blocks with class "abc" containing
ABC notation into images.  Assumes that abcm2ps and ImageMagick's
convert are in the path.  Images are put in the abc-images directory.
"""

import hashlib
import os
import sys
from pandocfilters import toJSONFilter, Para, Image
from subprocess import Popen, PIPE, call



def sha1(x):
    return hashlib.sha1(x.encode(sys.getfilesystemencoding())).hexdigest()


def abc2eps(abc, filetype, outfile):
    """
    Compile abc code in markdown
    """
    p = Popen(["abcm2ps", "-O", outfile + '.eps', "-"], stdin=PIPE)
    p.stdin.write(abc)
    p.communicate()
    p.stdin.close()
    call(["convert", outfile + '.eps', outfile + '.' + filetype])


def abc(key, value, format, meta):
    """
    Processing Logic
    1. locate specify element to parse: CodeBlock::abc-notes
    2. then determine where to output and the format to output
    3. the above operation is in order to tell abcm2ps to compile a note.
    4. write output to document.
    5. if target already exists, do not compile again
    """

    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        if "abc-notes" in classes:
            try: 
                imagedir = meta['filter.abc.imagedir']['c'][0]['c']
            except:
                imagedir = 'target/abc-images'
            imagelinkdir = "../abc-images"
            outfile = imagedir + '/' + sha1(code)

            if format == "html":
                filetype = "png"
            elif format == "latex":
                filetype = "pdf"
            else:
                filetype = "png"

            src = outfile + '.' + filetype
            sys.stderr.write("filter.abc: "+src+'\n')
            # sys.stderr.write("filter.abc: "+value.__str__()+'\n')

            if not os.path.isfile(src):
                try:
                    os.mkdir(imagedir)
                    sys.stderr.write('Created directory ' + imagedir + '\n')
                except OSError:
                    pass
                abc2eps(code.encode("utf-8"), filetype, outfile)
                sys.stderr.write('Created image ' + src + '\n')

            return Para([Image([], [imagelinkdir+'/'+sha1(code)+'.'+filetype, ""])])

if __name__ == "__main__":
    toJSONFilter(abc)
