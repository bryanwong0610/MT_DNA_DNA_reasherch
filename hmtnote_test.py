from hmtnote_test import annotate
import argparse
def argument_get():
    parser=argparse.ArgumentParser(prog='Hmtnote_tools',description='A python script for cwl in order to use the hmtnote')
    parser.add_argument('-sample_name','-s',type=str,help='Sample Name')
    parser.add_argument('-input_vcf','-i',type=str,help='Input the unannotated vcf')
    args, _ = parser.parse_known_args()
    args = vars(args)
    print(args) #test
    return args
args= argument_get()
output_result=args['sample_name']+'_hmtnote_annotate.vcf'
annotate(args['input_vcf'],output_result,basic=True,crossref=True,variab=True,predict=True,csv=True,offline=True)