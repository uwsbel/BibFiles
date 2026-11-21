#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Collect the BibTeX entries a paper cites into one self-contained .bib file.

Use it when you hand LaTeX sources to someone who does not have the BibFiles collection (a co-author,
a journal, arXiv), so you do not have to send all the topic files:

    python3 compileBibRefs.py main.tex /path/to/BibFiles refs.bib

then point the copy you send at the new file: \bibliography{refs}.

What it does:
  * reads main.tex AND every file it pulls in with \input, \include, \subfile or \import;
  * finds every cited key in every citation form: \cite, \citep, \citet, \cite[p.~3]{..},
    \citeauthor, \nocite, and biblatex's \parencite, \textcite, \autocite, \footcite, ...;
    \nocite{*} copies every entry;
  * copies those entries out of the *.bib files in the BibFiles folder, plus the @string macros and
    @preamble blocks, and the crossref parents the entries need;
  * ignores commented-out lines and verbatim blocks.

It exits with status 1 (after writing the file) when a cited key is in no .bib file, and prints the
missing keys, so a short bibliography does not go out unnoticed.

Pure Python 3 standard library; runs the same on Windows, Linux and macOS.
Created by Milad Rakhsha. Contributors: Dan Negrut.
"""
import os
import re
import sys

VERBATIM = ("verbatim", "Verbatim", "lstlisting", "minted", "comment")
BEGIN_VERB = re.compile(r'\\begin\{(' + '|'.join(VERBATIM) + r')\}')
END_VERB = re.compile(r'\\end\{(' + '|'.join(VERBATIM) + r')\}')
INPUT = re.compile(r'\\(?:input|include|subfile)\s*\{([^}]*)\}')
IMPORT = re.compile(r'\\(?:sub)?import\s*\{([^}]*)\}\s*\{([^}]*)\}')
CITE = re.compile(r'\\([A-Za-z]*[Cc]ite[A-Za-z]*)\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}')
NOT_A_CITATION = {"citestyle", "citeindextype", "citeindextrue", "citeindexfalse"}
CROSSREF = re.compile(r'\bcrossref\s*=\s*[{"]\s*([^}"\s]+)', re.I)


def strip_comment(line):
    """Drop everything from the first % that is not escaped as \\%."""
    for i, ch in enumerate(line):
        if ch == "%":
            backslashes, j = 0, i - 1
            while j >= 0 and line[j] == "\\":
                backslashes += 1
                j -= 1
            if backslashes % 2 == 0:
                return line[:i]
    return line


def find_tex(name, dirs):
    for d in dirs:
        for cand in (name, name + ".tex"):
            p = os.path.normpath(os.path.join(d, cand))
            if os.path.isfile(p):
                return p
    return None


def scan_tex(main_tex):
    """Return (cited keys in order of first use, \\nocite{*} seen, files read, files not found)."""
    root = os.path.dirname(os.path.abspath(main_tex))
    keys, seen, missing_files = [], set(), []
    nocite_all = [False]

    def walk(path):
        path = os.path.abspath(path)
        if path in seen:
            return
        seen.add(path)
        here = os.path.dirname(path)
        verb = []
        with open(path, encoding="utf-8", errors="replace") as fh:
            for raw in fh:
                if verb:
                    m = END_VERB.search(raw)
                    if m and m.group(1) == verb[-1]:
                        verb.pop()
                    continue
                m = BEGIN_VERB.search(raw)
                if m:
                    verb.append(m.group(1))
                    continue
                code = strip_comment(raw)
                for m in CITE.finditer(code):
                    if m.group(1).lower() in NOT_A_CITATION:
                        continue
                    for k in (x.strip() for x in m.group(2).split(",")):
                        if k == "*":
                            nocite_all[0] = True
                        elif k and k not in keys:
                            keys.append(k)
                for m in INPUT.finditer(code):
                    child = find_tex(m.group(1).strip(), [root, here])   # LaTeX resolves from the main file's folder
                    if child:
                        walk(child)
                    else:
                        missing_files.append(m.group(1).strip())
                for m in IMPORT.finditer(code):
                    child = find_tex(m.group(2).strip(), [os.path.join(here, m.group(1).strip()),
                                                          os.path.join(root, m.group(1).strip())])
                    if child:
                        walk(child)
                    else:
                        missing_files.append(m.group(1).strip() + m.group(2).strip())

    walk(main_tex)
    return keys, nocite_all[0], sorted(seen), missing_files


def parse_bib(text):
    """Yield (type, key, block) for each @-block. Braces are matched, so an @ or a comma inside a field
    does not end an entry; text between blocks (curators' comments) is skipped."""
    i, n = 0, len(text)
    while True:
        j = text.find("@", i)
        if j < 0:
            return
        m = re.match(r'@\s*([A-Za-z]+)\s*([({])', text[j:])
        if not m:
            i = j + 1
            continue
        typ, opener = m.group(1).lower(), m.group(2)
        p, depth = j + m.end(), 0
        while p < n:
            c = text[p]
            if c == "{":
                depth += 1
            elif c == "}":
                if depth == 0 and opener == "{":
                    break
                depth -= 1
            elif c == ")" and opener == "(" and depth == 0:
                break
            p += 1
        key = ""
        if typ not in ("string", "preamble", "comment"):
            key = text[j + m.end():p].split(",", 1)[0].strip()
        yield typ, key, text[j:p + 1]
        i = p + 1


def main():
    if len(sys.argv) < 3:
        print("usage: python3 compileBibRefs.py SOURCE.tex PATH/TO/BibFiles [output.bib]")
        return 2
    tex, bib_dir = sys.argv[1], sys.argv[2]
    out_name = sys.argv[3] if len(sys.argv) > 3 else "refs.bib"
    if not os.path.isfile(tex):
        print("ERROR: %s not found" % tex)
        return 2
    bib_files = sorted(os.path.join(bib_dir, f) for f in os.listdir(bib_dir) if f.lower().endswith(".bib"))
    if not bib_files:
        print("ERROR: no .bib files in %s" % bib_dir)
        return 2

    keys, nocite_all, tex_files, missing_files = scan_tex(tex)
    print("Read %d .tex file(s) starting from %s; %d distinct keys cited%s."
          % (len(tex_files), tex, len(keys), ", plus \\nocite{*}" if nocite_all else ""))
    for f in missing_files:
        print("  note: could not find included file '%s'; its citations are not counted" % f)

    entries, order, strings, preambles, dups = {}, [], [], [], []
    for path in bib_files:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for typ, key, block in parse_bib(text):
            if typ == "string":
                if block not in strings:
                    strings.append(block)
            elif typ == "preamble":
                if block not in preambles:
                    preambles.append(block)
            elif typ != "comment" and key:
                lk = key.lower()          # BibTeX matches keys case-insensitively and keeps the first
                if lk in entries:
                    dups.append("%s (%s)" % (key, os.path.basename(path)))
                    continue
                entries[lk] = (key, block)
                order.append(lk)

    wanted = list(order) if nocite_all else [k.lower() for k in keys]
    out, written, missing, parents = [], [], [], []
    for lk in wanted:
        if lk not in entries:
            missing.append(lk)
            continue
        out.append(entries[lk][1])
        written.append(lk)
        m = CROSSREF.search(entries[lk][1])
        if m and m.group(1).lower() not in wanted and m.group(1).lower() not in parents:
            parents.append(m.group(1).lower())
    for lk in parents:                    # BibTeX wants crossref parents after the entries that use them
        if lk in entries:
            out.append(entries[lk][1])
            written.append(lk)

    with open(out_name, "w", encoding="utf-8") as fh:
        fh.write("% Entries cited by " + os.path.basename(tex) + ", extracted from BibFiles by compileBibRefs.py.\n\n")
        for block in strings + preambles + out:
            fh.write(block + "\n\n")
    print("Wrote %d entries to %s (from %d .bib files in %s)." % (len(written), out_name, len(bib_files), bib_dir))
    if dups:
        print("  note: keys defined more than once; the first was kept: " + ", ".join(dups))
    if missing:
        orig = [k for k in keys if k.lower() in missing]
        print("MISSING: %d cited key(s) are in no .bib file and will print as [?]: %s"
              % (len(orig), ", ".join(orig)))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
