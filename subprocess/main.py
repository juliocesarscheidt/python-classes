import subprocess

def runcmd(cmd, verbose = False):
  process = subprocess.Popen(
    cmd,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    text = True,
    shell = True
  )
  std_out, std_err = process.communicate()
  if verbose:
    print(std_out.strip(), std_err)
  return std_out, std_err

if __name__ in '__main__':
  runcmd('echo "hello world"', True)
  # hello world
