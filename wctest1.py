import os
import sys
from optparse import OptionParser


def opt():
    parser = OptionParser()

    parser.add_option("-c", "--chars",
                      dest="chars",
                      action="store_true",
                      default=False,
                      help="only count chars.")
    parser.add_option("-w", "--words",
                      dest="words",
                      action="store_true",
                      default=False,
                      help="only count words.")
    parser.add_option("-l", "--lines",
                      dest="lines",
                      action="store_true",
                      default=False,
                      help="only count lines.")
    parser.add_option("-n", "--nototal",
                      dest="nototal",
                      action="store_true",
                      default=False,
                      help="not print total count.")
    options, args = parser.parse_args()

    return options, args


def get_Count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return lines, words, chars


def print_wc(options, lines, words, chars, fn):
    if options.lines:
        print
        lines,
    if options.words:
        print
        words,
    if options.chars:
        print
        chars,
    print
    fn


def main():
    options, args = opt()
    if not (options.chars or options.words or options.lines):
        options.chars, options.words, options.lines = True, True, True
    if args:
        total_lines, total_words, total_chars = 0, 0, 0
        for fn in args:
            if os.path.isfile(fn):
                with open(fn) as fd:
                    data = fd.read()
                    lines, words, chars = get_Count(data)
                    print_wc(options, lines, words, chars, fn)
                    total_lines += lines
                    total_words += words
                    total_chars += chars
            elif os.path.isdir(fn):
                print >> sys.stderr, "%s: is a directory." % fn
            else:
                sys.stderr.write("%s: No such file or directory.\n" % fn)
        if len(args) > 1:
            if not options.total:
                print_wc(options, total_lines, total_words, total_chars, 'total')

    else:
        data = sys.stdin.read()
        fn = ""
        lines, words, chars = get_Count(data)
        print_wc(options, lines, words, chars, fn)


if __name__ == '__main__':
    main()