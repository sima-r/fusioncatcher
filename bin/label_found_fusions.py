#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
It labels the candidate list of fusion genes generated by 'find_fusion_genes.py'.



Author: Daniel Nicorici, Daniel.Nicorici@gmail.com

Copyright (c) 2009-2016 Daniel Nicorici

This file is part of FusionCatcher.

FusionCatcher is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

FusionCatcher is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with FusionCatcher (see file 'COPYING.txt').  If not, see
<http://www.gnu.org/licenses/>.

By default, FusionCatcher is running BLAT aligner
<http://users.soe.ucsc.edu/~kent/src/> but it offers also the option to disable
all its scripts which make use of BLAT aligner if you choose explicitly to do so.
BLAT's license does not allow to be used for commercial activities. If BLAT
license does not allow to be used in your case then you may still use
FusionCatcher by forcing not use the BLAT aligner by specifying the option
'--skip-blat'. Fore more information regarding BLAT please see its license.

Please, note that FusionCatcher does not require BLAT in order to find
candidate fusion genes!

This file is not running/executing/using BLAT.

"""
import sys
import os
import optparse

if __name__ == '__main__':

    #command line parsing

    usage = "%prog [options]"
    description = """It labels a list of final candidates of fusion genes."""
    version = "%prog 0.10 beta"

    parser = optparse.OptionParser(
        usage = usage,
        description = description,
        version = version)

    parser.add_option("--input","-i",
                      action = "store",
                      type = "string",
                      dest = "input_fusions_filename",
                      help = """The input file in text tab delimited format containing list of final candidates of fusion genes. """)


    parser.add_option("--data","-d",
                      action = "store",
                      type = "string",
                      dest = "input_database_filename",
                      help = """The input text file tab separated format containing gene pairs which are used as filter for labeling (two columns and no header). Be default the order of genes in the a pair is ignored."""
                      )

    parser.add_option("--data-not-commutative","-n",
                      action = "store_true",
                      dest = "not_commutative",
                      default = False,
                      help = """By default the order of genes in the database is ignored. If this is set then the order matters.""")

    parser.add_option("--label","-l",
                      action = "store",
                      type = "string",
                      dest = "label",
                      help = """Label used to mark the found fusion genes.""")

    parser.add_option("--output","-o",
                      action = "store",
                      type = "string",
                      dest = "output_fusions_filename",
                      help = """The output text tab-separated file containing the candidate fusion genes which are found.""")



    (options,args) = parser.parse_args()

    # validate options
    if not (options.input_fusions_filename and
            options.output_fusions_filename and
            options.label
            ):
        parser.print_help()
        parser.error("One of the options has not been specified.")
        sys.exit(1)


    label = options.label

    data = [line.rstrip().split("\t") for line in file(options.input_database_filename,"r").readlines() if line.rstrip()]
    if options.not_commutative:
        data = ['\t'.join(line) for line in data]
    else:
        d = []
        for line in data:
            d.append("%s\t%s" % (line[0],line[1]))
            d.append("%s\t%s" % (line[1],line[0]))
        data = d
    data = set(data)
    
    fusions = [line.rstrip("\r\n").split("\t") for line in file(options.input_fusions_filename,"r").readlines() if line.rstrip("\r\n")]
    if fusions:
        header = fusions.pop(0)

        for line in fusions:
            gene_1 = line[10]
            gene_2 = line[11]
            k = "%s\t%s" % (gene_1,gene_2)
            if k in data:
                if line[2]:
                    line[2] = line[2] + ','+label
                else:
                    line[2] = label

        fusions.insert(0,header)
    
    file(options.output_fusions_filename,"w").writelines(["\t".join(line)+"\n" for line in fusions])
    #...

