import os

entries = os.listdir('/mnt/e/Gabriel/deep_motion_mag/data/output')
a = len(entries)
fps = '10'
for n in entries:
   print(n)
   if n != ('.DS_stores' and 'Testes' and 'Vids_outs_reunidos' and 'gimp'):
     os.system('ffmpeg -y -f image2 -r '
               +fps+' -i /mnt/e/Gabriel/deep_motion_mag/data/output/' 
               + n + '/%06d.png -c:v libx264 /mnt/e/Gabriel/deep_motion_mag/data/output/vids_out/'
               + n +'.mp4')
     