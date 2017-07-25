import squeal as sq
import unittest


#
# test coverages
# 
#    Field   Record    X   Field   Record  =  Field  Record
#---------------------------------------------------------
#001  1        1            1        1         2       1
#002  1        1            1        N         2       N
#003  1        1            M        N       1+M       N
#004  1        1            M        1       1+M       1
#     
#005  1        M            1        1         2       M
#006  1        M            1        N         2      MN
#007  1        M            M        N       1+M      MN
#008  1        M            M        1       1+M       M
#     
#009  N        1            1        1       N+1       1
#010  N        1            1        N       N+1       N
#011  N        1            M        N       N+M       N
#012  N        1            M        1       N+M       1
#     
#013  N        M            1        1       N+1       M
#014  N        M            1        N       N+1      MN
#015  N        M            M        N       N+M      MN
#016  N        M            M        1       N+M       M
#
# special?
#     1        1            1        0         2       ?
#     1        1            1        0         2       ?
#     1        1            M        0       1+M       ?
#     1        1            M        0       1+M       ?



class Test_cartesian_product(unittest.TestCase):
  def test_001_singleField_singleRecord_X_singleField_singleRecord(self):
    test_t1={
      't1_1':['t1_11']
    }
    test_t2={
      't2_1':['t2_11']
    }
    act=sq.cartesian_product(test_t1,test_t2)
    exp={
      't1_1':['t1_11'],
      't2_1':['t2_11'],
    }
    msg="\nFAILED: " +\
        "\n   TESTING VALUES: "+ str( test_t1 ) + " X " + str( test_t2 ) +\
        "\n   TYPE: table( field:1 record:1 ) X table( field:1 record: 1)"
    self.assertEqual(act,exp,msg)


  def test_002_singleField_singleRecord_X_singleField_manyRecord(self):
    test_t1={
      't1_1':
      [
        't1_11'
      ]
    }
    test_t2={
      't2_1':
      [
        't2_11',
        't2_21',
        't2_31',
        't2_41',
        't2_51'
      ]
    }
    act=sq.cartesian_product(test_t1,test_t2)
    exp={
      't1_1':
      [
        't1_11',
        't1_11',
        't1_11',
        't1_11',
        't1_11'  
      ],

      't2_1':
      [
        't2_11',
        't2_21',
        't2_31',
        't2_41',
        't2_51'
      ]
    }
    msg="\nFAILED: " +\
        "\n   TESTING VALUES: "+ str( test_t1 ) + " X " + str( test_t2 ) +\
        "\n   TYPE: table( field:1 record:1 ) X table( field:1 record: M)"
    self.assertEqual(act,exp,msg)


  def test_003_singleField_singleRecord_X_manyField_manyRecord(self):
    test_t1={
      't1_1':
      [
        't1_11'
      ]
    }
    test_t2={
      't2_1':
      [
        't2_11',
        't2_21',
        't2_31',
        't2_41',
        't2_51'
      ],
      't2_2':
      [
        't2_12',
        't2_22',
        't2_32',
        't2_42',
        't2_52'
      ],
      't2_3':
      [
        't2_13',
        't2_23',
        't2_33',
        't2_43',
        't2_53'
      ]
    }
    act=sq.cartesian_product(test_t1,test_t2)
    exp={
      't1_1':
      [
        't1_11',
        't1_11',
        't1_11',
        't1_11',
        't1_11'  
      ],

      't2_1':
      [
        't2_11',
        't2_21',
        't2_31',
        't2_41',
        't2_51'
      ],
      't2_2':
      [
        't2_12',
        't2_22',
        't2_32',
        't2_42',
        't2_52'
      ],
      't2_3':
      [
        't2_13',
        't2_23',
        't2_33',
        't2_43',
        't2_53'
      ]
    }
    msg="\nFAILED: " +\
        "\n   TESTING VALUES: "+ str( test_t1 ) + " X " + str( test_t2 ) +\
        "\n   TYPE: table( field:1 record:1 ) X table( field:M record: M)"
    self.assertEqual(act,exp,msg)



  def test_004_singleField_singleRecord_X_manyField_singleRecord(self):
    test_t1={
      't1_1':
      [
        't1_11'
      ]
    }
    test_t2={
      't2_1':
      [
        't2_11',
      ],
      't2_2':
      [
        't2_12',
      ],
      't2_3':
      [
        't2_13',
      ]
    }
    act=sq.cartesian_product(test_t1,test_t2)
    exp={
      't1_1':
      [
        't1_11',
      ],

      't2_1':
      [
        't2_11',
      ],
      't2_2':
      [
        't2_12',
      ],
      't2_3':
      [
        't2_13',
      ]
    }
    msg="\nFAILED: " +\
        "\n   TESTING VALUES: "+ str( test_t1 ) + " X " + str( test_t2 ) +\
        "\n   TYPE: table( field:1 record:1 ) X table( field:M record: 1)"
    self.assertEqual(act,exp,msg)

# ...






if __name__ == '__main__':
    unittest.main(exit=False)
    


