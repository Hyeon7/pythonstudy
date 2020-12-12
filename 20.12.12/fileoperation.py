import os
import pathlib
import glob
import shutil

#print(os.path.exists('text.txt'))
#print(os.path.isfile('text.txt'))
#print(os.path.isdir('design'))

#os.rename('test.txt', 'rename.txt')
#os.symlink('rename.txt', 'symlink.txt')

#os.mkdir('test_dir')
#os.rmdir('test_dir')

#pathlib.Path('empty.txt').touch()
#os.remove('empty.txt')

#os.mkdir('test_dir')
#os.mkdir('test_dir/test_dir2')
#print(os.listdir('test_dir'))
#pathlib.Path('test_dir/test_dir2/empty.txt').touch()
#shutil.copy('test_dir/test_dir2/empty.txt', #'test_dir/test_dir2/empty.txt2')
#print(glob.glob('test_dir/test_dir2/*'))
#shutil.rmtree('test_dir')

print(os.getcwd())