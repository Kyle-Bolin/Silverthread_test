#test script for find_tumor and find_all_tumors

import find_tumor,find_all_tumors

def test_find_tumor():
    assert find_tumor.find_tumor("Slice_inputs/messy_input.in") == "False,4,4\n"
    assert find_tumor.find_tumor("Slice_inputs/sample_no_tumor.in") == "False,50,80\n"
    assert find_tumor.find_tumor("Slice_inputs/sample_tumor.in") == "True,50,80\n"
    assert find_tumor.find_tumor("Slice_inputs/wrong_size.in") == "Error,NA,NA\n"

def test_find_all_tumors():
    find_all_tumors.find_all_tumors('./Slice_inputs','test.csv')
    t =open('test.csv','r')
    f = open('./Slice_inputs/tumor.csv','r')
    assert t.read() == f.read()
