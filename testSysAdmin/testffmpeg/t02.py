# %%
## goal: transcode rmvb and avi files to mp4, for better compatibility with dolphone file explorer

fps = [
# "/home/wenchen/zfs_tank/netStore01/download.video.d/000_TOP/Life_of_Pi (2012)/少年派的奇幻漂流.720p.BD中英双字幕.rar",
    "/home/wenchen/zfs_tank/netStore01/download.video.d/000_TOP/Pirates_of_the_Caribbean (2003)/加勒比海盗3CD2.rmvb",
    "/home/wenchen/zfs_tank/netStore01/download.video.d/000_TOP/Seven_Deadly_Sins (2010)/七宗罪BD全集[www.xiagun.com].rmvb",
    "/home/wenchen/zfs_tank/netStore01/download.video.d/000_TOP/The_Matrix (1999)/黑客帝国1BD版[www.qire123.com].rmvb",
    "/home/wenchen/zfs_tank/netStore01/download.video.d/000_TOP/The_Wolf_of_Wall_Street (2013)/【The Wolf of Wall Street】【DVD-RMVB.中字】.rmvb",
    "/home/wenchen/zfs_tank/netStore01/download.video.d/000_TOP/Vanilla_Sky (2001)/Vanilla.sky.香草天空.双语字幕.HR-HDTV.AC3.960X540.x264-人人影视制作(ED2000.COM).avi",
    "/home/wenchen/zfs_tank/netStore01/download.video.d/000_TOP/Whiplash (2014)/爆裂鼓手BD中英双字1280高清【6v电影www.6vhao.net】.rmvb",
]

import os
# os.system("echo 'he'")
# print(cmd02)
# os.system("ffmpeg")
# cmd03 = "ls '{}'".format(fps[0])
# print(cmd03)
cmd = """
time ffmpeg -hwaccel cuda -i '{}' -crf 24 \
    -vcodec hevc_nvenc -preset slow \
    -pixel_format yuv420p \
    '{}/{}.t01.mp4'
"""
for i in range(len(fps)):
    dir_str = os.path.dirname(fps[i])
    files = os.listdir(dir_str)
    for f in files:
        if not f.endswith(".rmvb") or f.startswith("."):
            continue
        if os.path.exists("'{}/{}.t01.mp4'".format(dir_str, f)):
            continue
        input_f = dir_str + "/" + f
        cmd02 = cmd.format(input_f, dir_str, f)
        cmd04 = "ffprobe {} 2>> {}/README.org".format(input_f, dir_str)
        # print(cmd02)
        os.system(cmd04)
        os.system(cmd02)

# %%

import os
cmd = """
time ffmpeg -hwaccel cuda -i '{}' -crf 24 \
    -vcodec hevc_nvenc -preset slow \
    -pixel_format yuv420p \
    '{}/{}.t01.mp4'
"""
# for i in range(len(fps)):
if 0:
    dir_str = os.path.dirname(fps[i])
    files = os.listdir(dir_str)
    for f in files:
        if not f.endswith(".rmvb") or f.startswith("."):
            continue
        if os.path.exists("'{}/{}.t01.mp4'".format(dir_str, f)):
            continue
        input_f = dir_str + "/" + f
        cmd02 = cmd.format(input_f, dir_str, f)
        cmd04 = "ffprobe {} 2>> {}/README.org".format(input_f, dir_str)
        # print(cmd02)
        os.system(cmd04)
        os.system(cmd02)
# %%
## detecting .rmvb and .avi files
root_dir = "/home/wenchen/zfs_tank/netStore01/download.video.d/010_PRESERVE/"
f_dirs = os.listdir(root_dir)
for f_dir in f_dirs:
    if not os.path.isdir(root_dir + f_dir ):
        continue
    fps = os.listdir(root_dir + f_dir)
    for f in fps:
        if (f.endswith(".rmvb") or f.endswith(".avi")) and not f.startswith("."):
            print(root_dir + f_dir + "/"+ f)
            input_f =  root_dir + f_dir + "/"+ f
            cmd02 = cmd.format(input_f, root_dir + f_dir, f)
            cmd04 = "ffprobe {} 2>> {}/README.org".format(input_f, root_dir + f_dir)
            os.system(cmd04)
            os.system(cmd02)

# %%
