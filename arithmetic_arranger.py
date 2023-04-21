def arithmetic_arranger(problems, count=False):

  # create empty strings for return
  s1, s2, s3, s4 = '', '', '', ''

  # if too many problems
  if len(problems) > 5:
    return "Error: Too many problems."
    
  for i in problems:
    # find numbers and operator
    n1, z, n2 = i.split()

    # if operator isn't + or -
    if z != '+' and z != '-':
      return "Error: Operator must be '+' or '-'."

    #if numbers aren't numbers
    try:
      int(n1) + int(n2)
    except:
      return "Error: Numbers must only contain digits."

    # calculate max len of number
    m_len = max(len(n1), len(n2))

    # if number too long
    if m_len > 4:
      return "Error: Numbers cannot be more than four digits."

    # calculate the whole lenght of problem
    problem_len = m_len + 2

    # generate new parts of strings
    s1 += f"{' '*(problem_len-len(n1))}{n1}    "
    s2 += f"{z}{' '*(problem_len-len(n2) - 1)}{n2}    "
    s3 += f"{'-'*problem_len}    "

    # if the additional parametr exist
    if count:
      if z == '+':
        itog = int(n1) + int(n2)
      elif z == '-':
        itog = int(n1) - int(n2)
      s4 += f"{' '*(problem_len-len(str(itog)))}{itog}    "

  # cut strings and add enter
  s1 = s1[:-4] + '\n'
  s2 = s2[:-4] + '\n'
  s3 = s3[:-4] + '\n'
  s4 = s4[:-4]

  # if the additional parametr exist
  if count:
    arranged_problems = s1 + s2 + s3 + s4
  else:
    s3 = s3[:-1]
    arranged_problems = s1 + s2 + s3
  
  return arranged_problems
