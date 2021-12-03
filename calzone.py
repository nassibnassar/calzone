import sys
import xlsxwriter


helptext = """
Usage:  calzone <inputfile>
"""


colors = ['black', 'blue', 'brown', 'green', 'purple', 'yellow', 'red']


def runhelp():
    print(helptext)


def makeworkbook(lines, workbook):
    if len(lines) < 1:
        return
    worksheet = workbook.add_worksheet()
    # Set column widths
    for i, line in enumerate(lines):
        width = 16 if i == 0 else 4
        sp = line.split('|')
        for field in sp:
            f = field.strip()
            if len(f) > width:
                width = len(f)
        worksheet.set_column(i, i, width + 2)
    # Write data
    last = 0
    for i, s in enumerate(lines):
        sp = s.split('|')
        if i == 0:
            alignh = 'right'
        else:
            alignh = 'center'
        for j, f in enumerate(sp):
            fmt = workbook.add_format()
            fmt.set_bold()
            fmt.set_align('top')
            fmt.set_align(alignh)
            fmt.set_bg_color('#F0F8FF')
            fmt.set_font_color(colors[j])
            worksheet.write(j, i, f.strip(), fmt)
            if j > last:
                last = j
    m = last + 1
    while m < 100:
        for n in range(len(lines)):
            if n == 0:
                continue
            fmt = workbook.add_format()
            fmt.set_align('top')
            fmt.set_align('center')
            worksheet.write(m, n, '', fmt)
        m += 1
    worksheet.freeze_panes(last + 1, 1)


def striplines(lines):
    newlines = []
    for i, line in enumerate(lines):
        s = line.strip()
        if s != '':
            newlines.append(s)
    return newlines


def calzone(argv):
    with open(argv[1]) as f:
        lines = f.readlines()
    lines = striplines(lines)
    workbook = xlsxwriter.Workbook(argv[1]+'.xlsx')
    try:
        makeworkbook(lines, workbook)
    finally:
        workbook.close()


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        runhelp()
    else:
        calzone(sys.argv)
