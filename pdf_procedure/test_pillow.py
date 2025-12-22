from PIL import Image
import os

def cp_mv_imgs(source_path,target_dir):
    img_files = os.listdir(source_path) 

    n = 1
    for img_file in img_files:
        img_path = os.path.join(source_path,img_file) 
        img = Image.open(img_path)
        target_img_file = str(n)+".jpg"
        n += 1

        target_path = os.path.join(target_dir,target_img_file)
        img.save(target_path)

def to_pdf(source_dir,target_path):
    #把图片存入列表valid_imgs
    files = os.listdir(source_dir) 
    files_path_list = [os.path.join(source_dir,file) for file in files]
    valid_imgs = []
    for file in files_path_list:
        img = Image.open(file)
        valid_imgs.append(img)

    #处理第一张图片
    first_img = valid_imgs[0]

    first_img.save(target_path,"PDF",save_all = True)
    #处理后续图片
    if len(valid_imgs) > 1:
        #获取目标路径
        other_imgs = valid_imgs[1:]
        first_img.save(target_path,"PDF",save_all = True,append_images = other_imgs)
source = "D:\\saved_imgs"
target =  "D:\\pdfs\\name.pdf"
to_pdf(source,target)       





'''def main():
    source_path = "C:\\Users\\liubo\\Documents\\xwechat_files\\wxid_v3ipf5xcn1lc22_82cf\\temp\\ImageUtils"
    target_dir = "D:\\saved_imgs"
    cp_mv_imgs(source_path,target_dir)
    source = "D:\\saved_imgs"
    target =  "D:\\pdfs"
    to_pdf(source,target)

if __name__ == "__main__":
    main()'''