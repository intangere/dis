import sys

def exec_(mem, length):
    a = 0
    c = 0
    d = 0
    x = 0
    p3 = [1,3,9,27,81,243,729,2187,6561,19683];

    while True:
     if mem[c] == ord('*'):
          d = mem[d];
     elif mem[c] == ord('^'):
          c = mem[d];
     elif mem[c] == ord('>'):
          mem[d] = mem[d] // 3 + mem[d] % 3 * 19683
          a = mem[d]
     elif mem[c] == ord('|'):
       i = 0
       j = 0
       while j < 10:
         i += ( a // p3[j] % 3 - mem[d] // p3[j] % 3 + 3 ) % 3 * p3[j];
         j += 1
       mem[d] = i
       a = mem[d]
     elif mem[c] == ord('{'):
        if a == 59048:
           return
        if x == 10:
           print('\n', end='')
        print(chr(a), end='')
     elif mem[c] == ord('}'):
        x = sys.stdin.read(1)
        if x == '\n':
           a = 10
        elif x == '': #EOF unimp
           a = 59048
        else:
           a = ord(x)
     elif mem[c] == ord('!'):
        return

     if c == 59048:
        c = 0
     else:
        c += 1

     if d == 59048:
        d = 0
     else:
        d += 1

if __name__ == '__main__':
   if len(sys.argv) < 2:
      print('File name missing!')
      sys.exit(1)

   with open(sys.argv[1], 'r') as f:
     program = ''.join([_.strip() for _ in f.readlines()])
     i = 0
     mem = []
     mem = [0] * 59049

     skipping = False
     macro = False
     sub_program = ''
     expanded_program = ''
     for _, x in enumerate(program):
       if x in ['*', '^', '>', '|', '{', '}', '_', '!'] and not skipping and not macro:
          if i == 59049:
             print('input file too large')
             sys.exit(1)
          mem[i] = ord(x)
          i += 1
       elif x == '(':
          skipping = True
       elif x == ')':
          skipping = False
       elif x == '/':
          if not macro:
             macro = True
          else:
             expand_amount = int(''.join(filter(str.isdigit, sub_program)))
             expanded_program = program.split('/'+sub_program+'/', 1)
             for _ in range(expand_amount):
                 while i < expand_amount:
                    mem[i] = ord(sub_program[-1])
                    i+=1
                    expanded_program[0]+=sub_program[-1]
             expanded_program=''.join(expanded_program)
             macro = False
       elif macro:
         sub_program += x

   if '--dump-mem' in sys.argv:
      print(mem)
      sys.exit(1)

   if '--expand' in sys.argv:
      print(expanded_program)
      sys.exit(1)

   exec_(mem, i)
   sys.exit(0)
